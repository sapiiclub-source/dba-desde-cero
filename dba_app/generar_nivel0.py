# -*- coding: utf-8 -*-
"""Genera contenido/nivel0.json con las 10 lecciones de la Parte 0."""
import json

L = []  # lecciones

L.append({
 "id": "0.1", "titulo": "¿Qué es un dato?",
 "paginas": [
  {"titulo": "Empecemos por el principio", "contenido":
   "Un **dato** es un pedacito de información que describe algo: tu nombre, tu edad, el precio de un kilo de pan.\n\n"
   "- \"Camila\" es un dato.\n- \"34\" es un dato.\n- \"Camila tiene 34 años\" es **información**: datos combinados que significan algo.\n\n"
   "💡 **Analogía**: los datos son como ingredientes sueltos; la información es el plato cocinado."},
  {"titulo": "Por qué existe tu futura profesión", "contenido":
   "Las empresas viven de datos: quiénes son sus clientes, qué compraron, cuánto deben, qué hay en bodega.\n\n"
   "Si una empresa **pierde sus datos**, en la práctica deja de existir.\n\n"
   "Por eso alguien tiene que guardarlos de forma **segura**, **ordenada** y **rápida de encontrar**. "
   "Esa persona es el o la **DBA** (*Database Administrator*: administrador/a de bases de datos). En eso te vas a convertir."}
 ],
 "quiz": [
  {"pregunta": "¿Cuál es la diferencia entre dato e información?",
   "opciones": ["Son exactamente lo mismo",
                "El dato es un pedacito suelto; la información es datos combinados con significado",
                "La información se guarda en papel y el dato en computador"],
   "correcta": 1,
   "explicacion": "El dato es la pieza suelta (\"34\"); la información es la combinación con significado (\"Camila tiene 34 años\")."},
  {"pregunta": "¿Qué significa DBA?",
   "opciones": ["Database Administrator (administrador/a de bases de datos)",
                "Digital Business Analyst", "Data Backup Application"],
   "correcta": 0,
   "explicacion": "DBA = Database Administrator: la persona que cuida los datos de una organización."},
  {"pregunta": "¿Por qué los datos son críticos para una empresa?",
   "opciones": ["Porque ocupan espacio en disco",
                "Porque si los pierde, en la práctica deja de poder operar",
                "Porque son bonitos en los reportes"],
   "correcta": 1,
   "explicacion": "Sin sus datos (clientes, deudas, inventario), una empresa no puede funcionar. Por eso existe el rol del DBA."}
 ]
})

L.append({
 "id": "0.2", "titulo": "El computador por dentro (la cocina)",
 "paginas": [
  {"titulo": "Las 3 piezas que te importan", "contenido":
   "Imagina la cocina de un restaurante:\n\n"
   "| Pieza | En la cocina | Qué hace |\n|---|---|---|\n"
   "| **CPU** (procesador) | El cocinero | Quien *trabaja*: hace cálculos, ejecuta órdenes |\n"
   "| **RAM** (memoria) | El mesón de trabajo | Lo que el cocinero usa AHORA. Rapidísima, pequeña, y **se borra al apagar** |\n"
   "| **Disco** | La despensa/bodega | Guarda TODO de forma permanente. Enorme pero **lento** |\n"},
  {"titulo": "La regla de oro del curso", "contenido":
   "⚡ **Trabajar en la RAM es miles de veces más rápido que ir al disco.**\n\n"
   "Para dimensionar: si leer algo de la RAM tardara **1 segundo**, leer lo mismo de un disco mecánico tardaría **más de un día**.\n\n"
   "Gran parte del trabajo de una base de datos (y del DBA) es lograr que los datos más usados estén \"en el mesón\" "
   "y no haya que ir a la \"bodega\" a cada rato. Esta idea va a reaparecer una y otra vez en el curso."}
 ],
 "quiz": [
  {"pregunta": "En la analogía de la cocina, ¿qué es la RAM?",
   "opciones": ["La despensa donde se guarda todo", "El mesón de trabajo del cocinero", "El cocinero"],
   "correcta": 1,
   "explicacion": "La RAM es el mesón: rápida y a mano, pero pequeña y se limpia al apagar. La despensa es el disco; el cocinero es la CPU."},
  {"pregunta": "¿Qué le pasa a la RAM cuando se corta la luz?",
   "opciones": ["Nada, conserva todo", "Se borra por completo", "Se pasa automáticamente al disco"],
   "correcta": 1,
   "explicacion": "La RAM es volátil: al apagar, se borra. Por eso lo permanente vive en el disco (y por eso existirá el \"redo\", que conocerás más adelante)."},
  {"pregunta": "¿Cuál es la regla de oro sobre RAM y disco?",
   "opciones": ["El disco es más rápido porque es más grande",
                "Son igual de rápidos en computadores modernos",
                "La RAM es miles de veces más rápida que el disco"],
   "correcta": 2,
   "explicacion": "RAM ≫ disco en velocidad. Mantener los datos calientes en memoria es la mitad del rendimiento de una base de datos."}
 ]
})

L.append({
 "id": "0.3", "titulo": "Programas, procesos y sistemas operativos",
 "paginas": [
  {"titulo": "Programa vs proceso", "contenido":
   "- Un **programa** es una lista de instrucciones guardada (WhatsApp instalado en tu teléfono).\n"
   "- Un **proceso** es ese programa **en ejecución**, ocupando RAM y CPU (WhatsApp abierto).\n\n"
   "Esta diferencia te importará mucho: Oracle funcionando son **decenas de procesos cooperando**, cada uno con su tarea."},
  {"titulo": "El sistema operativo y por qué Linux", "contenido":
   "El **sistema operativo (SO)** es el programa jefe: reparte CPU y RAM entre procesos, maneja disco, pantalla y red. "
   "Windows, macOS, Android y **Linux** son sistemas operativos.\n\n"
   "**¿Por qué Linux?** Casi todas las bases de datos serias del mundo corren sobre Linux: gratuito, estable, "
   "y se controla escribiendo **comandos** en una **terminal** (una ventana de texto).\n\n"
   "Al principio la terminal intimida. En un mes la vas a preferir: escribir es más preciso y automatizable que cliquear."},
  {"titulo": "Tu primer comando", "contenido":
   "En una terminal Linux, el comando `pwd` significa *print working directory*: \"¿en qué carpeta estoy parada?\".\n\n"
   "Otros que usarás a diario:\n- `ls` → ¿qué archivos hay aquí?\n- `cd nombre` → moverse a una carpeta\n- `cat archivo` → ver el contenido de un archivo",
   "practica": {"instruccion": "Estás en una terminal Linux y quieres saber en qué carpeta estás. ¿Qué comando escribes?",
                "respuestas": ["pwd"], "pista": "Son 3 letras: print working directory.",
                "ok": "¡Exacto! `pwd` te dice dónde estás. Es el primer comando de todo el mundo en Linux."}}
 ],
 "quiz": [
  {"pregunta": "¿Cuál es la diferencia entre programa y proceso?",
   "opciones": ["Ninguna, son sinónimos",
                "El programa son las instrucciones guardadas; el proceso es el programa ejecutándose",
                "El proceso está en el disco y el programa en la RAM"],
   "correcta": 1,
   "explicacion": "Programa = instrucciones guardadas. Proceso = programa corriendo, usando RAM y CPU. Oracle son decenas de procesos."},
  {"pregunta": "¿Por qué las bases de datos serias suelen correr en Linux?",
   "opciones": ["Porque tiene mejores gráficos", "Porque es gratuito, estable y automatizable por comandos", "Porque es el único que soporta Oracle"],
   "correcta": 1,
   "explicacion": "Linux domina los servidores por estabilidad, costo y control por terminal. Por eso lo aprenderás en paralelo."},
  {"pregunta": "¿Qué hace el comando `ls`?",
   "opciones": ["Lista los archivos de la carpeta actual", "Apaga el computador", "Borra un archivo"],
   "correcta": 0,
   "explicacion": "`ls` lista lo que hay en la carpeta. Junto a `pwd` y `cd` son tus primeros pasos en la terminal."}
 ]
})

L.append({
 "id": "0.4", "titulo": "Archivos: donde todo termina viviendo",
 "paginas": [
  {"titulo": "Archivos y bytes", "contenido":
   "Un **archivo** es un paquete de datos con nombre, guardado en el disco: una foto, un documento, una canción.\n\n"
   "Para el computador, TODO archivo es una secuencia de números llamados **bytes** (un byte guarda más o menos una letra). "
   "La extensión (.jpg, .docx) es solo una pista de cómo interpretarlos."},
  {"titulo": "El secreto adelantado", "contenido":
   "🤫 Te adelanto algo importante: una base de datos Oracle, al final del día, **es un conjunto de archivos en el disco** "
   "— archivos muy especiales que solo Oracle sabe leer y escribir.\n\n"
   "Cuando más adelante hablemos de \"datafiles\", recuerda esta lección: **no es magia, son archivos**. "
   "Y por eso respaldar una base será, en esencia, copiar archivos... con un truco genial que descubrirás."}
 ],
 "quiz": [
  {"pregunta": "¿Qué es un byte?",
   "opciones": ["Un tipo de virus", "La unidad mínima de almacenamiento (~una letra)", "Un programa pequeño"],
   "correcta": 1,
   "explicacion": "El byte es la unidad mínima: todo archivo es una secuencia de bytes."},
  {"pregunta": "Una base de datos Oracle, físicamente, ¿qué es?",
   "opciones": ["Un conjunto de archivos especiales en el disco", "Una página web", "Un componente de hardware"],
   "correcta": 0,
   "explicacion": "Oracle guarda los datos en archivos del disco (los \"datafiles\"). Desmitificarlo desde ya te servirá todo el curso."},
  {"pregunta": "¿Qué indica la extensión de un archivo (.jpg, .docx)?",
   "opciones": ["El tamaño del archivo", "Una pista de cómo interpretar sus bytes", "La carpeta donde debe guardarse"],
   "correcta": 1,
   "explicacion": "La extensión es solo una convención para saber cómo leer esos bytes."}
 ]
})

L.append({
 "id": "0.5", "titulo": "Servidores y la nube",
 "paginas": [
  {"titulo": "Un servidor no tiene nada de místico", "contenido":
   "Un **servidor** es simplemente un computador que trabaja para otros computadores: como tu notebook pero más potente, "
   "sin pantalla bonita, en una sala fría, encendido 24/7, y cuyo trabajo es **responder pedidos**.\n\n"
   "- Tu teléfono (el **cliente**) pide: \"muéstrame mi saldo\".\n- El servidor del banco busca el dato y responde.\n\n"
   "Este modelo se llama **cliente-servidor** y es la arquitectura de casi todo internet. "
   "La base de datos vive en un servidor; usuarios y aplicaciones son clientes que le hacen pedidos."},
  {"titulo": "¿Y \"la nube\"?", "contenido":
   "**La nube (cloud)** es alquilar servidores ajenos en vez de comprar propios. Amazon (AWS), Microsoft (Azure), "
   "Google y Oracle (OCI) tienen edificios con miles de servidores y arriendan pedacitos por hora.\n\n"
   "Para ti como DBA significa: **los mismos conceptos, pero el \"fierro\" es de otro**. Lo veremos en serio al final del curso."}
 ],
 "quiz": [
  {"pregunta": "¿Qué es un servidor?",
   "opciones": ["Un computador que responde pedidos de otros computadores", "Un programa antivirus", "Un cable de red especial"],
   "correcta": 0,
   "explicacion": "Servidor = computador potente, siempre encendido, dedicado a atender pedidos de clientes."},
  {"pregunta": "En el modelo cliente-servidor, tu teléfono consultando el saldo del banco es...",
   "opciones": ["El servidor", "El cliente", "La nube"],
   "correcta": 1,
   "explicacion": "Quien pide es el cliente; quien responde es el servidor."},
  {"pregunta": "¿Qué es \"la nube\"?",
   "opciones": ["Internet inalámbrico", "Alquilar servidores de empresas como AWS, Azure u OCI", "Un tipo de base de datos"],
   "correcta": 1,
   "explicacion": "La nube es arrendar computación ajena. Mismos conceptos de siempre; el hardware es de otro."}
 ]
})

L.append({
 "id": "0.6", "titulo": "Redes en 10 minutos: IP y puerto",
 "paginas": [
  {"titulo": "La dirección y el departamento", "contenido":
   "Para que cliente y servidor conversen necesitan una **red**:\n\n"
   "- Cada computador tiene una **dirección IP**: su \"dirección de casa\" (ej: `192.168.1.50`).\n"
   "- Dentro de un computador pueden vivir varios servicios. El **puerto** es el número de \"departamento\" "
   "que distingue a cada uno. Oracle atiende, por costumbre, en el puerto **1521**.\n\n"
   "💡 \"Conectarse a la base de datos\" = enviar un mensaje a la IP del servidor, puerto 1521, y esperar respuesta."},
  {"titulo": "Diagnóstico básico (y PuTTY)", "contenido":
   "Cuando algo \"no conecta\", el diagnóstico empieza aquí: ¿llego a esa IP? ¿está abierto ese puerto?\n\n"
   "- `ping 192.168.1.50` → ¿el servidor responde en la red?\n"
   "- Programas como **PuTTY** (en Windows) sirven para conectarse a la **terminal de un servidor Linux remoto** "
   "por la red, usando el protocolo **SSH** (conexión segura, puerto 22). Es la herramienta diaria del DBA: "
   "desde tu escritorio, controlas servidores que pueden estar en otra ciudad.\n\n"
   "En el Módulo 0 te conectarás por SSH a tu propio laboratorio, paso a paso.",
   "practica": {"instruccion": "Quieres saber si el servidor 10.0.0.5 responde en la red. ¿Qué comando usas?",
                "respuestas": ["ping 10.0.0.5"], "pista": "Es el comando que hace 'eco' en la red + la IP.",
                "ok": "¡Correcto! `ping` es siempre la primera pregunta: ¿estás vivo y te alcanzo?"}}
 ],
 "quiz": [
  {"pregunta": "¿Qué es un puerto?",
   "opciones": ["La velocidad de la red", "El número que distingue a cada servicio dentro de un mismo computador", "Un tipo de cable"],
   "correcta": 1,
   "explicacion": "IP = edificio; puerto = departamento. Oracle atiende típicamente en el 1521; SSH en el 22."},
  {"pregunta": "¿Para qué sirve PuTTY?",
   "opciones": ["Para dibujar diagramas", "Para conectarse por SSH a la terminal de un servidor remoto", "Para crear tablas en Oracle"],
   "correcta": 1,
   "explicacion": "PuTTY abre una terminal segura (SSH) hacia servidores Linux remotos: la herramienta diaria del DBA en Windows."},
  {"pregunta": "¿En qué puerto atiende Oracle por convención?",
   "opciones": ["80", "22", "1521"],
   "correcta": 2,
   "explicacion": "1521 es el puerto clásico de Oracle. El 22 es SSH y el 80/443 son páginas web."}
 ]
})

L.append({
 "id": "0.7", "titulo": "¿Por qué Excel no basta?",
 "paginas": [
  {"titulo": "Los 5 problemas de la planilla", "contenido":
   "Casi todo el mundo parte guardando datos en planillas. Funciona... hasta que deja de funcionar:\n\n"
   "1. **Dos personas no pueden modificarla a la vez** sin pisarse.\n"
   "2. Un corte de luz a mitad de un guardado puede dejar el archivo **corrupto** (dañado).\n"
   "3. Nada impide escribir \"treinta y dos\" en la columna edad, o duplicar un cliente.\n"
   "4. Con 5 millones de filas, buscar algo es eterno.\n"
   "5. Quien tiene el archivo **lo ve TODO**: no hay permisos finos."},
  {"titulo": "La base de datos: 5 soluciones", "contenido":
   "Una **base de datos** es un programa especializado que resuelve exactamente esos 5 problemas. "
   "Guarda los datos en **tablas** (filas y columnas), pero además:\n\n"
   "1. Miles de personas leen y escriben a la vez sin pisarse (**concurrencia**).\n"
   "2. **Garantiza** que ningún corte de luz deje datos a medias (verás cómo: es una de las ideas más bellas de la informática).\n"
   "3. **Impone reglas**: la edad es un número; no hay dos clientes con el mismo RUT.\n"
   "4. Encuentra una fila entre mil millones en milésimas de segundo (con índices).\n"
   "5. Controla **quién ve y toca qué**.\n\n"
   "El programa que hace todo esto se llama **motor de base de datos** o **RDBMS** (sistema administrador de bases de datos *relacionales*: organizadas en tablas relacionadas entre sí)."}
 ],
 "quiz": [
  {"pregunta": "¿Qué es la concurrencia?",
   "opciones": ["Muchas personas usando los datos a la vez sin pisarse", "Una competencia entre bases de datos", "La velocidad del disco"],
   "correcta": 0,
   "explicacion": "Concurrencia = uso simultáneo seguro. Es uno de los grandes problemas que la base de datos resuelve y Excel no."},
  {"pregunta": "¿Qué significa que un archivo quede \"corrupto\"?",
   "opciones": ["Que tiene virus", "Que quedó dañado/ilegible, por ejemplo por un corte a mitad de un guardado", "Que está protegido con clave"],
   "correcta": 1,
   "explicacion": "Corrupto = dañado. Las bases de datos están diseñadas para que un corte de luz JAMÁS deje los datos a medias."},
  {"pregunta": "¿Qué significa la R de RDBMS?",
   "opciones": ["Rápido", "Relacional: los datos se organizan en tablas relacionadas entre sí", "Respaldado"],
   "correcta": 1,
   "explicacion": "Relacional: tablas conectadas por claves. Es el modelo que dominarás en este curso."}
 ]
})

L.append({
 "id": "0.8", "titulo": "¿Qué es Oracle? (y quiénes son los demás)",
 "paginas": [
  {"titulo": "El gigante", "contenido":
   "**Oracle Database** es el motor de base de datos más usado por las grandes empresas del mundo "
   "(bancos, retail, gobiernos, agroindustria). Existe desde 1979, es extremadamente potente y completo... "
   "y por lo mismo, complejo: dominarlo es una profesión en sí misma, **y bien pagada**."},
  {"titulo": "El vecindario", "contenido":
   "Otros motores que escucharás (los conceptos del curso te servirán en todos):\n\n"
   "| Motor | En una frase |\n|---|---|\n"
   "| **SQL Server** | El de Microsoft; muy común en empresas medianas |\n"
   "| **PostgreSQL** | Gratuito y open source; favorito de proyectos nuevos |\n"
   "| **MySQL/MariaDB** | Gratuito; mueve gran parte de la web |\n"
   "| **MongoDB (NoSQL)** | Familia distinta: no usa tablas |\n\n"
   "Este curso se centra en Oracle porque es el más profundo: **si entiendes Oracle por dentro, los demás te parecerán sencillos**."}
 ],
 "quiz": [
  {"pregunta": "¿Por qué este curso se centra en Oracle?",
   "opciones": ["Porque es el único motor que existe",
                "Porque es el más profundo y el que más demanda DBAs especializados",
                "Porque es gratuito y simple"],
   "correcta": 1,
   "explicacion": "Oracle es el motor de las grandes empresas; dominarlo te abre todos los demás."},
  {"pregunta": "¿Cuál de estos motores es de Microsoft?",
   "opciones": ["PostgreSQL", "SQL Server", "MySQL"],
   "correcta": 1,
   "explicacion": "SQL Server es el motor de Microsoft, muy común en empresas medianas."},
  {"pregunta": "¿Qué tiene de distinto MongoDB?",
   "opciones": ["Es más antiguo que Oracle", "Pertenece a la familia NoSQL: no organiza los datos en tablas", "Solo funciona en Windows"],
   "correcta": 1,
   "explicacion": "Los NoSQL usan otros modelos (documentos, llaves-valor). Los entenderás mejor cuando domines lo relacional."}
 ]
})

L.append({
 "id": "0.9", "titulo": "Un día en la vida de un/a DBA",
 "paginas": [
  {"titulo": "Las 6 responsabilidades", "contenido":
   "1. **Mantener viva la base**: encendida, con espacio, respaldada.\n"
   "2. **Respaldos y recuperación**: la responsabilidad sagrada. Si se incendia el servidor, el DBA reconstruye los datos. "
   "*Un DBA que no puede recuperar, no es DBA.*\n"
   "3. **Performance**: \"el sistema está lento\" será la frase que más escucharás. Diagnosticarlo es lo que distingue a los seniors.\n"
   "4. **Seguridad y permisos**: quién entra, qué ve, qué queda registrado.\n"
   "5. **Apoyar a los desarrolladores**: revisar consultas, diseñar tablas, automatizar.\n"
   "6. **Instalar, actualizar, migrar**: versiones nuevas, servidores nuevos, la nube."},
  {"titulo": "El perfil", "contenido":
   "Es una mezcla de:\n\n"
   "- 🚒 **Bombero**: emergencias (\"¡se cayó la base!\").\n"
   "- 🕵️ **Detective**: diagnósticos (\"¿por qué está lento desde ayer?\").\n"
   "- 🏗️ **Arquitecto**: diseño (\"¿cómo estructuramos estos datos para los próximos 10 años?\").\n\n"
   "Nunca es aburrido. Y este curso te entrena en los tres roles."}
 ],
 "quiz": [
  {"pregunta": "¿Cuál es la responsabilidad \"sagrada\" del DBA?",
   "opciones": ["Hacer reportes bonitos", "Poder respaldar y RECUPERAR los datos ante cualquier desastre", "Instalar Windows"],
   "correcta": 1,
   "explicacion": "A un DBA no lo despiden por una base lenta; lo despiden por no poder recuperar los datos."},
  {"pregunta": "¿Cuál será la frase que más escucharás como DBA?",
   "opciones": ["\"El sistema está lento\"", "\"Sobra espacio en disco\"", "\"No necesitamos respaldos\""],
   "correcta": 0,
   "explicacion": "Diagnosticar lentitud con método (y no adivinando) es la habilidad que distingue a los seniors. Tendrá su propio nivel en el curso."},
  {"pregunta": "El rol del DBA combina tres perfiles. ¿Cuáles?",
   "opciones": ["Vendedor, contador y diseñador", "Bombero, detective y arquitecto", "Profesor, médico y piloto"],
   "correcta": 1,
   "explicacion": "Emergencias (bombero), diagnóstico (detective) y diseño (arquitecto)."}
 ]
})

L.append({
 "id": "0.10", "titulo": "Tus herramientas y el checkpoint final",
 "paginas": [
  {"titulo": "Con qué vas a estudiar", "contenido":
   "- **Terminal de Linux**: la ventana de texto donde escribes comandos (y **PuTTY** para llegar a ella desde Windows).\n"
   "- **SQL*Plus**: el programa más básico para \"conversar\" con Oracle escribiendo. Feo pero universal: está en todos los servidores del planeta.\n"
   "- **SQL Developer / VS Code**: editores gráficos más cómodos para el día a día.\n"
   "- 📓 **Un cuaderno**: anotar con tus palabras es la técnica de estudio más efectiva que existe."},
  {"titulo": "Checkpoint de la Parte 0", "contenido":
   "Antes de seguir, deberías poder explicarle a un amigo, **sin mirar**:\n\n"
   "✅ La diferencia entre RAM y disco (y por qué importa la velocidad)\n"
   "✅ Qué es un servidor y el modelo cliente-servidor\n"
   "✅ Qué es una IP y un puerto\n"
   "✅ Por qué una empresa usa Oracle en vez de Excel\n\n"
   "¿Puedes? El quiz final de esta lección repasa TODA la Parte 0. Apruébalo y desbloqueas el **Módulo 0: tu laboratorio**, "
   "donde instalarás tu propia base de datos Oracle. 🚀"}
 ],
 "quiz": [
  {"pregunta": "¿Por qué el COMMIT... perdón, ¿por qué la RAM no sirve para guardar datos permanentes?",
   "opciones": ["Porque es muy cara", "Porque se borra al apagar el computador", "Porque es muy lenta"],
   "correcta": 1,
   "explicacion": "La RAM es volátil. Lo permanente vive en disco. (Y sí: la pregunta empezó con una palabra del futuro... la entenderás en el Módulo 4 😉)."},
  {"pregunta": "\"Conectarse a la base de datos\" significa enviar un mensaje a...",
   "opciones": ["La IP del servidor, en el puerto donde Oracle atiende (típicamente 1521)", "Cualquier computador de la red", "La impresora del servidor"],
   "correcta": 0,
   "explicacion": "IP (el edificio) + puerto (el departamento). Si no conecta: ¿llego a la IP? ¿está abierto el puerto?"},
  {"pregunta": "¿Cuál de los 5 problemas de Excel NO resuelve una base de datos?",
   "opciones": ["La concurrencia", "Las reglas sobre los datos", "Ninguno: resuelve los cinco"],
   "correcta": 2,
   "explicacion": "Concurrencia, resistencia a fallas, reglas, búsqueda veloz y permisos: la base de datos resuelve los cinco. Por eso existe."},
  {"pregunta": "¿Qué herramienta usarás para llegar desde Windows a la terminal de un servidor Linux?",
   "opciones": ["Excel", "PuTTY (conexión SSH)", "SQL Developer"],
   "correcta": 1,
   "explicacion": "PuTTY abre una terminal remota segura (SSH). En el Módulo 0 la usarás con tu propio laboratorio."}
 ]
})

nivel0 = {
  "nivel": 0,
  "emoji": "🌱",
  "titulo": "El mundo antes de las bases de datos",
  "descripcion": "Para quien parte de cero absoluto: computadores, servidores, redes y por qué existen las bases de datos. 10 lecciones cortas.",
  "lecciones": L,
}

with open("contenido/nivel0.json", "w", encoding="utf-8") as f:
    json.dump(nivel0, f, ensure_ascii=False, indent=1)

print("Lecciones:", len(L), "| Quiz total:", sum(len(l["quiz"]) for l in L))
