"""DBA desde Cero — app de curso interactivo (v1).

Estructura:
- El contenido vive en /contenido/*.json (niveles -> lecciones -> páginas/quiz).
- El progreso se guarda en Supabase (db.py) o en sesión si no hay credenciales.
- Una lección se completa aprobando su quiz (>= 70%). Las lecciones se
  desbloquean en orden.
"""
import json
import re
from pathlib import Path

import streamlit as st

import db

st.set_page_config(page_title="DBA desde Cero", page_icon="🛢️", layout="centered")

APROBACION = 0.7  # 70% del quiz para aprobar
DIR_CONTENIDO = Path(__file__).parent / "contenido"


# ------------------------------------------------------------- contenido ---

@st.cache_data
def cargar_niveles() -> list[dict]:
    niveles = []
    for ruta in sorted(DIR_CONTENIDO.glob("nivel*.json")):
        with open(ruta, encoding="utf-8") as f:
            niveles.append(json.load(f))
    return niveles


def todas_las_lecciones(niveles) -> list[dict]:
    lecciones = []
    for nivel in niveles:
        for lec in nivel["lecciones"]:
            lecciones.append(lec)
    return lecciones


def normalizar(texto: str) -> str:
    """Para validar comandos: minúsculas, espacios colapsados, sin ; final."""
    texto = texto.strip().lower().rstrip(";").strip()
    return re.sub(r"\s+", " ", texto).strip()


# ----------------------------------------------------------------- login ---

def vista_login():
    st.title("🛢️ DBA desde Cero")
    st.caption("De no saber nada, a experto en bases de datos Oracle. Paso a paso.")
    if db.get_client() is None:
        st.info(
            "Estás en **modo invitado** (sin Supabase configurado): puedes usar "
            "todo el curso, pero el progreso se pierde al cerrar. Para hacerlo "
            "persistente, configura los secrets (ver README)."
        )
    tab_entrar, tab_crear = st.tabs(["Entrar", "Crear cuenta"])
    with tab_entrar:
        usuario = st.text_input("Usuario", key="login_usuario")
        pin = st.text_input("PIN (4+ dígitos)", type="password", key="login_pin")
        if st.button("Entrar", type="primary", use_container_width=True):
            if usuario and pin and db.validar_usuario(usuario.strip(), pin):
                st.session_state.usuario = usuario.strip()
                st.rerun()
            else:
                st.error("Usuario o PIN incorrectos.")
    with tab_crear:
        usuario_n = st.text_input("Elige un usuario", key="reg_usuario")
        pin_n = st.text_input("Elige un PIN (4+ dígitos)", type="password", key="reg_pin")
        if st.button("Crear cuenta", use_container_width=True):
            if not usuario_n or len(pin_n) < 4:
                st.error("Ingresa un usuario y un PIN de al menos 4 dígitos.")
            else:
                ok, msg = db.registrar_usuario(usuario_n.strip(), pin_n)
                (st.success if ok else st.error)(msg)


# ------------------------------------------------------------------ mapa ---

def vista_mapa(niveles, progreso):
    lecciones = todas_las_lecciones(niveles)
    completadas = sum(1 for l in lecciones if progreso.get(l["id"], {}).get("completada"))
    total = len(lecciones)

    st.title("🛢️ DBA desde Cero")
    st.progress(completadas / total if total else 0.0,
                text=f"Progreso: {completadas} de {total} lecciones · "
                     f"{round(100 * completadas / total) if total else 0}%")

    desbloqueada_hasta = True  # la primera siempre está abierta
    for nivel in niveles:
        etiqueta_nivel = nivel.get("etiqueta", f"Nivel {nivel['nivel']}")
        st.subheader(f"{nivel['emoji']} {etiqueta_nivel}: {nivel['titulo']}")
        st.caption(nivel["descripcion"])
        for lec in nivel["lecciones"]:
            hecha = progreso.get(lec["id"], {}).get("completada", False)
            if hecha:
                icono, habilitada = "✅", True
            elif desbloqueada_hasta:
                icono, habilitada = "▶️", True
                desbloqueada_hasta = False  # solo una pendiente abierta a la vez
            else:
                icono, habilitada = "🔒", False
            etiqueta = f"{icono}  {lec['id']} — {lec['titulo']}"
            if st.button(etiqueta, key=f"abrir_{lec['id']}",
                         use_container_width=True, disabled=not habilitada):
                st.session_state.leccion_actual = lec["id"]
                st.session_state.pagina = 0
                st.session_state.pop("quiz_enviado", None)
                st.rerun()
        st.divider()

    if completadas == total and total > 0:
        st.balloons()
        st.success("¡Completaste todo el contenido disponible! Pronto habrá más módulos.")


# --------------------------------------------------------------- lección ---

def vista_leccion(niveles, progreso, usuario):
    lecciones = todas_las_lecciones(niveles)
    lec = next(l for l in lecciones if l["id"] == st.session_state.leccion_actual)
    paginas = lec["paginas"]
    n_pag = len(paginas)
    quiz = lec.get("quiz", [])
    pagina = st.session_state.get("pagina", 0)

    col_a, col_b = st.columns([1, 5])
    with col_a:
        if st.button("⬅️ Mapa"):
            st.session_state.pop("leccion_actual")
            st.rerun()
    with col_b:
        st.markdown(f"### {lec['id']} — {lec['titulo']}")

    # --- páginas de contenido ---
    if pagina < n_pag:
        pag = paginas[pagina]
        st.progress((pagina + 1) / (n_pag + (1 if quiz else 0)),
                    text=f"Página {pagina + 1} de {n_pag}" + (" + quiz" if quiz else ""))
        if pag.get("titulo"):
            st.markdown(f"#### {pag['titulo']}")
        st.markdown(pag["contenido"])

        # mini-terminal de práctica dentro de la página
        if "practica" in pag:
            pr = pag["practica"]
            st.markdown("---")
            st.markdown(f"🖥️ **Práctica**: {pr['instruccion']}")
            respuesta = st.text_input("Escribe aquí, como en una terminal:",
                                      key=f"prac_{lec['id']}_{pagina}")
            if respuesta:
                if normalizar(respuesta) in [normalizar(r) for r in pr["respuestas"]]:
                    st.success(pr.get("ok", "¡Correcto! Así se hace."))
                else:
                    st.warning(f"Aún no. Pista: {pr['pista']}")

        izq, der = st.columns(2)
        with izq:
            if pagina > 0 and st.button("← Anterior", use_container_width=True):
                st.session_state.pagina -= 1
                st.rerun()
        with der:
            etiqueta = "Siguiente →" if pagina < n_pag - 1 else ("Ir al quiz 🎯" if quiz else "Terminar ✅")
            if st.button(etiqueta, type="primary", use_container_width=True):
                st.session_state.pagina += 1
                st.rerun()
        return

    # --- quiz (o cierre sin quiz) ---
    if not quiz:
        db.guardar_progreso(usuario, lec["id"], 0, 0, True)
        st.success("¡Lección completada!")
        if st.button("Volver al mapa", type="primary"):
            st.session_state.pop("leccion_actual")
            st.rerun()
        return

    st.progress(1.0, text="Quiz final de la lección")
    st.markdown("#### 🎯 Quiz: demuestra lo aprendido")
    respuestas = []
    for i, q in enumerate(quiz):
        eleccion = st.radio(f"**{i + 1}. {q['pregunta']}**", q["opciones"],
                            index=None, key=f"quiz_{lec['id']}_{i}")
        respuestas.append(eleccion)

    if st.button("Enviar respuestas", type="primary", use_container_width=True):
        st.session_state.quiz_enviado = True

    if st.session_state.get("quiz_enviado"):
        if any(r is None for r in respuestas):
            st.warning("Responde todas las preguntas antes de enviar.")
            st.session_state.quiz_enviado = False
            return
        correctas = 0
        for i, q in enumerate(quiz):
            es_correcta = respuestas[i] == q["opciones"][q["correcta"]]
            correctas += es_correcta
            icono = "✅" if es_correcta else "❌"
            st.markdown(f"{icono} **Pregunta {i + 1}:** {q['explicacion']}")
        aprobada = correctas / len(quiz) >= APROBACION
        db.guardar_progreso(usuario, lec["id"], correctas, len(quiz), aprobada)
        idx = next(i for i, l in enumerate(lecciones) if l["id"] == lec["id"])
        siguiente = lecciones[idx + 1] if idx + 1 < len(lecciones) else None
        if aprobada:
            st.success(f"¡Aprobado! {correctas} de {len(quiz)} correctas. 🎉")
            col1, col2 = st.columns([3, 1])
            with col1:
                if siguiente and st.button(
                        f"Siguiente: {siguiente['id']} — {siguiente['titulo']} →",
                        type="primary", use_container_width=True):
                    st.session_state.leccion_actual = siguiente["id"]
                    st.session_state.pagina = 0
                    st.session_state.pop("quiz_enviado", None)
                    st.rerun()
                if not siguiente:
                    st.balloons()
                    st.info("¡Completaste todo el contenido disponible! Pronto habrá más módulos.")
            with col2:
                if st.button("Mapa", use_container_width=True):
                    st.session_state.pop("leccion_actual")
                    st.session_state.pop("quiz_enviado", None)
                    st.rerun()
        else:
            st.error(f"{correctas} de {len(quiz)}. Necesitas el 70%. "
                     "Repasar no es perder tiempo: es la única forma de no perderlo.")
            col1, col2 = st.columns([3, 1])
            with col1:
                if st.button("📖 Repasar la lección y reintentar", type="primary",
                             use_container_width=True):
                    for i in range(len(quiz)):
                        st.session_state.pop(f"quiz_{lec['id']}_{i}", None)
                    st.session_state.pagina = 0
                    st.session_state.pop("quiz_enviado", None)
                    st.rerun()
            with col2:
                if st.button("Mapa", use_container_width=True):
                    st.session_state.pop("leccion_actual")
                    st.session_state.pop("quiz_enviado", None)
                    st.rerun()


# ------------------------------------------------------------------ main ---

def main():
    if "usuario" not in st.session_state:
        vista_login()
        return
    niveles = cargar_niveles()
    progreso = db.cargar_progreso(st.session_state.usuario)
    with st.sidebar:
        st.markdown(f"👤 **{st.session_state.usuario}**")
        if st.button("Cerrar sesión"):
            st.session_state.clear()
            st.rerun()
        st.markdown("---")
        st.caption("DBA desde Cero · v1\nContenido: Parte 0 (más módulos en camino)")
    if "leccion_actual" in st.session_state:
        vista_leccion(niveles, progreso, st.session_state.usuario)
    else:
        vista_mapa(niveles, progreso)


main()
