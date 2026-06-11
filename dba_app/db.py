"""Capa de datos: Supabase si hay credenciales, modo invitado (memoria) si no.

Así puedes probar la app localmente sin configurar nada, y al desplegar en
Streamlit Cloud solo agregas los secrets y el progreso se vuelve persistente.
"""
import hashlib
import streamlit as st

try:
    from supabase import create_client
except ImportError:  # permite correr sin la librería en modo invitado
    create_client = None


def _hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


@st.cache_resource
def get_client():
    """Devuelve el cliente de Supabase o None (modo invitado)."""
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
    except Exception:
        return None
    if create_client is None:
        return None
    try:
        return create_client(url, key)
    except Exception:
        return None


# ---------------------------------------------------------------- usuarios --

def registrar_usuario(usuario: str, pin: str) -> tuple[bool, str]:
    sb = get_client()
    if sb is None:
        return True, "Modo invitado: tu progreso vive solo en esta sesión."
    existe = sb.table("usuarios").select("usuario").eq("usuario", usuario).execute()
    if existe.data:
        return False, "Ese nombre de usuario ya existe."
    sb.table("usuarios").insert({"usuario": usuario, "pin_hash": _hash_pin(pin)}).execute()
    return True, "¡Cuenta creada! Ya puedes entrar."


def validar_usuario(usuario: str, pin: str) -> bool:
    sb = get_client()
    if sb is None:
        return True  # modo invitado: cualquier login entra
    res = (
        sb.table("usuarios")
        .select("pin_hash")
        .eq("usuario", usuario)
        .execute()
    )
    return bool(res.data) and res.data[0]["pin_hash"] == _hash_pin(pin)


# ---------------------------------------------------------------- progreso --

def cargar_progreso(usuario: str) -> dict:
    """Devuelve {leccion_id: {"puntaje": x, "total": y, "completada": bool}}."""
    sb = get_client()
    if sb is None:
        return st.session_state.get("_progreso_invitado", {})
    res = sb.table("progreso").select("*").eq("usuario", usuario).execute()
    return {
        r["leccion_id"]: {
            "puntaje": r["puntaje"],
            "total": r["total"],
            "completada": r["completada"],
        }
        for r in (res.data or [])
    }


def guardar_progreso(usuario: str, leccion_id: str, puntaje: int, total: int, completada: bool):
    sb = get_client()
    registro = {"puntaje": puntaje, "total": total, "completada": completada}
    if sb is None:
        prog = st.session_state.setdefault("_progreso_invitado", {})
        previo = prog.get(leccion_id, {})
        # nunca "des-completar" ni bajar el mejor puntaje
        registro["completada"] = completada or previo.get("completada", False)
        registro["puntaje"] = max(puntaje, previo.get("puntaje", 0))
        prog[leccion_id] = registro
        return
    sb.table("progreso").upsert(
        {
            "usuario": usuario,
            "leccion_id": leccion_id,
            "puntaje": puntaje,
            "total": total,
            "completada": completada,
        },
        on_conflict="usuario,leccion_id",
    ).execute()
