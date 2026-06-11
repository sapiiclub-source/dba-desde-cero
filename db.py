"""Capa de datos: Supabase si hay credenciales, modo invitado (memoria) si no."""
import hashlib
import streamlit as st

try:
    from supabase import create_client
except ImportError:
    create_client = None


def _hash_pin(pin: str) -> str:
    return hashlib.sha256(pin.encode("utf-8")).hexdigest()


def get_client():
    """Devuelve el cliente de Supabase o None (modo invitado).
    Sin cache_resource para que siempre lea los secrets frescos.
    """
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
        if not url or not key:
            return None
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
    try:
        existe = sb.table("usuarios").select("usuario").eq("usuario", usuario).execute()
        if existe.data:
            return False, "Ese nombre de usuario ya existe."
        sb.table("usuarios").insert({"usuario": usuario, "pin_hash": _hash_pin(pin)}).execute()
        return True, "¡Cuenta creada! Ya puedes entrar."
    except Exception as e:
        return False, f"Error al crear cuenta: {e}"


def validar_usuario(usuario: str, pin: str) -> bool:
    sb = get_client()
    if sb is None:
        return True
    try:
        res = (
            sb.table("usuarios")
            .select("pin_hash")
            .eq("usuario", usuario)
            .execute()
        )
        return bool(res.data) and res.data[0]["pin_hash"] == _hash_pin(pin)
    except Exception:
        return False


# ---------------------------------------------------------------- progreso --

def cargar_progreso(usuario: str) -> dict:
    sb = get_client()
    if sb is None:
        return st.session_state.get("_progreso_invitado", {})
    try:
        res = sb.table("progreso").select("*").eq("usuario", usuario).execute()
        return {
            r["leccion_id"]: {
                "puntaje": r["puntaje"],
                "total": r["total"],
                "completada": r["completada"],
            }
            for r in (res.data or [])
        }
    except Exception:
        return {}


def guardar_progreso(usuario: str, leccion_id: str, puntaje: int, total: int, completada: bool):
    sb = get_client()
    if sb is None:
        prog = st.session_state.setdefault("_progreso_invitado", {})
        previo = prog.get(leccion_id, {})
        prog[leccion_id] = {
            "puntaje": max(puntaje, previo.get("puntaje", 0)),
            "total": total,
            "completada": completada or previo.get("completada", False),
        }
        return
    try:
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
    except Exception:
        pass
