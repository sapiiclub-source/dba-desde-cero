# -*- coding: utf-8 -*-
"""Genera contenido/nivel2.json: Nivel 1 — SQL, el idioma de las bases de datos."""
import json

L = []

L.append({
 "id": "1.1", "titulo": "Tablas, filas, columnas y tipos de datos",
 "paginas": [
  {"titulo": "La planilla con reglas", "contenido":
   "Una **tabla** es como una planilla, pero con reglas estrictas:\n\n"
   "- Cada **columna** tiene nombre y un **tipo de dato** fijo.\n"
   "- Cada **fila** es un registro: un cliente, un producto, una venta.\n\n"
   "Los 3 tipos de datos que cubren el 90% de la vida:\n\n"
   "| Tipo | Guarda | Ejemplo |\n|---|---|---|\n"
   "| `NUMBER` | números | 34, 1990.50 |\n"
   "| `VARCHAR2(n)` | texto de hasta n caracteres | 'Camila' |\n"
   "| `DATE` | fecha y hora | 15/03/2026 14:30 |\n\n"
   "💡 Si la columna es NUMBER, es **imposible** guardar \"hola\" ahí. La base te protege de la basura — "
   "una de las 5 ventajas sobre Excel que viste en la lección 0.7."},
  {"titulo": "Pensar en tablas", "contenido":
   "Antes de escribir nada, el diseño: ¿qué tablas necesita un almacén de barrio?\n\n"
   "- `CLIENTES` (id, nombre, telefono)\n- `PRODUCTOS` (id, nombre, precio, stock)\n- `VENTAS` (id, fecha, cliente_id)\n\n"
   "Fíjate en `cliente_id` dentro de VENTAS: en vez de repetir el nombre del cliente en cada venta, guardamos su **id** "
   "y \"apuntamos\" a la tabla CLIENTES. Cada dato vive en UN solo lugar. Esa idea —que formalizaremos en la lección 1.7— "
   "es el corazón del modelo **relacional**."}
 ],
 "quiz": [
  {"pregunta": "¿Qué tipo de dato usarías para guardar el nombre de un cliente?",
   "opciones": ["NUMBER", "VARCHAR2", "DATE"],
   "correcta": 1,
   "explicacion": "VARCHAR2(n) guarda texto de largo variable hasta n caracteres."},
  {"pregunta": "¿Qué pasa si intentas guardar 'hola' en una columna NUMBER?",
   "opciones": ["Se guarda igual", "La base de datos lo rechaza con un error", "Se convierte en 0"],
   "correcta": 1,
   "explicacion": "Los tipos de datos son un contrato: la base rechaza lo que no calza. Protección automática contra datos basura."},
  {"pregunta": "¿Por qué VENTAS guarda cliente_id en vez del nombre del cliente?",
   "opciones": ["Para ahorrar tinta", "Para que cada dato viva en un solo lugar y se relacione por id", "Porque los nombres están prohibidos"],
   "correcta": 1,
   "explicacion": "Si el cliente cambia de nombre, se corrige en UN lugar. Relacionar por id es la esencia del modelo relacional."}
 ]
})

L.append({
 "id": "1.2", "titulo": "DDL: crear y modificar estructuras",
 "paginas": [
  {"titulo": "Tu primera palabra técnica oficial: DDL", "contenido":
   "Los comandos SQL se clasifican en familias. La primera: **DDL** (*Data Definition Language*, lenguaje de "
   "definición de datos) — los comandos que crean y modifican **estructuras** (las tablas mismas, no su contenido).\n\n"
   "Analogía: el DDL es la **construcción de la estantería**; los datos que pondrás en ella vienen después.\n\n"
   "Los tres grandes del DDL:\n- `CREATE` → construir (una tabla, un índice, un usuario...)\n"
   "- `ALTER` → modificar la estructura (agregar una columna, por ejemplo)\n"
   "- `DROP` → demoler ⚠️ (la tabla Y todos sus datos)"},
  {"titulo": "CREATE TABLE, línea por línea", "contenido":
   "```sql\nCREATE TABLE clientes (\n  id      NUMBER        NOT NULL,\n  nombre  VARCHAR2(100),\n  ciudad  VARCHAR2(50),\n  edad    NUMBER\n);\n```\n\n"
   "- `CREATE TABLE clientes` → \"construye una tabla llamada clientes\".\n"
   "- Entre paréntesis, cada columna: nombre + tipo.\n"
   "- `NOT NULL` → esta columna es **obligatoria**: no se puede dejar vacía.\n"
   "- El `;` final cierra la orden.\n\n"
   "Y para modificar después:\n```sql\nALTER TABLE clientes ADD (correo VARCHAR2(120));\n```",
   "practica": {"instruccion": "Crea una tabla llamada `mascotas` con una sola columna: `nombre` de tipo texto de hasta 50 caracteres.",
                "respuestas": ["create table mascotas (nombre varchar2(50))", "create table mascotas(nombre varchar2(50))"],
                "pista": "CREATE TABLE nombre (columna TIPO(tamaño));",
                "ok": "¡Tu primer DDL! Acabas de construir una estructura en la base de datos."}},
  {"titulo": "DROP: el comando que se escribe despacio", "contenido":
   "```sql\nDROP TABLE clientes;\n```\n\n"
   "Demuele la tabla **con todos sus datos adentro**. En Oracle existe una \"papelera\" (recyclebin) que a veces salva, "
   "pero la regla profesional es tratarlo como irreversible.\n\n"
   "🧠 Detalle técnico que te hará ver senior desde ya: **los comandos DDL confirman automáticamente** todo lo pendiente "
   "(en jerga: hacen *commit implícito*). Entenderás el peso completo de esta frase en el Módulo 4; por ahora grábate que "
   "el DDL es definitivo al instante: no hay \"deshacer\"."}
 ],
 "quiz": [
  {"pregunta": "¿Qué es el DDL?",
   "opciones": ["Los comandos que consultan datos", "Los comandos que definen/modifican estructuras (CREATE, ALTER, DROP)", "Un tipo de dato"],
   "correcta": 1,
   "explicacion": "Data Definition Language: construye la estantería. Los datos vienen después (eso será el DML)."},
  {"pregunta": "Necesitas agregar la columna `telefono` a una tabla que ya existe. ¿Qué comando usas?",
   "opciones": ["CREATE", "ALTER TABLE ... ADD", "DROP"],
   "correcta": 1,
   "explicacion": "ALTER modifica estructuras existentes sin perder los datos que ya contienen."},
  {"pregunta": "¿Qué hace DROP TABLE?",
   "opciones": ["Vacía la tabla pero la deja existiendo", "Elimina la tabla Y todos sus datos", "Renombra la tabla"],
   "correcta": 1,
   "explicacion": "DROP demuele estructura y contenido. Se escribe despacio y se lee dos veces."}
 ]
})

L.append({
 "id": "1.3", "titulo": "DML: insertar, modificar y borrar datos",
 "paginas": [
  {"titulo": "La segunda familia: DML", "contenido":
   "**DML** (*Data Manipulation Language*, lenguaje de manipulación de datos): los comandos que trabajan con el "
   "**contenido** de las tablas. Si el DDL construía la estantería, el DML pone, cambia y saca los libros.\n\n"
   "```sql\nINSERT INTO clientes (id, nombre, ciudad, edad)\nVALUES (1, 'Camila', 'Rancagua', 34);\n```\n"
   "= \"inserta en clientes una fila con estos valores\". El orden de los VALUES corresponde al orden de las columnas listadas.",
   "practica": {"instruccion": "Inserta en la tabla `mascotas` (columna nombre) una fila con el valor 'Sapi'. Usa: INSERT INTO tabla (columna) VALUES ('valor');",
                "respuestas": ["insert into mascotas (nombre) values ('sapi')", "insert into mascotas(nombre) values('sapi')", "insert into mascotas (nombre) values('sapi')", "insert into mascotas(nombre) values ('sapi')"],
                "pista": "INSERT INTO mascotas (nombre) VALUES ('Sapi');  — el texto va entre comillas simples.",
                "ok": "¡Primera fila insertada! Nota las comillas simples para el texto."}},
  {"titulo": "UPDATE y DELETE… y la cláusula que salva carreras", "contenido":
   "```sql\nUPDATE clientes SET edad = 35 WHERE id = 1;\nDELETE FROM clientes WHERE id = 1;\n```\n\n"
   "El **WHERE** dice *a cuáles filas* aplicar el cambio.\n\n"
   "⚠️ **La lección que todo el mundo aprende llorando**: un UPDATE o DELETE **sin WHERE** afecta TODAS las filas de la tabla. "
   "`DELETE FROM clientes;` borra todos los clientes. Todos.\n\n"
   "Ritual profesional antes de cualquier UPDATE/DELETE importante:\n"
   "1. Escribe primero un `SELECT` con el mismo WHERE para VER qué filas tocarás.\n"
   "2. Cuenta cuántas son. ¿Coincide con lo esperado?\n"
   "3. Recién entonces, ejecuta el UPDATE/DELETE."},
  {"titulo": "El adelanto: nada es definitivo… todavía", "contenido":
   "Sorpresa importante: en Oracle, los cambios DML **no son definitivos de inmediato**. Quedan \"en borrador\", "
   "visibles solo para ti, hasta que digas:\n\n"
   "- `COMMIT;` → \"confirmo, que sea definitivo\".\n- `ROLLBACK;` → \"me arrepiento, deshaz todo\".\n\n"
   "(Estos dos forman su propia mini-familia: **TCL**, *Transaction Control Language*.)\n\n"
   "O sea: si borraste de más y AÚN no hiciste commit, `ROLLBACK;` te salva. 🙏 El mecanismo completo —y por qué es "
   "una de las ideas más bellas de la informática— es el tema estelar del Módulo 4. Por ahora: DML = borrador hasta el COMMIT; "
   "DDL = definitivo al instante (lección 1.2)."}
 ],
 "quiz": [
  {"pregunta": "¿Qué es el DML?",
   "opciones": ["Los comandos que trabajan con el contenido: INSERT, UPDATE, DELETE", "Los comandos que crean tablas", "Un tipo de servidor"],
   "correcta": 0,
   "explicacion": "Data Manipulation Language: pone, cambia y saca los datos de las estructuras que el DDL construyó."},
  {"pregunta": "¿Qué hace `DELETE FROM clientes;` (sin WHERE)?",
   "opciones": ["Borra una fila al azar", "Borra TODAS las filas de la tabla", "Da error siempre"],
   "correcta": 1,
   "explicacion": "Sin WHERE, el DML aplica a todas las filas. El ritual: SELECT primero con el mismo WHERE, contar, y recién ejecutar."},
  {"pregunta": "Borraste filas de más con DELETE y aún NO has hecho COMMIT. ¿Qué te salva?",
   "opciones": ["Nada, está perdido", "ROLLBACK;", "Apagar el computador rápido"],
   "correcta": 1,
   "explicacion": "El DML queda en borrador hasta el COMMIT. ROLLBACK deshace lo no confirmado. (El Módulo 4 te mostrará la magia detrás.)"}
 ]
})

L.append({
 "id": "1.4", "titulo": "El mapa completo: DDL, DML, DQL, DCL y TCL",
 "paginas": [
  {"titulo": "Las 5 familias del SQL", "contenido":
   "Ya conoces dos; aquí está el mapa completo (pregunta de entrevista clásica):\n\n"
   "| Familia | Significado | Comandos | En una frase |\n|---|---|---|---|\n"
   "| **DDL** | Definition | CREATE, ALTER, DROP, TRUNCATE | Construye/modifica estructuras |\n"
   "| **DML** | Manipulation | INSERT, UPDATE, DELETE, MERGE | Trabaja el contenido |\n"
   "| **DQL** | Query | SELECT | Consulta (algunos lo cuentan dentro del DML) |\n"
   "| **DCL** | Control | GRANT, REVOKE | Da y quita permisos |\n"
   "| **TCL** | Transaction | COMMIT, ROLLBACK, SAVEPOINT | Confirma o deshace |\n"},
  {"titulo": "El par traicionero: TRUNCATE vs DELETE", "contenido":
   "Ambos \"vacían\" una tabla, pero son de familias distintas y eso lo cambia todo:\n\n"
   "- `DELETE FROM tabla;` es **DML**: borra fila por fila, queda en borrador, **ROLLBACK te salva**.\n"
   "- `TRUNCATE TABLE tabla;` es **DDL**: vacía la tabla de un golpe, instantáneo incluso con millones de filas… "
   "y como todo DDL, **es definitivo al instante: no hay rollback**.\n\n"
   "🎤 Pregunta de entrevista garantizada: \"¿diferencia entre DELETE y TRUNCATE?\". Ahora puedes responderla "
   "con el *porqué* (la familia a la que pertenece cada uno), no de memoria."}
 ],
 "quiz": [
  {"pregunta": "GRANT y REVOKE (dar y quitar permisos) pertenecen a...",
   "opciones": ["DDL", "DCL", "DML"],
   "correcta": 1,
   "explicacion": "Data Control Language: el control de quién puede hacer qué. Lo usarás mucho como DBA."},
  {"pregunta": "¿Por qué TRUNCATE no se puede deshacer con ROLLBACK?",
   "opciones": ["Porque es muy rápido", "Porque es DDL, y el DDL es definitivo al instante", "Sí se puede deshacer"],
   "correcta": 1,
   "explicacion": "TRUNCATE es DDL (define el estado de la estructura). DELETE es DML (borrador hasta COMMIT)."},
  {"pregunta": "COMMIT y ROLLBACK pertenecen a...",
   "opciones": ["TCL (control de transacciones)", "DQL", "DDL"],
   "correcta": 0,
   "explicacion": "Transaction Control Language: confirmar o deshacer el borrador del DML."}
 ]
})

L.append({
 "id": "1.5", "titulo": "SELECT a fondo: preguntar bien",
 "paginas": [
  {"titulo": "La anatomía del SELECT", "contenido":
   "```sql\nSELECT nombre, edad\nFROM   clientes\nWHERE  ciudad = 'San Fernando'\nORDER  BY edad DESC;\n```\n\n"
   "- `SELECT` → qué columnas quiero (`*` = todas).\n- `FROM` → de qué tabla.\n"
   "- `WHERE` → con qué condición (filtra filas).\n- `ORDER BY` → ordenado por... (`DESC` = descendente, `ASC` = ascendente, el default).\n\n"
   "Se lee como una frase: \"selecciona nombre y edad, de clientes, donde la ciudad sea San Fernando, ordenado por edad de mayor a menor\".",
   "practica": {"instruccion": "Pide TODAS las columnas de la tabla productos.",
                "respuestas": ["select * from productos"], "pista": "El asterisco significa 'todas las columnas'.",
                "ok": "¡Eso! SELECT * FROM productos. El pan de cada día."}},
  {"titulo": "Operadores del WHERE", "contenido":
   "| Operador | Significa | Ejemplo |\n|---|---|---|\n"
   "| `=  <>  >  <  >=  <=` | igual, distinto, mayor... | `edad >= 18` |\n"
   "| `BETWEEN a AND b` | en el rango (incluyente) | `edad BETWEEN 18 AND 30` |\n"
   "| `IN (a, b, c)` | es alguno de la lista | `ciudad IN ('Rancagua','Talca')` |\n"
   "| `LIKE` | se parece a (% = lo que sea) | `nombre LIKE 'Ca%'` → empieza con Ca |\n"
   "| `AND / OR / NOT` | combinar condiciones | `edad > 18 AND ciudad = 'Talca'` |\n\n"
   "💡 En Oracle, los textos van entre **comillas simples** y las comparaciones de texto distinguen mayúsculas: "
   "'CAMILA' y 'Camila' NO son iguales.",
   "practica": {"instruccion": "De la tabla clientes, pide los nombres de quienes tienen edad mayor o igual a 18.",
                "respuestas": ["select nombre from clientes where edad >= 18"],
                "pista": "SELECT columna FROM tabla WHERE condición — con >=.",
                "ok": "¡Perfecto! Ya filtras como profesional."}},
  {"titulo": "Funciones que usarás a diario", "contenido":
   "```sql\nSELECT UPPER(nombre),            -- a MAYÚSCULAS\n       ROUND(precio * 1.19, 0),  -- con IVA, redondeado\n       SYSDATE,                  -- fecha/hora actual\n       NVL(telefono, 'sin fono') -- si es NULL, muestra esto otro\nFROM productos;\n```\n\n"
   "Hay cientos de funciones; estas cuatro (texto, número, fecha, manejo de vacíos) te resuelven la mitad de la vida. "
   "La cuarta, `NVL`, nos lleva directo al tema de la próxima lección: el escurridizo **NULL**."}
 ],
 "quiz": [
  {"pregunta": "¿Qué devuelve `WHERE nombre LIKE 'Ca%'`?",
   "opciones": ["Nombres que terminan en Ca", "Nombres que empiezan con Ca", "Nombres que contienen exactamente 'Ca%'"],
   "correcta": 1,
   "explicacion": "% comodín al final = \"empieza con Ca\". '%Ca' sería termina con; '%Ca%' contiene."},
  {"pregunta": "¿Qué hace ORDER BY edad DESC?",
   "opciones": ["Ordena de mayor a menor edad", "Borra la columna edad", "Ordena alfabéticamente"],
   "correcta": 0,
   "explicacion": "DESC = descendente. Sin indicar nada, el orden es ascendente (ASC)."},
  {"pregunta": "¿`ciudad IN ('Talca','Curicó')` equivale a...?",
   "opciones": ["ciudad = 'Talca' AND ciudad = 'Curicó'", "ciudad = 'Talca' OR ciudad = 'Curicó'", "ciudad LIKE 'Talca'"],
   "correcta": 1,
   "explicacion": "IN = \"es alguno de la lista\" = una cadena de OR. (Con AND sería imposible: nadie está en dos ciudades a la vez.)"}
 ]
})

L.append({
 "id": "1.6", "titulo": "NULL: el valor que no es un valor",
 "paginas": [
  {"titulo": "¿Qué es NULL?", "contenido":
   "**NULL** significa \"no hay valor\" o \"desconocido\". No es cero, no es texto vacío: es **ausencia**.\n\n"
   "El teléfono de un cliente que no lo dio: NULL. La fecha de término de un contrato vigente: NULL.\n\n"
   "Y aquí la rareza que causa errores hasta en programadores con años de experiencia:\n\n"
   "> `NULL = NULL` **no es verdadero.**\n\n"
   "¿Por qué? Lógica pura: dos cosas *desconocidas* no se pueden declarar iguales (¿son iguales el teléfono que no sé "
   "de Juan y el que no sé de María? No se sabe). A NULL se le pregunta distinto:\n\n"
   "```sql\nWHERE telefono IS NULL      -- los que NO tienen\nWHERE telefono IS NOT NULL  -- los que SÍ tienen\n```",
   "practica": {"instruccion": "Pide todas las columnas de clientes cuyo telefono NO tiene valor.",
                "respuestas": ["select * from clientes where telefono is null"],
                "pista": "A NULL no se le pregunta con =, sino con IS NULL.",
                "ok": "¡Exacto! IS NULL es la forma correcta de preguntar por ausencia."}},
  {"titulo": "Las trampas clásicas", "contenido":
   "1. `WHERE telefono = NULL` → no da error... pero **nunca devuelve filas**. Trampa silenciosa.\n"
   "2. `COUNT(*)` cuenta todas las filas; `COUNT(telefono)` cuenta solo las filas donde telefono NO es NULL. "
   "Por eso pueden dar números distintos (pregunta de entrevista del quiz de la lección 1.1 del curso PDF 😉).\n"
   "3. Cualquier cálculo con NULL da NULL: `100 + NULL = NULL`. Para eso existe `NVL(columna, valor_si_nulo)`.\n\n"
   "🧠 Regla mental: trata a NULL como \"no sé\". ¿No sé + 100? No sé. ¿No sé igual a no sé? No sé."}
 ],
 "quiz": [
  {"pregunta": "¿Qué devuelve `WHERE telefono = NULL`?",
   "opciones": ["Las filas sin teléfono", "Ninguna fila, jamás (trampa silenciosa)", "Un error de sintaxis"],
   "correcta": 1,
   "explicacion": "NULL no es comparable con =. La forma correcta: IS NULL."},
  {"pregunta": "Una tabla tiene 100 filas y 30 no tienen correo. ¿Qué da COUNT(correo)?",
   "opciones": ["100", "70", "30"],
   "correcta": 1,
   "explicacion": "COUNT(columna) ignora los NULL: cuenta las 70 filas que SÍ tienen correo. COUNT(*) daría 100."},
  {"pregunta": "¿Cuánto es 100 + NULL?",
   "opciones": ["100", "0", "NULL"],
   "correcta": 2,
   "explicacion": "\"100 más no-sé\" = no-sé. Para evitarlo: NVL(columna, 0)."}
 ]
})

L.append({
 "id": "1.7", "titulo": "Claves: las reglas que sostienen todo",
 "paginas": [
  {"titulo": "Clave primaria (PK)", "contenido":
   "La **clave primaria** (*primary key*, PK) es la columna que identifica cada fila **sin repetirse jamás** "
   "(como el RUT de una persona).\n\n"
   "```sql\nCREATE TABLE clientes (\n  id     NUMBER PRIMARY KEY,\n  nombre VARCHAR2(100) NOT NULL\n);\n```\n\n"
   "Con eso, la base **impide físicamente** insertar dos clientes con el mismo id (error ORA-00001: tu primera "
   "sigla de error con nombre propio). No es una sugerencia: es una muralla."},
  {"titulo": "Clave foránea (FK)", "contenido":
   "La **clave foránea** (*foreign key*, FK) es la columna que \"apunta\" a la PK de otra tabla:\n\n"
   "```sql\nCREATE TABLE ventas (\n  id         NUMBER PRIMARY KEY,\n  fecha      DATE NOT NULL,\n  cliente_id NUMBER REFERENCES clientes(id)\n);\n```\n\n"
   "`REFERENCES clientes(id)` = \"cliente_id debe existir en clientes\". Resultado: **es imposible registrar una venta "
   "de un cliente fantasma**, y es imposible borrar un cliente que tiene ventas (la base protege la coherencia sola).\n\n"
   "Estas reglas se llaman **constraints** (restricciones). Otras de la familia: `NOT NULL` (obligatorio), "
   "`UNIQUE` (sin repetidos), `CHECK` (condición a cumplir, ej: `CHECK (edad >= 0)`)."}
 ],
 "quiz": [
  {"pregunta": "¿Qué garantiza una PRIMARY KEY?",
   "opciones": ["Que la columna sea de texto", "Que cada fila tenga un identificador único e irrepetible", "Que la tabla sea rápida"],
   "correcta": 1,
   "explicacion": "La PK identifica cada fila sin duplicados. La base lo impone con una muralla, no con una sugerencia."},
  {"pregunta": "Intentas insertar una venta con cliente_id = 999, pero ese cliente no existe. ¿Qué pasa?",
   "opciones": ["Se inserta igual", "La FK lo rechaza con error: no hay ventas de clientes fantasma", "Se crea el cliente automáticamente"],
   "correcta": 1,
   "explicacion": "La clave foránea garantiza la coherencia entre tablas: REFERENCES exige que el valor exista en la tabla apuntada."},
  {"pregunta": "¿Qué constraint usarías para impedir edades negativas?",
   "opciones": ["CHECK (edad >= 0)", "UNIQUE", "PRIMARY KEY"],
   "correcta": 0,
   "explicacion": "CHECK valida una condición en cada fila. UNIQUE evita repetidos; PK identifica filas."}
 ]
})

L.append({
 "id": "1.8", "titulo": "JOIN: combinar tablas",
 "paginas": [
  {"titulo": "La consulta que une mundos", "contenido":
   "Tus datos están repartidos (clientes por un lado, ventas por otro) y relacionados por claves. "
   "El **JOIN** los junta en una sola respuesta:\n\n"
   "```sql\nSELECT c.nombre, v.fecha, v.total\nFROM   clientes c\nJOIN   ventas   v ON v.cliente_id = c.id;\n```\n\n"
   "- `clientes c` → \"llamaré c a clientes\" (un alias, para abreviar).\n"
   "- `ON v.cliente_id = c.id` → la condición de unión: junta cada venta con SU cliente (la FK encontrándose con su PK).\n\n"
   "Se lee: \"muéstrame el nombre del cliente junto a la fecha y total de cada una de sus ventas\"."},
  {"titulo": "INNER vs LEFT: ¿y los que no tienen pareja?", "contenido":
   "- `JOIN` (o INNER JOIN) → solo las coincidencias: clientes CON ventas.\n"
   "- `LEFT JOIN` → todos los de la izquierda, tengan o no pareja: **todos** los clientes, y NULL en las columnas de venta "
   "para los que nunca compraron.\n\n"
   "```sql\nSELECT c.nombre, v.id\nFROM clientes c\nLEFT JOIN ventas v ON v.cliente_id = c.id\nWHERE v.id IS NULL;\n```\n"
   "→ ¡los clientes que **nunca** han comprado! (todos, menos los que tienen pareja). Combina JOIN + NULL de la lección 1.6: "
   "las piezas del curso empiezan a encajar entre sí. 🧩",
   "practica": {"instruccion": "Une clientes c con ventas v por la condición v.cliente_id = c.id, pidiendo c.nombre y v.fecha. (Usa JOIN ... ON)",
                "respuestas": ["select c.nombre, v.fecha from clientes c join ventas v on v.cliente_id = c.id",
                               "select c.nombre, v.fecha from clientes c inner join ventas v on v.cliente_id = c.id"],
                "pista": "SELECT c.nombre, v.fecha FROM clientes c JOIN ventas v ON v.cliente_id = c.id",
                "ok": "¡Tu primer JOIN! La consulta más importante del SQL relacional."}}
 ],
 "quiz": [
  {"pregunta": "¿Qué hace la cláusula ON en un JOIN?",
   "opciones": ["Enciende la tabla", "Define la condición de unión entre las tablas (típicamente FK = PK)", "Ordena el resultado"],
   "correcta": 1,
   "explicacion": "ON dice cómo se emparejan las filas: cada venta con su cliente vía cliente_id = id."},
  {"pregunta": "Quieres TODOS los clientes, hayan comprado o no. ¿Qué usas?",
   "opciones": ["INNER JOIN", "LEFT JOIN", "DROP JOIN"],
   "correcta": 1,
   "explicacion": "LEFT JOIN conserva todos los de la izquierda; los sin pareja muestran NULL en las columnas de la derecha."},
  {"pregunta": "En un LEFT JOIN de clientes a ventas, ¿qué significa que v.id sea NULL?",
   "opciones": ["Un error en la base", "Ese cliente no tiene ventas (no encontró pareja)", "La venta fue anulada"],
   "correcta": 1,
   "explicacion": "El NULL de \"sin pareja\" permite trucos como encontrar clientes que nunca compraron."}
 ]
})

L.append({
 "id": "1.9", "titulo": "Agrupar y resumir: GROUP BY",
 "paginas": [
  {"titulo": "De filas a respuestas", "contenido":
   "El negocio no pregunta \"dame las 80.000 ventas\": pregunta \"¿cuánto vendimos **por mes**?\". Para eso se agrupa:\n\n"
   "```sql\nSELECT ciudad,\n       COUNT(*)   AS cantidad,\n       AVG(edad)  AS edad_promedio\nFROM clientes\nGROUP BY ciudad;\n```\n\n"
   "`GROUP BY ciudad` = \"haz un montoncito por cada ciudad y calcula lo pedido sobre cada montoncito\".\n\n"
   "Las funciones de agregación: `COUNT` (cuenta), `SUM` (suma), `AVG` (promedio), `MAX`, `MIN`."},
  {"titulo": "HAVING: filtrar montoncitos", "contenido":
   "```sql\nSELECT ciudad, COUNT(*) AS cantidad\nFROM clientes\nWHERE edad >= 18          -- filtra FILAS, antes de agrupar\nGROUP BY ciudad\nHAVING COUNT(*) > 10;     -- filtra GRUPOS, ya formados\n```\n\n"
   "🎤 La diferencia WHERE vs HAVING es LA pregunta de entrevista de SQL:\n"
   "- **WHERE** filtra filas individuales ANTES de armar los grupos.\n"
   "- **HAVING** filtra los grupos DESPUÉS de formados (por eso puede usar COUNT, SUM...).\n\n"
   "Con tus palabras: WHERE elige qué entra a la juguera; HAVING elige qué jugos se sirven.",
   "practica": {"instruccion": "Cuenta cuántos clientes hay por ciudad: pide ciudad y COUNT(*) desde clientes, agrupando por ciudad.",
                "respuestas": ["select ciudad, count(*) from clientes group by ciudad"],
                "pista": "SELECT ciudad, COUNT(*) FROM clientes GROUP BY ciudad",
                "ok": "¡Perfecto! Acabas de pasar de filas sueltas a respuestas de negocio."}}
 ],
 "quiz": [
  {"pregunta": "¿Cuál es la diferencia entre WHERE y HAVING?",
   "opciones": ["Ninguna, son sinónimos", "WHERE filtra filas antes de agrupar; HAVING filtra grupos ya formados", "HAVING es más rápido"],
   "correcta": 1,
   "explicacion": "WHERE elige qué entra a la juguera; HAVING elige qué jugos se sirven. LA pregunta de entrevista de SQL."},
  {"pregunta": "¿Qué función usarías para el total vendido por mes?",
   "opciones": ["COUNT", "SUM", "MAX"],
   "correcta": 1,
   "explicacion": "SUM suma valores (los montos). COUNT contaría cuántas ventas hubo."},
  {"pregunta": "¿Por qué `WHERE COUNT(*) > 10` da error?",
   "opciones": ["Porque COUNT solo funciona los lunes", "Porque WHERE actúa antes de agrupar: aún no existen los conteos (eso es trabajo de HAVING)", "No da error"],
   "correcta": 1,
   "explicacion": "Las funciones de agregación se evalúan al agrupar; por eso sus filtros van en HAVING."}
 ]
})

L.append({
 "id": "1.10", "titulo": "Checkpoint Nivel 1 + tu mini proyecto",
 "paginas": [
  {"titulo": "Tu mini proyecto (hazlo en tu laboratorio)", "contenido":
   "En tu Oracle del Módulo 0, construye la base de un negocio que conozcas (almacén, veterinaria, librería):\n\n"
   "1. **DDL**: crea CLIENTES, PRODUCTOS, VENTAS y DETALLE_VENTAS con sus PK, FK, NOT NULL y al menos un CHECK.\n"
   "2. **DML**: inserta 5 clientes, 10 productos y 15 ventas. Confirma con COMMIT.\n"
   "3. Equivócate a propósito: inserta una venta con cliente inexistente (debe fallar), un id duplicado (debe fallar). "
   "Ver las murallas funcionando vale más que leerlas.\n"
   "4. **Consultas**: ventas por cliente (JOIN + GROUP BY), productos nunca vendidos (LEFT JOIN + IS NULL), "
   "top 3 productos por monto (SUM + ORDER BY).\n\n"
   "Guarda tus scripts en un archivo: es la primera pieza de tu portafolio."},
  {"titulo": "Checkpoint", "contenido":
   "Deberías poder explicar sin mirar:\n\n"
   "✅ Las 5 familias del SQL y un comando de cada una\n"
   "✅ DELETE vs TRUNCATE (con el porqué)\n"
   "✅ Por qué `NULL = NULL` no es verdadero\n"
   "✅ Qué garantizan una PK y una FK\n"
   "✅ INNER vs LEFT JOIN\n"
   "✅ WHERE vs HAVING\n\n"
   "El quiz final mezcla todo el nivel. Al aprobarlo desbloqueas el **Nivel 2: la arquitectura de Oracle por dentro** — "
   "donde dejarás de usar la base de datos y empezarás a entenderla. 🚀"}
 ],
 "quiz": [
  {"pregunta": "CREATE es a DDL como INSERT es a...",
   "opciones": ["DCL", "DML", "TCL"],
   "correcta": 1,
   "explicacion": "CREATE define estructuras (DDL); INSERT manipula contenido (DML)."},
  {"pregunta": "¿Cuál de estos NO se puede deshacer con ROLLBACK?",
   "opciones": ["DELETE", "UPDATE", "TRUNCATE"],
   "correcta": 2,
   "explicacion": "TRUNCATE es DDL: definitivo al instante. DELETE y UPDATE son DML: borrador hasta el COMMIT."},
  {"pregunta": "Quieres los clientes que NUNCA han comprado. ¿Qué combinación usas?",
   "opciones": ["INNER JOIN + COUNT", "LEFT JOIN + WHERE columna_de_ventas IS NULL", "DELETE + WHERE"],
   "correcta": 1,
   "explicacion": "LEFT JOIN conserva a todos; el NULL marca a los sin pareja. Piezas de 1.6 + 1.8 encajando."},
  {"pregunta": "Insertas dos clientes con el mismo id (que es PK). ¿Qué pasa con el segundo?",
   "opciones": ["Se inserta y quedan duplicados", "Falla con ORA-00001: la PK es una muralla", "Reemplaza al primero"],
   "correcta": 1,
   "explicacion": "La PK impide duplicados físicamente. ORA-00001: tu primer error con nombre y apellido."},
  {"pregunta": "¿Dónde va el filtro \"solo grupos con más de 5 ventas\"?",
   "opciones": ["En el WHERE", "En el HAVING", "En el ORDER BY"],
   "correcta": 1,
   "explicacion": "Filtra grupos ya formados (usa COUNT): es trabajo de HAVING."}
 ]
})

nivel_sql = {
  "nivel": 2,
  "etiqueta": "Nivel 1",
  "emoji": "🧱",
  "titulo": "SQL: el idioma de las bases de datos",
  "descripcion": "DDL, DML y las 5 familias del SQL; SELECT, NULL, claves, JOIN y GROUP BY. 10 lecciones con práctica.",
  "lecciones": L,
}

with open("contenido/nivel2.json", "w", encoding="utf-8") as f:
    json.dump(nivel_sql, f, ensure_ascii=False, indent=1)

print("Lecciones:", len(L), "| Quiz:", sum(len(l['quiz']) for l in L),
      "| Prácticas:", sum(1 for l in L for p in l['paginas'] if 'practica' in p))
