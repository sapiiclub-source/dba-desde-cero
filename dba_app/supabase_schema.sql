-- Esquema para la app "DBA desde Cero" (ejecutar en el SQL Editor de Supabase)

create table if not exists usuarios (
  id          bigint generated always as identity primary key,
  usuario     text unique not null,
  pin_hash    text not null,            -- hash SHA-256 del PIN
  creado_en   timestamptz default now()
);

create table if not exists progreso (
  id          bigint generated always as identity primary key,
  usuario     text not null references usuarios(usuario) on delete cascade,
  leccion_id  text not null,            -- ej: '0.1'
  puntaje     int  not null default 0,  -- preguntas correctas del quiz
  total       int  not null default 0,  -- total de preguntas
  completada  boolean not null default false,
  fecha       timestamptz default now(),
  unique (usuario, leccion_id)
);

-- Para la versión 1 la app usa la service_role key desde el servidor (st.secrets),
-- por lo que RLS puede quedar desactivado igual que en tu app del Sapi Club.
