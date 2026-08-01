# 🎙️ Guía Docente Diapositiva por Diapositiva — Sesión 3: Docker Compose y Aplicaciones Multi-Contenedor
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Instructor:** Ing. Cristian Jampier Chileno Segundo | OTI - UNI  
**Programa:** Programa de Iniciación Tecnológica (PIT 2026) — Universidad Nacional de Ingeniería  
**Total Diapositivas:** 25 Diapositivas  

---

## 🎯 Instrucciones de Orientación Pedagógica
Esta guía contiene la explicación detallada y el guión profesional en primera persona para abordar **cada una de las 25 diapositivas** de la presentación oficial de la Sesión 3.
Está diseñada para guiar la clase paso a paso, enseñando a orquestar stacks con múltiples servicios (Flask + PostgreSQL), entender la sintaxis YAML de `docker-compose.yml`, dominar el Service Discovery (DNS interno por nombre de servicio) y gestionar variables de entorno de forma segura con `.env`.

---

## 🖥️ Explicación Diapositiva por Diapositiva (1 a 25)

### 📄 Diapositiva 1: DOCKER DESDE CERO: Crea y Despliega Aplicaciones — Sesión 3
**Contenido de la PPT:**
```text
DOCKER DESDE CERO: Crea y Despliega Aplicaciones
INSTRUCTOR: Cristian Jampier Chileno Segundo
PROGRAMA DE INICIACIÓN TECNOLÓGICA — PIT 2026
Oficina de Tecnologías de la Información (OTI - UNI)
Programa Completo — PIT 2026
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Muy buenos días/tardes a todos. Bienvenidos a la **Sesión 3** del curso *Docker desde Cero: Crea y Despliega Aplicaciones*, organizado por la OTI-UNI.
> En las dos primeras sesiones aprendimos a trabajar con contenedores individuales y a redactar recetas de imágenes con Dockerfile. Pero en el mundo real, los sistemas modernos no viven aislados: requieren bases de datos, cachés y proxies.
> Hoy aprenderemos a utilizar **Docker Compose** para orquestar y definir aplicaciones multi-contenedor en un único archivo declarativo."

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar la portada oficial del curso y recordar la ruta del repositorio en GitHub: `https://github.com/Crsitian22/docker-desde-cero-pit`.

**💡 Tip de Gestión del Aula:**
- Preguntar al grupo: *"¿Cuántos de ustedes han tenido que levantar a mano una app y su base de datos abriendo 3 o 4 terminales diferentes?"*

---

### 📄 Diapositiva 2: SESIÓN 3 — Índice del Temario
**Contenido de la PPT:**
```text
SESIÓN 3
1. Orquestación Local
2. Estructura del docker-compose.yml
3. Comandos de Compose
4. Integración Flask + PostgreSQL
5. Red Interna y Servicios
6. Variables de Entorno
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los 6 ejes temáticos de esta tercera sesión:
> 1. En **Orquestación Local**, entenderemos por qué el comando `docker run` imperativo se vuelve insostenible en stacks complejos.
> 2. En la **Estructura del docker-compose.yml**, analizaremos el formato YAML y sus bloques principales (`services`, `networks`, `volumes`).
> 3. Practicaremos los **Comandos de Compose**: `up -d`, `ps`, `logs`, `exec` y `down`.
> 4. Desarrollaremos la **Integración Flask + PostgreSQL**.
> 5. Explicaremos cómo funciona la **Red Interna y Servicios** (DNS interno por nombre).
> 6. Y finalmente, segregaremos las credenciales usando **Variables de Entorno** con `.env`."

**👨‍💻 Acción en Consola / Pizarra:**
- Anotar en la pizarra el mapa conceptual: `código + compose.yml + .env -> docker compose up -d -> Stack Completo`.

**💡 Tip de Gestión del Aula:**
- Mencionar que Docker Compose es el paso obligado antes de aprender orquestadores de producción a mayor escala como Kubernetes.

---

### 📄 Diapositiva 3: Objetivo de la Sesión 3
**Contenido de la PPT:**
```text
Objetivo de la sesión 3:
Al terminar la sesión 3 podrás:
• Explicar para qué sirve Docker Compose.
• Levantar proyectos reales con múltiples servicios.
• Entender la estructura de docker-compose.yml.
• Conectar una aplicación Flask con PostgreSQL.
• Configurar variables de entorno usando archivo .env.
• Ejecutar, revisar y detener un stack completo con Compose.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Nuestro **Objetivo de la Sesión 3** es muy concreto:
> Al finalizar la clase, cada estudiante sabrá redactar un archivo `docker-compose.yml`, levantar en un solo comando una arquitectura web conectada a una base de datos PostgreSQL, entenderá cómo se comunican internamente por nombre de servicio y sabrá controlar todo el ciclo de vida del stack con `docker compose up` y `down`."

**👨‍💻 Acción en Consola / Pizarra:**
- Destacar el concepto de **DECLARATIVO**: En lugar de ejecutar comandos manuales uno a uno, le describimos a Docker el estado final deseado en un YAML.

**💡 Tip de Gestión del Aula:**
- Resaltar que hoy se conectarán dos contenedores entre sí por primera vez en el curso.

---

### 📄 Diapositiva 4: Bloque 1 — Docker Compose
**Contenido de la PPT:**
```text
Docker Compose
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Iniciamos el **Bloque 1: Docker Compose**. Vamos a abordar la problemática de gestionar arquitecturas distribuidas y cómo Compose nos simplifica la vida."

**👨‍💻 Acción en Consola / Pizarra:**
- Transición visual hacia la problemática de ejecutar múltiples comandos `docker run`.

**💡 Tip de Gestión del Aula:**
- Enfatizar la diferencia entre desarrollo imperativo (comandos sueltos) vs desarrollo declarativo (archivo YAML).

---

### 📄 Diapositiva 5: El problema: una app ya no vive sola
**Contenido de la PPT:**
```text
El problema: una app ya no vive sola
• Una app real suele necesitar base de datos, caché, proxy o workers.
• Ejecutar cada contenedor a mano vuelve el laboratorio repetitivo.
• Los comandos docker run crecen con puertos, redes, volúmenes y variables.
• El equipo necesita una forma reproducible de levantar todo el stack.

PREGUNTA CLAVE: ¿Cómo describimos una aplicación completa, no solo un contenedor?
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Analicemos **El Problema**:
> En el software moderno, una aplicación web casi nunca trabaja aislada. Necesita una base de datos (PostgreSQL), un caché en memoria (Redis), un proxy inverso (Nginx) y colas de tareas.
> Intentar levantar esto con comandos `docker run` individuales exige crear redes manuales, recordar contraseñas, mapear puertos y ejecutar 5 o 6 comandos en un orden estricto. Si un nuevo programador llega al equipo, tardará horas en replicar el entorno.
> **La pregunta clave es:** *¿Cómo describimos toda la arquitectura de la aplicación en un solo lugar reproducible?*"

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar en la pizarra el caos de ejecutar 4 terminales con `docker run` vs un único archivo `compose.yml`.

**💡 Tip de Gestión del Aula:**
- Pausa activa: Preguntar si a algún alumno se le ha olvidado un flag en un `docker run` y ha tenido que borrar el contenedor para volver a empezar.

---

### 📄 Diapositiva 6: ¿Qué es Docker Compose?
**Contenido de la PPT:**
```text
¿QUÉ ES DOCKER COMPOSE?
DEFINICIÓN PRÁCTICA:
Docker Compose permite definir y ejecutar aplicaciones multi-contenedor usando un archivo YAML versionable.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Definición Práctica de Docker Compose**:
> **Docker Compose es la herramienta oficial de Docker que permite definir, configurar y ejecutar aplicaciones compuestas por múltiples contenedores mediante un único archivo manifest escrito en formato YAML**.
> Al ser un archivo de texto (`compose.yml`), se puede guardar en el repositorio Git del proyecto, versionando la infraestructura de desarrollo junto con el código fuente."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir la equivalencia en la pizarra: `Docker Compose = Infraestructura como Código (IaC) para entornos locales y de pruebas`.

**💡 Tip de Gestión del Aula:**
- Subrayar que Compose viene preinstalado en Docker Desktop y disponible como plugin (`docker compose`) en Linux.

---

### 📄 Diapositiva 7: De docker run a docker compose
**Contenido de la PPT:**
```text
DE DOCKER RUN A DOCKER COMPOSE

Sin Compose (Imperativo y propenso a errores):
docker network create app-net
docker run -d --name db --network app-net postgres:16
docker run -d --name web --network app-net -p 5000:5000 mi-flask:v3

Con Compose (Declarativo y en 1 solo paso):
docker compose up -d
docker compose ps
docker compose down
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Comparemos los dos enfoques en pantalla:
> - **Sin Compose (Modo Imperativo):** Tienes que crear la red con `docker network create`, luego levantar la BD en esa red con `docker run`, luego compilar la app y levantarla en la misma red mapeando puertos. Si cometes un error en un argumento, debes destruir todo y empezar de nuevo.
> - **Con Compose (Modo Declarativo):** Defines la red y los dos servicios en `compose.yml`. Para encender la infraestructura completa solo ejecutas `docker compose up -d`. Para verificar ejecutas `docker compose ps`. Y para apagar y limpiar todo ejecutas `docker compose down`. Un solo comando controla toda la arquitectura."

**👨‍💻 Acción en Consola / Pizarra:**
- Resaltar en la pizarra: `3 comandos imperativos manuales  VS  1 solo comando: docker compose up -d`.

**💡 Tip de Gestión del Aula:**
- Preguntar a los alumnos si ven la enorme ventaja en productividad que esto representa para sus equipos de trabajo.

---

### 📄 Diapositiva 8: Bloque 2 — Estructura de compose.yml
**Contenido de la PPT:**
```text
Estructura de compose.yml
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Entramos al **Bloque 2: Estructura del docker-compose.yml**. Vamos a aprender la sintaxis de los archivos YAML y los bloques principales que los componen."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra las 3 claves del YAML: Indentación con espacios, llaves tipo clave-valor y listas con guion `-`.

**💡 Tip de Gestión del Aula:**
- Recordar que en YAML está **estrictamente prohibido usar tabuladores**; siempre se usan espacios en blanco (2 espacios por nivel).

---

### 📄 Diapositiva 9: Piezas principales de Compose
**Contenido de la PPT:**
```text
PIEZAS PRINCIPALES DE COMPOSE
IDEA MENTAL:
Compose describe la topología local: qué servicios existen, cómo se conectan y qué datos conservan.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Grábense esta **Idea Mental**:
> El archivo Compose describe la **topología completa de su sistema local**:
> 1. `services:` Define qué contenedores van a correr (web, base de datos, caché).
> 2. `networks:` Define cómo se comunican esos contenedores de forma aislada.
> 3. `volumes:` Define qué datos se deben conservar de forma permanente en el disco duro del host."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar el mapa de bloques YAML:
  ```text
  services:    (Los procesos)
  networks:    (Los cables virtuales)
  volumes:     (Los discos persistentes)
  ```

**💡 Tip de Gestión del Aula:**
- Verificar que la diferencia entre servicios, redes y volúmenes quede clara antes de ver el código YAML real.

---

### 📄 Diapositiva 10: docker-compose.yml mínimo
**Contenido de la PPT:**
```text
DOCKER-COMPOSE.YML MÍNIMO
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: appdb
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppass

LECTURA RÁPIDA:
web construye la app desde la carpeta actual.
db usa la imagen oficial de PostgreSQL 16.
Compose crea una red interna por defecto automáticamente.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Leamos paso a paso este `docker-compose.yml` mínimo:
> - `services:` Abre la lista de nuestros contenedores.
> - `web:` Nombre del primer servicio.
>   - `build: .` Le dice a Compose que compile la imagen buscando el `Dockerfile` en la carpeta actual (`.`).
>   - `ports: - "5000:5000"` Mapea el puerto 5000 del host al 5000 del contenedor.
>   - `depends_on: - db` Indica que el servicio `db` debe arrancar antes que `web`.
> - `db:` Nombre del segundo servicio.
>   - `image: postgres:16` Descarga la imagen oficial de PostgreSQL versión 16.
>   - `environment:` Define las variables de inicialización necesarias para crear la base de datos, usuario y clave.
>
> **Detalle clave:** No declaramos la sección `networks:` porque Docker Compose crea automáticamente una red bridge privada dedicada exclusivamente a este proyecto."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar la estructura YAML con resaltado de sintaxis en el VS Code.

**💡 Tip de Gestión del Aula:**
- Explicar por qué los puertos van entre comillas `"5000:5000"`: en YAML la notación sin comillas puede ser interpretada como número base 60.

---

### 📄 Diapositiva 11: Comandos esenciales de Compose
**Contenido de la PPT:**
```text
COMANDOS ESENCIALES DE COMPOSE
| COMANDO | PARA QUÉ SIRVE | USO / SOLUCIÓN RÁPIDA |
|---|---|---|
| docker compose up -d | Levanta el stack en segundo plano | Iniciar laboratorio |
| docker compose ps | Lista servicios del proyecto | Ver estado |
| docker compose logs -f | Muestra logs integrados | Diagnóstico de errores |
| docker compose exec web sh | Abre una shell interactiva en el servicio | Debugging interno |
| docker compose down | Detiene y elimina contenedores/redes | Limpiar el stack |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los 5 **Comandos Esenciales de Docker Compose**:
> 1. **`docker compose up -d`:** Compila (si es necesario), crea las redes/volúmenes y enciende todos los servicios en segundo plano (`-d`).
> 2. **`docker compose ps`:** Muestra la lista de servicios del stack actual, sus puertos e IPs.
> 3. **`docker compose logs -f`:** Muestra la consola combinada de TODOS los contenedores en tiempo real (pueden filtrar uno solo con `docker compose logs -f web`).
> 4. **`docker compose exec web sh`:** Ingresa a la terminal dentro del contenedor `web` activo.
> 5. **`docker compose down`:** Detiene y destruye los contenedores y redes creadas por este Compose de forma limpia."

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar la tabla durante unos instantes para que los estudiantes anoten la sintaxis del comando V2 (`docker compose` con espacio).

**💡 Tip de Gestión del Aula:**
- Aclarar que en versiones antiguas se usaba `docker-compose` (con guion), pero la versión moderna V2 integrada en Docker CLI usa `docker compose` (con espacio).

---

### 📄 Diapositiva 12: Dependencias entre servicios
**Contenido de la PPT:**
```text
DEPENDENCIAS ENTRE SERVICIOS
REGLA PRÁCTICA: Arrancar antes no significa estar listo para recibir tráfico.

• depends_on define el orden de arranque básico.
• NO garantiza que la base de datos ya acepte conexiones SQL.
• Para laboratorios robustos o producción se usan healthchecks.
• En esta sesión nos enfocamos en levantar y conectar el stack.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Atención con esta **Regla Práctica sobre `depends_on`**:
> `depends_on` indica a Docker Compose qué contenedor debe encender primero. Por ejemplo, enciende `db` antes que `web`.
> PERO **arrancar antes no significa estar listo para recibir tráfico SQL**. PostgreSQL tarda un par de segundos en inicializar sus sockets internos. Si la app Flask intenta conectarse en el milisegundo 0, la conexión fallará.
> Para solucionar esto en entornos profesionales usamos **Healthchecks** (controles de salud), tema que profundizaremos en la Sesión 4. Por hoy, nos aseguraremos de que nuestro código en Flask reintente la conexión."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `depends_on = Orden de encendido del contenedor` | `Healthcheck = Confirmación de que el servicio está LISTO`.

**💡 Tip de Gestión del Aula:**
- Preguntar si comprenden la diferencia entre que un contenedor esté en estado `running` vs que su base de datos esté aceptando consultas.

---

### 📄 Diapositiva 13: Bloque 3 — Flask + PostgreSQL
**Contenido de la PPT:**
```text
Flask + PostgreSQL
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 3: Integración Flask + PostgreSQL**. Vamos a ver cómo se conecta nuestra aplicación web en Python con un motor de base de datos relacional."

**👨‍💻 Acción en Consola / Pizarra:**
- Diagramar en la pizarra el flujo de datos: `Navegador -> Flask (puerto 5000) -> Driver psycopg2 -> PostgreSQL (puerto 5432)`.

**💡 Tip de Gestión del Aula:**
- Verificar que los alumnos entiendan la necesidad del driver `psycopg2-binary` en el archivo `requirements.txt`.

---

### 📄 Diapositiva 14: Arquitectura del laboratorio
**Contenido de la PPT:**
```text
ARQUITECTURA DEL LABORATORIO
CLAVE DE RED INTERNA:
Dentro de Compose, la app NO se conecta a localhost; se conecta al nombre del servicio: db.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Clave de Red Interna** de la clase de hoy:
> Cuando ejecutamos múltiples contenedores bajo Compose, **la aplicación web Flask NO debe intentar conectarse a `localhost` para llegar a PostgreSQL**.
> Dentro de un contenedor, `localhost` (o `127.0.0.1`) apunta a la propia interfaz loopback del mismo contenedor Flask.
> En su lugar, Flask debe conectarse utilizando el hostname del **nombre del servicio** definido en el YAML: **`db`**.
> El servidor DNS interno de Docker interceptará la solicitud a `db` y la resolverá automáticamente hacia la IP privada del contenedor de la base de datos."

**👨‍💻 Acción en Consola / Pizarra:**
- Ilustrar la resolución DNS en la pizarra:
  `Contenedor Web busca 'db' ---> DNS Interno de Docker (127.0.0.11) ---> Responde con IP 172.18.0.3 (Contenedor DB)`.

**💡 Tip de Gestión del Aula:**
- Reiterar este concepto tres veces: es el error número 1 de todos los alumnos en la Sesión 3.

---

### 📄 Diapositiva 15: Variables de conexión en Flask
**Contenido de la PPT:**
```text
VARIABLES DE CONEXIÓN EN FLASK
import os

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD")

POR QUÉ USAR VARIABLES:
• Evitan hardcodear credenciales en el código fuente.
• Permiten cambiar de entorno (Dev, QA, Prod) sin tocar código.
• Funcionan perfectamente integradas con .env y Compose.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos cómo se programa esto en Python con buenas prácticas:
> Usamos la librería estándar `os` para leer las variables de entorno mediante `os.getenv()`.
> Fíjense en `os.getenv("DB_HOST", "db")`: intenta leer la variable `DB_HOST`, y si no está definida, toma por defecto `"db"`.
> **Ventajas de usar variables de entorno:**
> 1. No dejamos contraseñas ni nombres de servidor quemados en el código de Python.
> 2. Podemos pasar del entorno de desarrollo al de producción cambiando solo las variables, sin modificar una sola línea del programa."

**👨‍💻 Acción en Consola / Pizarra:**
```python
# app.py
import os, psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST', 'db'),
        database=os.getenv('POSTGRES_DB', 'appdb'),
        user=os.getenv('POSTGRES_USER', 'appuser'),
        password=os.getenv('POSTGRES_PASSWORD', 'apppass')
    )
    return conn
```

**💡 Tip de Gestión del Aula:**
- Mostrar lo limpio que resulta cambiar parámetros de conexión sin editar archivos `.py`.

---

### 📄 Diapositiva 16: Compose para Flask + PostgreSQL
**Contenido de la PPT:**
```text
COMPOSE PARA FLASK + POSTGRESQL
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: ${DB_NAME}
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Analicemos la estructura completa de nuestro `compose.yml` para este laboratorio:
> - En `web`: Compila el Dockerfile local (`build: .`), expone el puerto `5000:5000` a nuestra laptop y depende de `db`.
> - En `db`: Utiliza la imagen `postgres:16` e inyecta las variables de credenciales leídas desde nuestro archivo de entorno mediante la sintaxis `${VARIABLE}`.
> - **Persistencia:** En `db` añadimos un montaje de volumen `postgres_data:/var/lib/postgresql/data` y lo declaramos en la sección `volumes:`. Esto garantiza que aunque detengamos los contenedores, los datos de la base de datos NO se perderán."

**👨‍💻 Acción en Consola / Pizarra:**
- Explicar la directiva `${VARIABLE}`: Compose sustituye esa expresión por el valor que encuentra en el archivo `.env`.

**💡 Tip de Gestión del Aula:**
- Señalar la sección `volumes:` en la parte inferior del archivo YAML.

---

### 📄 Diapositiva 17: Bloque 4 — Variables de entorno
**Contenido de la PPT:**
```text
Variables de entorno
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Entramos al **Bloque 4: Variables de entorno**. Vamos a revisar cómo utilizar archivos `.env` y las mejores prácticas para no exponer contraseñas en Git."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `.env` (Secretos Locales) vs `.env.example` (Plantilla pública en Git).

**💡 Tip de Gestión del Aula:**
- Recordar a los alumnos agregar `.env` en su archivo `.gitignore`.

---

### 📄 Diapositiva 18: Archivo .env del proyecto
**Contenido de la PPT:**
```text
ARCHIVO .ENV DEL PROYECTO
# Archivo .env
DB_HOST=db
DB_NAME=appdb
DB_USER=appuser
DB_PASSWORD=appsecret
FLASK_ENV=development

IMPORTANTE:
No subas .env con credenciales reales a GitHub.
Usa .env.example para documentar las variables esperadas sin secretos.

PARA CLASE:
Usaremos valores simples de laboratorio para entender el flujo.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "El archivo **`.env`** es un archivo de texto plano clave-valor ubicado en la misma carpeta que `compose.yml`.
> Docker Compose detecta y lee automáticamente este archivo al ejecutar `docker compose up`.
> **Regla de Seguridad de la UNI:**
> **Jamás suban el archivo `.env` con credenciales reales a sus repositorios de GitHub**.
> En su lugar, creen y suban un archivo llamado **`.env.example`** con los nombres de las variables pero sin las contraseñas reales. Así cualquier colaborador sabrá qué variables necesita configurar en su propio entorno."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
# Archivo .env.example (En Git):
DB_HOST=db
DB_NAME=
DB_USER=
DB_PASSWORD=

# Archivo .env (LOCAL, en .gitignore):
DB_HOST=db
DB_NAME=appdb
DB_USER=appuser
DB_PASSWORD=SuperSecreta123!
```

**💡 Tip de Gestión del Aula:**
- Verificar que todos comprendan la diferencia entre `.env` (local/secreto) y `.env.example` (público/plantilla).

---

### 📄 Diapositiva 19: .env vs environment
**Contenido de la PPT:**
```text
.ENV VS ENVIRONMENT
| OPCIÓN | VENTAJAS | CUÁNDO USARLA |
|---|---|---|
| environment | Visible en el YAML | Valores simples o explícitos |
| env_file | Separa configuración | Variables por entorno |
| .env.example | Documenta sin secretos | Repositorios compartidos |
| Secret manager | Mejor seguridad | Producción real |

REGLA PRÁCTICA: El archivo .env ayuda en desarrollo; no es una bóveda de secretos para producción real.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos las opciones para manejar variables en Compose:
> 1. **`environment` (en el YAML):** Útil para valores fijos o para mapear variables del sistema.
> 2. **`env_file:` (en el YAML):** Carga un archivo `.env` completo directamente en el servicio.
> 3. **`.env.example`:** Indispensable en repositorios Git compartidos.
> 4. **Secret Manager (HashiCorp Vault, AWS Secrets):** Es la solución definitiva en producción real.
> **Regla Práctica:** `.env` es una solución genial para desarrollo local; en producción se usan secret managers o variables inyectadas por el sistema de CI/CD."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar la tabla comparativa en pantalla.

**💡 Tip de Gestión del Aula:**
- Preguntar si tienen alguna duda sobre cómo Compose sustituye las variables antes de iniciar el laboratorio.

---

### 📄 Diapositiva 20: Bloque 5 — Laboratorio multi-contenedor
**Contenido de la PPT:**
```text
Laboratorio multi-contenedor
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 5: Laboratorio multi-contenedor**. Vamos a poner las manos en la masa y levantar todo el stack con un solo comando."

**👨‍💻 Acción en Consola / Pizarra:**
- Abrir la terminal y verificar que estamos en `codigo/sesion3`.

**💡 Tip de Gestión del Aula:**
- Asegurarse de que todos los alumnos hayan creado su archivo `.env` copiando el `.env.example`.

---

### 📄 Diapositiva 21: Flujo del laboratorio
**Contenido de la PPT:**
```text
FLUJO DEL LABORATORIO
META:
Ejecutar una aplicación Flask conectada a PostgreSQL usando un solo archivo Compose.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Nuestra **Meta del Laboratorio**:
> Vamos a posicionarnos en `codigo/sesion3`, copiaremos `.env.example` a `.env`, ejecutaremos `docker compose up -d --build`, verificaremos los servicios con `docker compose ps`, revisaremos los logs con `docker compose logs -f` y probaremos la conexión a la base de datos desde el navegador web."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar los archivos en el explorador: `app.py`, `requirements.txt`, `Dockerfile`, `docker-compose.yml`, `.env.example`.

**💡 Tip de Gestión del Aula:**
- Pedir a los alumnos que abran la terminal integrada de VS Code.

---

### 📄 Diapositiva 22: Comandos del laboratorio Compose
**Contenido de la PPT:**
```text
COMANDOS DEL LABORATORIO COMPOSE
# 1. Levantar el stack
docker compose up -d --build

# 2. Revisar servicios
docker compose ps

# 3. Ver logs integrados
docker compose logs -f

# 4. Probar la app
curl http://localhost:5000

# 5. Entrar al servicio web
docker compose exec web sh

# 6. Detener y limpiar
docker compose down
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos juntos los 6 pasos del laboratorio:
> 1. Copien la plantilla `.env`: `cp .env.example .env` (o `Copy-Item .env.example .env` en PowerShell).
> 2. Levanten el stack reconstruyendo la imagen: `docker compose up -d --build`.
> 3. Verifiquen que los dos servicios (`web` y `db`) estén activos: `docker compose ps`.
> 4. Inspeccionen las bitácoras: `docker compose logs -f`. Verán los mensajes de PostgreSQL y Flask.
> 5. Prueben la aplicación en su navegador en `http://localhost:5000`. Debe devolver la versión de PostgreSQL consultada con éxito.
> 6. Prueben ingresar al contenedor `web` con `docker compose exec web sh`.
> 7. Al terminar, apaguen el stack con `docker compose down`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
cp .env.example .env
docker compose up -d --build
docker compose ps
curl http://localhost:5000
docker compose down
```

**💡 Tip de Gestión del Aula:**
- Guiar a los alumnos que reciben respuestas JSON en `http://localhost:5000` para que verifiquen el string `db_version`.

---

### 📄 Diapositiva 23: Errores frecuentes en Compose
**Contenido de la PPT:**
```text
ERRORES FRECUENTES EN COMPOSE
| ERROR | CAUSA PROBABLE | SOLUCIÓN RÁPIDA |
|---|---|---|
| App no conecta a BD | Usa localhost en vez de db | Cambiar host al nombre del servicio |
| Puerto ocupado | Otro proceso usa 5000 | Cambiar a 5001:5000 |
| Variables vacías | Falta .env o nombre incorrecto | Revisar env_file y claves en .env |
| BD pierde datos | No hay volumen persistente | Agregar volumen nombrado en el YAML |
| Cambios no aparecen | Imagen antigua en caché | Usar docker compose up -d --build |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos la tabla de **Resolución de Errores Frecuentes en Compose**:
> 1. **App no conecta a BD:** Es el error #1. Colocaron `host='localhost'` en Python. Solución: Cambiar a `host='db'`.
> 2. **Puerto ocupado:** El puerto 5000 ya está tomado en su laptop. Solución: Cambiar a `"5001:5000"` en la sección `ports:` del `compose.yml`.
> 3. **Variables vacías:** Se olvidaron de crear el archivo `.env`. Solución: Copiar `.env.example` a `.env`.
> 4. **Los cambios en el código Python no se reflejan:** Docker está usando la imagen anterior guardada en caché. Solución: Forzar el build con `docker compose up -d --build`."

**👨‍💻 Acción en Consola / Pizarra:**
- Resaltar la importancia del flag `--build` al ejecutar `docker compose up -d`.

**💡 Tip de Gestión del Aula:**
- Enseñar a leer los logs con `docker compose logs web` para identificar si la falla es de sintaxis Python o de red.

---

### 📄 Diapositiva 24: Checklist de aprendizaje — Sesión 3
**Contenido de la PPT:**
```text
CHECKLIST DE APRENDIZAJE — SESIÓN 3
✔ Puedo explicar para qué sirve Docker Compose.
✔ Puedo leer la estructura básica de docker-compose.yml.
✔ Puedo definir servicios, puertos, dependencias y volúmenes.
✔ Puedo conectar Flask con PostgreSQL usando el nombre del servicio.
✔ Puedo configurar variables con .env y env_file.
✔ Puedo levantar y detener un stack con docker compose up y down.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos nuestro **Checklist de Aprendizaje de la Sesión 3**:
> Hoy han aprendido la utilidad de Docker Compose, leen y redactan la estructura de un archivo `compose.yml`, definen servicios, puertos, dependencias y volúmenes, conectan aplicaciones web con bases de datos por nombre de servicio (`db`), gestionan credenciales de forma segura con `.env` y controlan stacks completos con `up` y `down`.
> ¡Un logro fundamental para su perfil técnico!"

**👨‍💻 Acción en Consola / Pizarra:**
- Marcar los 6 ticks en la pizarra haciendo énfasis en la conexión Flask-Postgres.

**💡 Tip de Gestión del Aula:**
- Felicitar a la clase por haber completado su primer proyecto multi-contenedor.

---

### 📄 Diapositiva 25: Resumen de la Sesión 3
**Contenido de la PPT:**
```text
RESUMEN DE LA SESIÓN 3
1. Compose describe aplicaciones multi-contenedor en un archivo YAML.
2. Los servicios se comunican por nombre dentro de la red del proyecto.
3. ports publica hacia la máquina host; la red interna usa nombres de servicio.
4. volumes permite conservar datos de PostgreSQL entre reinicios.
5. .env separa la configuración del código y del YAML.

PRÓXIMA SESIÓN:
Redes, volúmenes y persistencia: comunicación interna, almacenamiento y datos durables.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Sinteticemos las **5 Conclusiones Clave de la Sesión 3**:
> 1. Compose describe toda tu arquitectura distribuida en un único YAML.
> 2. Los contenedores se encuentran por su nombre de servicio vía DNS interno de Docker.
> 3. Usamos `ports` solo para lo que debe acceder el usuario desde su navegador; lo demás queda privado en la red interna.
> 4. Usamos `volumes` nombrados para que los datos de la base de datos no se borren.
> 5. Usamos `.env` para separar contraseñas del código.
>
> **En la Próxima Sesión (Sesión 4):** Profundizaremos en **Redes, Volúmenes y Persistencia**: aislamiento de red perimetral, backups automatizados con `pg_dump` y healthchecks de producción.
> ¡Muchas gracias por su atención y nos vemos en la Sesión 4!"

**👨‍💻 Acción en Consola / Pizarra:**
- Despedida de la sesión, recordar ingresar al aula virtual para resolver el cuestionario de evaluación de la Sesión 3.

**💡 Tip de Gestión del Aula:**
- Recordar a los alumnos resolver la evaluación de 12 preguntas correspondiente a la Sesión 3.
