# Guía de despliegue paso a paso — App "DBA desde Cero"
### Tres plataformas, en este orden: GitHub → Supabase → Streamlit Cloud
*(Mismo flujo que tu app del Sapi Club: si algo te suena familiar, es porque lo es.)*

---

## ANTES DE PARTIR — Probar en tu PC (opcional pero recomendado, 5 min)

1. Descomprime `dba_app_v2.zip` en una carpeta, por ejemplo `C:\proyectos\dba_app`.
2. Abre una terminal (CMD o PowerShell) en esa carpeta y ejecuta:
   ```
   pip install -r requirements.txt
   streamlit run app.py
   ```
3. Se abre el navegador en `http://localhost:8501`. Sin configurar nada, la app corre en **modo invitado** (lo dice un aviso azul): todo funciona, pero el progreso se pierde al cerrar. Perfecto para revisar contenido y dinámica antes de publicar.

---

## PASO 1 — GITHUB (donde vive el código)

> Streamlit Cloud despliega leyendo un repositorio de GitHub. Probablemente ya tienes cuenta por el Sapi Club; si es así, salta al 1.2.

### 1.1 Crear cuenta (si no tienes)
1. Entra a `github.com` → **Sign up** → correo, contraseña, nombre de usuario → verifica el correo.

### 1.2 Crear el repositorio
1. Arriba a la derecha: **+** → **New repository**.
2. Repository name: `dba-desde-cero` (sin espacios).
3. Visibilidad: **Private** funciona perfecto con Streamlit Cloud (no necesitas hacerlo público).
4. NO marques "Add a README" (subiremos el nuestro).
5. **Create repository**.

### 1.3 Subir los archivos (vía web, sin instalar Git)
1. En la página del repo recién creado: link **"uploading an existing file"**.
2. Arrastra TODO el contenido de la carpeta `dba_app`: `app.py`, `db.py`, `requirements.txt`, `README.md`, `supabase_schema.sql`, los `generar_*.py`.
3. ⚠️ **Detalle importante**: la carpeta `contenido/` con sus JSON debe quedar como carpeta. La subida web a veces aplana carpetas; verifica que al final exista `contenido/nivel0.json` y `contenido/nivel1.json` DENTRO de una carpeta `contenido`. Si la web no te deja crear la carpeta: entra al repo → **Add file → Create new file** → en el nombre escribe `contenido/nivel0.json` (el `/` crea la carpeta) → pega el contenido del JSON → Commit. Repite para `nivel1.json`.
4. Botón verde **Commit changes**.
5. Verificación final: el repo debe verse así:
   ```
   app.py
   db.py
   requirements.txt
   README.md
   supabase_schema.sql
   contenido/nivel0.json
   contenido/nivel1.json
   ```

*(Alternativa si usas Git por consola: `git clone`, copiar archivos, `git add .`, `git commit -m "v1"`, `git push`.)*

---

## PASO 2 — SUPABASE (donde viven usuarios y progreso)

### 2.1 Crear el proyecto
1. Entra a `supabase.com` → inicia sesión (puedes entrar con tu cuenta de GitHub).
2. **New project** → elige tu organización.
3. Name: `dba-desde-cero` · Database Password: genera una y **guárdala** (no la usaremos en la app, pero Supabase la pide) · Region: **South America (São Paulo)** (la más cercana a Chile).
4. **Create new project** y espera ~2 minutos a que aprovisione.

### 2.2 Crear las tablas
1. Menú izquierdo → **SQL Editor** → **New query**.
2. Pega COMPLETO el contenido del archivo `supabase_schema.sql` → botón **Run**.
3. Debe decir "Success". Verifica en **Table Editor** (menú izquierdo): deben existir las tablas `usuarios` y `progreso`.

### 2.3 Obtener las dos credenciales
1. Menú izquierdo → **Project Settings** (el engranaje) → **API**.
2. Copia y guarda en un bloc de notas:
   - **Project URL** → algo como `https://abcdefgh.supabase.co`
   - **service_role key** (sección "Project API keys", la marcada como `service_role`, secreta) → un texto larguísimo que empieza con `eyJ...`
3. ⚠️ La `service_role` da acceso total: **solo** va en los Secrets de Streamlit (paso 3.4). Jamás la pegues en el código ni en GitHub.

---

## PASO 3 — STREAMLIT CLOUD (donde la app cobra vida con URL pública)

### 3.1 Cuenta
1. Entra a `share.streamlit.io` → **Sign in with GitHub** → autoriza el acceso.

### 3.2 Crear la app
1. **New app** (o "Create app").
2. Repository: selecciona `tu-usuario/dba-desde-cero`.
3. Branch: `main`.
4. Main file path: `app.py`.
5. App URL: elige el subdominio, por ejemplo `dba-desde-cero` → quedará `https://dba-desde-cero.streamlit.app`.

### 3.3 Primer despliegue
1. **Deploy**. Verás el log de instalación (~2-3 min). 
2. Cuando cargue, la app funcionará... en **modo invitado** (aún no le dimos las credenciales de Supabase). Vamos a eso.

### 3.4 Configurar los Secrets (la conexión con Supabase)
1. En `share.streamlit.io`, en tu app → menú **⋮** → **Settings** → pestaña **Secrets**.
2. Pega exactamente esto, reemplazando con TUS valores del paso 2.3:
   ```toml
   SUPABASE_URL = "https://abcdefgh.supabase.co"
   SUPABASE_KEY = "eyJ...tu-service-role-key-completa..."
   ```
   (Comillas incluidas; una variable por línea.)
3. **Save** → la app se reinicia sola en unos segundos.

### 3.5 Verificación final (checklist)
1. Abre tu URL `https://....streamlit.app`: el aviso azul de "modo invitado" **ya no debe aparecer**.
2. Crea una cuenta de prueba (usuario + PIN) → debe decir "¡Cuenta creada!".
3. En Supabase → Table Editor → tabla `usuarios`: debe aparecer tu usuario de prueba. ✅
4. Completa la lección 0.1 con su quiz → en la tabla `progreso` debe aparecer la fila. ✅
5. Cierra el navegador, vuelve a entrar con el mismo usuario: el progreso debe seguir ahí. ✅
6. Ábrela desde tu celular y compártele el link a alguien más para que cree SU cuenta. 🎉

---

## MANTENCIÓN Y PROBLEMAS FRECUENTES

**¿Cómo agrego los próximos módulos?**
Subes el nuevo `contenido/nivelN.json` al repo de GitHub (Add file → Upload). Streamlit Cloud redespliega solo en ~1 minuto. El código no se toca.

**La app dice "modo invitado" aunque configuré los Secrets** → revisa que las claves se llamen EXACTAMENTE `SUPABASE_URL` y `SUPABASE_KEY`, con comillas, y que usaste la **service_role** key (no la `anon`). Luego ⋮ → Reboot app.

**Error al crear cuenta / guardar progreso** → en Supabase, Table Editor: ¿existen `usuarios` y `progreso`? Si no, repite el paso 2.2.

**La app "se durmió"** → en el plan gratuito, Streamlit suspende apps sin visitas por unos días; el primer visitante la despierta en ~1 min con un botón. Normal.

**Cambié código y no se refleja** → cada commit a `main` redespliega solo; si no, ⋮ → Reboot app. Para errores, mira ⋮ → Manage app → logs.

**¿Cuántas personas soporta gratis?** → Streamlit Cloud gratuito soporta cómodamente decenas de usuarios simultáneos de una app liviana como esta, y Supabase gratis incluye 500 MB de base de datos (el progreso ocupa bytes por persona: te alcanza para miles de estudiantes).

**Seguridad** → los PIN se guardan como hash SHA-256 (nunca en claro). Aun así, dile a tus usuarios que no usen contraseñas importantes como PIN: es una app educativa, no un banco.
