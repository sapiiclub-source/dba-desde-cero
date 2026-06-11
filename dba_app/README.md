# 🛢️ DBA desde Cero — App del curso

Curso interactivo para llegar de cero absoluto a DBA experto. Lecciones cortas,
prácticas de terminal simulada y quizzes que desbloquean el avance.

## Estructura
```
app.py               → la aplicación Streamlit
db.py                → capa de datos (Supabase o modo invitado)
contenido/*.json     → las lecciones (¡el contenido vive aquí, no en el código!)
generar_nivel0.py    → script con el que se generó el nivel 0 (referencia)
supabase_schema.sql  → tablas a crear en Supabase
requirements.txt     → dependencias
```

## Probarla en tu PC (5 minutos)
```bash
pip install -r requirements.txt
streamlit run app.py
```
Sin configurar nada funciona en **modo invitado** (el progreso no persiste).

## Desplegarla para el mundo (igual que el Sapi Club)
1. **Supabase**: crea un proyecto nuevo → SQL Editor → pega y ejecuta
   `supabase_schema.sql`.
2. **GitHub**: sube esta carpeta a un repositorio.
3. **Streamlit Cloud** (share.streamlit.io): New app → apunta al repo →
   en *Settings → Secrets* agrega:
   ```toml
   SUPABASE_URL = "https://TU-PROYECTO.supabase.co"
   SUPABASE_KEY = "TU-SERVICE-ROLE-KEY"
   ```
4. Comparte la URL. Cada persona crea su usuario+PIN y su progreso queda guardado.

## Agregar más módulos (lo haremos juntos, paso a paso)
Cada nivel es un archivo `contenido/nivelN.json` con este esquema:
```json
{
 "nivel": 1, "emoji": "🧱", "titulo": "...", "descripcion": "...",
 "lecciones": [
   {"id": "1.1", "titulo": "...",
    "paginas": [
      {"titulo": "...", "contenido": "markdown...",
       "practica": {"instruccion": "...", "respuestas": ["select sysdate from dual"],
                    "pista": "...", "ok": "..."}}
    ],
    "quiz": [
      {"pregunta": "...", "opciones": ["a","b","c"], "correcta": 0, "explicacion": "..."}
    ]}
 ]
}
```
La app los detecta automáticamente (lee todos los `nivel*.json` en orden).
La clave `practica` es opcional por página: valida lo que el alumno escribe
(ignora mayúsculas, espacios extra y el `;` final).

## Hoja de ruta
- v1 (esta): Parte 0 completa, login simple, progreso, quizzes, terminal simulada.
- v2: Módulo 0 y Nivel 1 (SQL) con más prácticas de comandos; rachas y logros.
- v3: simulador SQL real (sandbox), certificado de avance, modo oscuro.
