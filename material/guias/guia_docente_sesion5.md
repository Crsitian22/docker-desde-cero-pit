# 🎙️ Guía Docente Diapositiva por Diapositiva — Sesión 5: Docker en Producción
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Instructor:** Ing. Cristian Jampier Chileno Segundo | OTI - UNI  
**Programa:** Programa de Iniciación Tecnológica (PIT 2026) — Universidad Nacional de Ingeniería  
**Total Diapositivas:** 29 Diapositivas  

---

## 🎯 Instrucciones de Orientación Pedagógica
Esta guía contiene la explicación detallada y el guión profesional en primera persona para abordar **cada una de las 29 diapositivas** de la presentación oficial de la Sesión 5.
Está diseñada para guiar la clase paso a paso, enseñando a reforzar volúmenes y healthchecks, implementar Nginx como Reverse Proxy frontal en el puerto 8080, construir imágenes optimizadas mediante el patrón Multi-stage build, aislar credenciales seguras con `.env` y dominar la rutina de diagnóstico con `logs`, `inspect`, `exec` y `docker status/stats`.

---

## 🖥️ Explicación Diapositiva por Diapositiva (1 a 29)

### 📄 Diapositiva 1: DOCKER DESDE CERO: Crea y Despliega Aplicaciones — Sesión 5
**Contenido de la PPT:**
```text
DOCKER DESDE CERO: Crea y Despliega Aplicaciones
INSTRUCTOR: Cristian Jampier Chileno Segundo
PROGRAMA DE INICIACIÓN TECNOLÓGICA — PIT 2026
Oficina de Tecnologías de la Información (OTI - UNI)
Programa Completo — PIT 2026
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Muy buenos días/tardes a todos. Bienvenidos a la **Sesión 5** del curso *Docker desde Cero: Crea y Despliega Aplicaciones*, impartido por la OTI-UNI.
> Hoy daremos el salto decisivo hacia entornos de producción reales. Hasta ahora hemos trabajado con nuestra app expuesta directamente. Hoy colocaremos un servidor web **Nginx como Reverse Proxy** al frente en el puerto 8080, implementaremos imágenes ultraligeras con **Multi-stage builds**, aprenderemos a aislar credenciales y estableceremos una rutina profesional de monitoreo y logs."

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar la portada del curso y recordar la ruta del repositorio en GitHub: `https://github.com/Crsitian22/docker-desde-cero-pit`.

**💡 Tip de Gestión del Aula:**
- Preguntar al grupo: *"¿Por qué nunca deberíamos exponer un servidor web de desarrollo como Flask o Node directamente a internet sin un proxy como Nginx al frente?"*

---

### 📄 Diapositiva 2: SESIÓN 5 — Índice del Temario
**Contenido de la PPT:**
```text
SESIÓN 5
1. Reverse Proxy con Nginx
2. Configuración de Nginx
3. Multi-Stage Builds
4. Credenciales Seguras
5. Monitoreo y Logging
6. Integración del Stack
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los 6 ejes temáticos de esta quinta sesión:
> 1. En **Reverse Proxy con Nginx**, entenderemos la arquitectura de protección frontal.
> 2. En **Configuración de Nginx**, redactaremos el archivo `default.conf` con `proxy_pass`.
> 3. En **Multi-Stage Builds**, construiremos imágenes de producción descartando herramientas de compilación.
> 4. En **Credenciales Seguras**, revisaremos las reglas para evitar fugas de claves en repositorios.
> 5. En **Monitoreo y Logging**, practicaremos la secuencia de troubleshooting con `docker compose logs -f` y `docker stats`.
> 6. Y en **Integración del Stack**, levantaremos el laboratorio completo en `http://localhost:8080`."

**👨‍💻 Acción en Consola / Pizarra:**
- Anotar la arquitectura objetivo en la pizarra:
  `Navegador (:8080) -> [Nginx Proxy] <---Red Interna---> [Flask (:5000)] <---> [PostgreSQL (:5432)]`.

**💡 Tip de Gestión del Aula:**
- Señalar que esta sesión representa el estándar de arquitectura que se pide en puestos de DevOps Junior / SysAdmin.

---

### 📄 Diapositiva 3: Objetivo de la Sesión 5
**Contenido de la PPT:**
```text
Objetivo de la sesión 5:
Al terminar la sesión 5 podrás:
• Reforzar volúmenes, healthchecks, backup y restauración con práctica guiada.
• Configurar Nginx como reverse proxy delante de una app Flask.
• Optimizar una imagen con multi-stage builds.
• Separar credenciales y configuración usando variables de entorno.
• Revisar logs, estado, consumo y comportamiento de contenedores en ejecución.
• Integrar buenas prácticas mínimas para acercar el stack a producción.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Nuestro **Objetivo de la Sesión 5** es afianzar el perfil profesional:
> Al finalizar esta clase, cada uno de ustedes sabrá colocar un proxy Nginx delante de su aplicación web, retirará la exposición directa del puerto de Flask, compilará imágenes Multi-stage reducidas, manejará credenciales con `.env` sin exponer secretos y sabrá diagnosticar fallas inspeccionando métricas y bitácoras."

**👨‍💻 Acción en Consola / Pizarra:**
- Resaltar las palabras clave: **REVERSE PROXY**, **MULTI-STAGE**, **OBSERVABILIDAD**.

**💡 Tip de Gestión del Aula:**
- Generar motivación: *"Hoy convertiremos nuestro laboratorio en un stack listo para la nube"*.

---

### 📄 Diapositiva 4: Bloque 1 — Recuperación práctica
**Contenido de la PPT:**
```text
Recuperación práctica
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Iniciamos el **Bloque 1: Recuperación práctica**. Haremos un repaso dinámico de los 4 conceptos clave de la sesión anterior para asegurar que nadie tenga dudas antes de agregar Nginx."

**👨‍💻 Acción en Consola / Pizarra:**
- Listar los 4 puntos de repaso: Volúmenes, Bind Mounts, Healthchecks y Backup SQL.

**💡 Tip de Gestión del Aula:**
- Resolver preguntas rápidas del laboratorio anterior.

---

### 📄 Diapositiva 5: Qué nos faltó cerrar bien
**Contenido de la PPT:**
```text
Qué nos faltó cerrar bien
PENDIENTES DE LA SESIÓN ANTERIOR:
• Volúmenes nombrados para PostgreSQL.
• Diferencia real entre volumen y bind mount.
• Healthcheck de base de datos.
• Backup y restauración usando pg_dump y psql.

ENFOQUE DE HOY:
Explicación corta + Ejercicio inmediato + Validación con comandos + Corrección de errores frecuentes.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los pendientes de la sesión anterior que cerraremos con ejercicios relámpago:
> 1. Validaremos la persistencia real del volumen de PostgreSQL eliminando el contenedor con `down` y volviendo a levantar.
> 2. Revisaremos el estado del `healthcheck` con `docker inspect`.
> 3. Ejecutaremos el respaldo y restauración con `pg_dump`.
> Nuestro enfoque de hoy será: **Explicación corta -> Ejercicio inmediato -> Validación en consola -> Corrección de errores**."

**👨‍💻 Acción en Consola / Pizarra:**
- Explicar la metodología ágil de la clase de hoy.

**💡 Tip de Gestión del Aula:**
- Indicar que abran la carpeta `codigo/sesion5`.

---

### 📄 Diapositiva 6: Mapa del stack que usaremos hoy
**Contenido de la PPT:**
```text
MAPA DEL STACK QUE USAREMOS HOY
META DEL DÍA:
Convertir el stack Flask + PostgreSQL en un escenario más real: datos persistentes, salud verificable, proxy frontal, logs y monitoreo básico.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Este es el **Mapa del Stack de la Sesión 5**:
> Integramos 3 contenedores coordinados:
> - **`nginx`:** Escucha en el puerto `8080` de nuestra laptop y redirige el tráfico internamente.
> - **`web`:** Nuestra app Flask expuesta solo internamente en el puerto `5000`.
> - **`db`:** PostgreSQL 16 aislado perimetralmente con volumen nombrado `postgres_data` y Healthcheck `pg_isready`."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar el mapa completo en la pizarra resaltando que solo Nginx tiene puerto abierto hacia el Host (`8080:80`).

**💡 Tip de Gestión del Aula:**
- Verificar que la arquitectura completa sea comprendida antes de los ejercicios individuales.

---

### 📄 Diapositiva 7: Ejercicio 1: Volumen persistente para PostgreSQL
**Contenido de la PPT:**
```text
EJERCICIO 1: VOLUMEN PERSISTENTE PARA POSTGRESQL
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: appuser
      POSTGRES_PASSWORD: apppass
      POSTGRES_DB: appdb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:

VALIDACIÓN:
Levanta el stack, crea datos, ejecuta docker compose down, vuelve a levantar y verifica que los datos sigan existiendo.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos el **Ejercicio 1: Validación de Persistencia**:
> 1. Levanten el stack: `docker compose up -d`.
> 2. Entren al sitio web o inserten registros en la BD.
> 3. Ejecuten `docker compose down` (sin el flag `-v`).
> 4. Vuelvan a levantar con `docker compose up -d`.
> 5. Verifiquen que la información sigue almacenada gracias al volumen `postgres_data`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker compose up -d
curl http://localhost:5000/add
docker compose down
docker compose up -d
curl http://localhost:5000
```

**💡 Tip de Gestión del Aula:**
- Mostrar cómo el volumen nombrado `postgres_data` preserva el estado del sistema de archivos de PostgreSQL.

---

### 📄 Diapositiva 8: Ejercicio 2: Healthcheck de PostgreSQL
**Contenido de la PPT:**
```text
EJERCICIO 2: HEALTHCHECK DE POSTGRESQL
services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U appuser -d appdb"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

COMANDOS DE REVISIÓN:
docker compose ps
docker inspect --format '{{json .State.Health}}' <id_contenedor>
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos el **Ejercicio 2: Verificación de Salud**:
> Noten el atributo `start_period: 10s`: le da 10 segundos de gracia al contenedor para inicializar archivos antes de empezar a calificarlo.
> **Comando de inspección:**
> Ejecuten `docker compose ps` para ver si la columna STATUS indica `(healthy)`.
> Para ver el reporte JSON detallado, ejecuten:
> `docker inspect --format '{{json .State.Health}}' sesion5-db-1`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker compose ps
docker inspect --format '{{json .State.Health.Status}}' $(docker compose ps -q db)
```

**💡 Tip de Gestión del Aula:**
- Explicar la utilidad de `pg_isready` en scripts de automatización.

---

### 📄 Diapositiva 9: Ejercicio 3: Backup y restauración
**Contenido de la PPT:**
```text
EJERCICIO 3: BACKUP Y RESTAURACIÓN
# Backup
mkdir backups
docker compose exec -T db pg_dump     -U appuser appdb > backups/appdb.sql

# Restauración
docker compose exec -T db psql     -U appuser appdb < backups/appdb.sql

DIFERENCIA IMPORTANTE:
Volumen es persistencia local. Backup es una copia transportable que puede recuperarse incluso si el volumen se pierde.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos el **Ejercicio 3: Backup y Restauración**:
> Recuerden la gran diferencia:
> - **Volumen:** Es almacenamiento persistente en el servidor local.
> - **Backup:** Es una copia de seguridad en un archivo portable `.sql` que puedes enviar por correo, guardar en S3 o restaurar en otro servidor si el volumen local se corrompe.
> Ejecuten el backup con `pg_dump` y comprueben la creación del archivo `backups/appdb.sql`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
mkdir -p backups
docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql
ls -lh backups/appdb.sql
```

**💡 Tip de Gestión del Aula:**
- Verificar que ningún estudiante olvide el flag `-T`.

---

### Diapositiva 10: Bloque 2 — Nginx como reverse proxy
**Contenido de la PPT:**
```text
Nginx como reverse proxy
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 2: Nginx como Reverse Proxy**. Vamos a integrar Nginx como el único punto de entrada público a nuestra infraestructura."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar la arquitectura del Reverse Proxy en la pizarra.

**💡 Tip de Gestión del Aula:**
- Explicar qué es un Reverse Proxy: A diferencia de un Proxy directo (que oculta a los clientes), un Reverse Proxy oculta a los servidores backend.

---

### 📄 Diapositiva 11: Por qué usar un reverse proxy
**Contenido de la PPT:**
```text
POR QUÉ USAR UN REVERSE PROXY
REGLA PRÁCTICA: Publica Nginx hacia el host; deja Flask y PostgreSQL dentro de la red Docker.

• Centraliza el acceso externo a la aplicación.
• Permite ocultar servicios internos como web y db.
• En escenarios reales puede manejar TLS/SSL, headers, compresión y balanceo.
• En Compose, Nginx puede comunicarse con Flask usando el nombre del servicio (web).
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Analicemos **Por qué usar un Reverse Proxy**:
> 1. **Punto Único de Entrada:** Centraliza todas las peticiones entrantes en el puerto HTTP (80/8080) o HTTPS (443).
> 2. **Seguridad / Aislamiento:** Oculta la app Flask y la BD. Los clientes externos nunca interactúan directamente con el servidor WSGI de Python.
> 3. **Funcionalidades de Producción:** Nginx se encarga de los certificados SSL/TLS, compresión gzip, servir archivos estáticos (CSS/JS) a alta velocidad y realizar balanceo de carga.
> 4. **Resolución en Compose:** Nginx se conecta a Flask usando el nombre del servicio `http://web:5000`."

**👨‍💻 Acción en Consola / Pizarra:**
- Anotar la regla de oro: `Publicar SOLO Nginx hacia el Host (ports: 8080:80). Ocultar Flask y DB (expose/red interna)`.

**💡 Tip de Gestión del Aula:**
- Preguntar si los alumnos ven claro por qué esto evita exponer Flask en el puerto 5000.

---

### 📄 Diapositiva 12: Configuración mínima de Nginx
**Contenido de la PPT:**
```text
CONFIGURACIÓN MÍNIMA DE NGINX
# nginx/default.conf
server {
    listen 80;
    location / {
        proxy_pass http://web:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

LECTURA: proxy_pass http://web:5000 funciona porque web es resoluble dentro de la red Docker de Compose.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Inspeccionemos la configuración de Nginx en `nginx/default.conf`:
> - `listen 80;`: Indica que Nginx escuchará peticiones en el puerto 80 interno del contenedor.
> - `location / { ... }`: Captura todas las rutas recibidas.
> - `proxy_pass http://web:5000;`: Redirige de forma transparente la solicitud hacia el contenedor `web` en el puerto 5000.
> - `proxy_set_header`: Preserva la IP real del cliente y la cabecera Host original para que Flask sepa quién está haciendo la petición."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar en la pizarra el flujo del paquete HTTP:
  `Cliente -> Nginx (:80) --(proxy_pass http://web:5000)--> Flask (:5000)`.

**💡 Tip de Gestión del Aula:**
- Recomendar la lectura atenta de la línea `proxy_pass http://web:5000;`.

---

### 📄 Diapositiva 13: Agregar Nginx al docker-compose.yml
**Contenido de la PPT:**
```text
AGREGAR NGINX AL DOCKER-COMPOSE.YML
services:
  nginx:
    image: nginx:1.27-alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro
    depends_on:
      - web
  web:
    build: .
    expose:
      - "5000"

CAMBIO DE MENTALIDAD: web ya no necesita ports. Nginx es el servicio publicado hacia el host.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Observen este **Cambio de Mentalidad en Compose**:
> 1. Añadimos el servicio `nginx:` usando la imagen ligera `nginx:1.27-alpine`.
> 2. Mapeamos sus puertos hacia el host: `ports: - "8080:80"`.
> 3. Montamos nuestra configuración como de solo lectura (`:ro`): `- ./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro`.
> 4. **En el servicio `web` RETIRAMOS `ports:` y colocamos `expose: - "5000"`**. Ahora Flask ya NO es accesible directamente en `http://localhost:5000`; solo se puede acceder pasando por Nginx en `http://localhost:8080`."

**👨‍💻 Acción en Consola / Pizarra:**
- Resaltar la directiva `:ro` (Read Only) en el volumen de Nginx para evitar que el contenedor modifique la configuración.

**💡 Tip de Gestión del Aula:**
- Verificar que los alumnos comprendan por qué el puerto de la app cambia de 5000 a 8080 en el navegador.

---

### 📄 Diapositiva 14: Bloque 3 — Imágenes listas para producción
**Contenido de la PPT:**
```text
Imágenes listas para producción
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 3: Imágenes listas para producción**. Aprenderemos a optimizar el Dockerfile de Flask usando la compilación Multi-stage."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `Multi-stage = Etapa Builder + Etapa Runtime`.

**💡 Tip de Gestión del Aula:**
- Recordar la importancia de no incluir compiladores ni herramientas de dev en las imágenes finales de producción.

---

### 📄 Diapositiva 15: Qué problema resuelve multi-stage
**Contenido de la PPT:**
```text
QUÉ PROBLEMA RESUELVE MULTI-STAGE
IDEA CLAVE: Construir con una imagen completa, ejecutar con una imagen mínima.

• Para compilar o instalar dependencias a veces necesitamos herramientas pesadas.
• En producción solo necesitamos ejecutar la aplicación.
• Multi-stage permite copiar únicamente el resultado final.
• Reduce tamaño, superficie de ataque y tiempos de descarga.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Entendamos **Qué problema resuelve Multi-stage**:
> Para instalar dependencias en Python, Node o C++, los gestores de paquetes requieren instaladores, encabezados C y compiladores pesados. Pero una vez que las bibliotecas están instaladas o el binario está compilado, **esas herramientas ya no se necesitan para ejecutar la app**.
> Si dejamos esas herramientas dentro de la imagen final, estamos desperdiciando cientos de megabytes y dejando utilidades de compilación que un cibercriminal podría usar si vulnera la app.
> **La Idea Clave:** *Compilamos en una etapa pesada (`builder`) y copiamos únicamente el resultado final a una etapa ultraligera (`runtime`)*."

**👨‍💻 Acción en Consola / Pizarra:**
- Ilustrar la separación:
  - `Etapa 1 (builder):` Descarga dependencias, compila, pesa 800MB -> **SE DESCARDA**.
  - `Etapa 2 (runtime):` Copia solo las dependencias listasa `/root/.local`, pesa 120MB -> **IMAGEN FINAL DE PRODUCCIÓN**.

**💡 Tip de Gestión del Aula:**
- Hacer notar el impacto en los tiempos de despliegue en la nube.

---

### 📄 Diapositiva 16: Dockerfile multi-stage para Flask
**Contenido de la PPT:**
```text
DOCKERFILE MULTI-STAGE PARA FLASK
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.12-slim AS runtime
ENV PATH=/root/.local/bin:$PATH     PYTHONUNBUFFERED=1

WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Leamos el `Dockerfile.prod` Multi-stage profesional:
> - `FROM python:3.12-slim AS builder`: Etapa 1 llamada `builder`.
> - `RUN pip install --user --no-cache-dir -r requirements.txt`: El flag `--user` instala los paquetes dentro del directorio local del usuario `/root/.local`.
> - `FROM python:3.12-slim AS runtime`: Etapa 2 llamada `runtime` (será la imagen final).
> - `ENV PATH=/root/.local/bin:$PATH`: Agrega las librerías instaladas al PATH del sistema.
> - `COPY --from=builder /root/.local /root/.local`: **La magia de Multi-stage**. Copia únicamente la carpeta de paquetes instalados desde la etapa `builder`.
> - `COPY . .`: Copia el código fuente al final.
> - `CMD ["python", "app.py"]`: Ejecuta la app."

**👨‍💻 Acción en Consola / Pizarra:**
- Resaltar en la pizarra la instrucción `COPY --from=builder`.

**💡 Tip de Gestión del Aula:**
- Verificar que entiendan por qué la primera etapa se descarta automáticamente al terminar la compilación.

---

### 📄 Diapositiva 17: Ejercicio 4: Comparar imágenes
**Contenido de la PPT:**
```text
EJERCICIO 4: COMPARAR IMÁGENES
# Build normal
docker build -f Dockerfile -t flask-normal:v1 .

# Build multi-stage
docker build -f Dockerfile.prod -t flask-prod:v1 .

# Comparar tamaños
docker images | grep flask

PREGUNTA AL GRUPO: ¿La imagen más pequeña siempre es mejor?
No necesariamente: debe equilibrar tamaño, compatibilidad, seguridad y facilidad de mantenimiento.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos el **Ejercicio 4: Comparación de Tamaños**:
> Compilaremos la versión normal y la versión Multi-stage y revisaremos con `docker images | grep flask`.
> **Pregunta para el grupo:** *'¿Una imagen más pequeña es SIEMPRE la mejor opción?'*
> **Respuesta:** No necesariamente. Una imagen Alpine de 5MB puede ser diminuta pero si carece de `glibc` y provoca fallas intermitentes en producción, no conviene. La imagen ideal debe lograr un equilibrio óptimo entre **tamaño, seguridad, compatibilidad y facilidad de mantenimiento**."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker build -f Dockerfile -t flask-normal:v1 .
docker build -f Dockerfile.prod -t flask-prod:v1 .
docker images | grep flask
```

**💡 Tip de Gestión del Aula:**
- Mostrar en la terminal la diferencia de megabytes entre ambas versiones.

---

### 📄 Diapositiva 18: Bloque 4 — Credenciales y configuración segura
**Contenido de la PPT:**
```text
Credenciales y configuración segura
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 4: Credenciales y configuración segura**. Vamos a revisar los errores de seguridad más graves en la gestión de secretos."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `Seguridad = Nunca harcodear contraseñas ni subir .env a Git`.

**💡 Tip de Gestión del Aula:**
- Explicar qué son los bots de escaneo de credenciales en GitHub.

---

### 📄 Diapositiva 19: Qué no debe quedar dentro de la imagen
**Contenido de la PPT:**
```text
QUÉ NO DEBE QUEDAR DENTRO DE LA IMAGEN
EVITAR:
• Contraseñas dentro del Dockerfile.
• Tokens pegados en el código.
• Archivos .env copiados a la imagen.
• Credenciales subidas a GitHub.

PREFERIR:
• Variables de entorno en Compose.
• Archivo .env local excluido por Git.
• Secret managers en producción real.
• Rotación de credenciales cuando se exponen.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos las buenas prácticas de **Gestión de Credenciales**:
> **LO QUE NUNCA DEBEN HACER (EVITAR):**
> 1. Escribir contraseñas dentro del `Dockerfile` (ej. `ENV DB_PASS=secret123`).
> 2. Hardcodear tokens en archivos de código Python/Node.
> 3. Incluir el archivo `.env` en la instrucción `COPY . .` sin filtrarlo en `.dockerignore`.
> 4. Subir archivos `.env` a repositorios de GitHub.
>
> **LO QUE SIEMPRE DEBEN PREFERIR:**
> 1. Inyectar variables desde Compose.
> 2. Mantener `.env` únicamente en la máquina local y agregarlo a `.gitignore` y `.dockerignore`.
> 3. Usar gestores de secretos (AWS Secrets Manager, HashiCorp Vault, Kubernetes Secrets) en producción."

**👨‍💻 Acción en Consola / Pizarra:**
- Tachar en rojo en la pizarra: `ENV DB_PASSWORD=123` dentro del Dockerfile.

**💡 Tip de Gestión del Aula:**
- Preguntar qué hacer si por error subieron una clave a GitHub (Respuesta: Invalidate/rotate la clave inmediatamente, cambiarla en la BD).

---

### 📄 Diapositiva 20: Usar .env con Compose
**Contenido de la PPT:**
```text
USAR .ENV CON COMPOSE
# .env
POSTGRES_USER=appuser
POSTGRES_PASSWORD=apppass
POSTGRES_DB=appdb
FLASK_ENV=production

services:
  db:
    image: postgres:16
    env_file:
      - .env

IMPORTANTE: .env mejora la organización, pero no cifra secretos. En producción real se usan mecanismos de secretos o variables inyectadas por la plataforma.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Veamos cómo se usa la directiva **`env_file:`** en Compose:
> En lugar de listar las variables una a una en el YAML, podemos indicarle a Compose que cargue el archivo `.env` con la sintaxis:
> ```yaml
> env_file:
>   - .env
> ```
> **Aclaración importante:** El archivo `.env` organiza las variables en desarrollo local, pero **no las encripta**. En un entorno de producción real en la nube, las variables son inyectadas en memoria por la plataforma de orquestación."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar la sintaxis de `env_file:` en el archivo `docker-compose.yml`.

**💡 Tip de Gestión del Aula:**
- Verificar que entiendan la diferencia entre `environment:` (mapeo directo) y `env_file:` (carga de archivo externo).

---

### 📄 Diapositiva 21: Bloque 5 — Logging y monitoreo básico
**Contenido de la PPT:**
```text
Logging y monitoreo básico
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 5: Logging y monitoreo básico**. Vamos a aprender a auditar el comportamiento de los contenedores en ejecución."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra los 4 pilares de la observabilidad: `Estado`, `Logs`, `Recursos` e `Inspect`.

**💡 Tip de Gestión del Aula:**
- Presentar la rutina de diagnóstico profesional para resolver fallas.

---

### 📄 Diapositiva 22: Qué observar en un contenedor
**Contenido de la PPT:**
```text
QUÉ OBSERVABLE EN UN CONTENEDOR
| SEÑAL | PREGUNTA | COMANDO |
|---|---|---|
| Estado | ¿Está arriba o reiniciando? | docker compose ps |
| Logs | ¿Qué errores muestra la app? | docker compose logs -f |
| Recursos | ¿Consume mucha CPU/RAM? | docker stats |
| Configuración | ¿Qué red, variables y mounts tiene? | docker inspect |
| Proceso interno | ¿Qué pasa dentro del contenedor? | docker compose exec |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos la matriz de **Observabilidad de Contenedores**:
> 1. **Estado:** Para saber si está activo o ciclando en caídas, usamos `docker compose ps`.
> 2. **Logs:** Para leer excepciones o errores en tiempo real, usamos `docker compose logs -f <servicio>`.
> 3. **Recursos:** Para ver el consumo de memoria RAM y uso de CPU en vivo, usamos `docker stats`.
> 4. **Configuración:** Para ver montajes, variables e IPs asignadas, usamos `docker inspect <id>`.
> 5. **Proceso Interno:** Para navegar las carpetas internas del contenedor, usamos `docker compose exec <servicio> sh`."

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar la matriz y destacar el comando `docker stats`.

**💡 Tip de Gestión del Aula:**
- Explicar cómo `docker stats` permite detectar fugas de memoria (memory leaks) en tiempo real.

---

### 📄 Diapositiva 23: Comandos mínimos de diagnóstico
**Contenido de la PPT:**
```text
COMANDOS MÍNIMOS DE DIAGNÓSTICO
REGLA DE TROUBLESHOOTING:
Primero estado, luego logs, luego red/variables/mounts, y recién después modificar archivos.

Comandos:
docker compose ps
docker compose logs -f nginx
docker compose logs -f web
docker compose logs -f db
docker stats
docker compose exec web sh
docker inspect <contenedor>
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Regla Profesional de Troubleshooting (Resolución de Fallas)**:
> Cuando un sistema falla en producción, **NUNCA cambien el código a ciegas ni reinicien el servidor a lo loco**.
> Sigan siempre esta secuencia estricta:
> 1. Verificar estado (`docker compose ps`).
> 2. Leer las bitácoras de error (`docker compose logs -f <servicio>`).
> 3. Verificar consumo de hardware (`docker stats`).
> 4. Inspeccionar la configuración (`docker inspect`).
> 5. Probar conectividad interna (`docker compose exec web sh`).
> Solo después de identificar la causa raíz en los logs se procede a modificar archivos."

**👨‍💻 Acción en Consola / Pizarra:**
- Anotar los 5 pasos del protocolo de troubleshooting en la pizarra.

**💡 Tip de Gestión del Aula:**
- Hacer que los alumnos memoricen el orden: `ps -> logs -> stats -> inspect -> exec`.

---

### 📄 Diapositiva 24: Bloque 6 — Laboratorio de producción local
**Contenido de la PPT:**
```text
Laboratorio de producción local
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 6: Laboratorio de producción local**. Vamos a integrar todo el stack Nginx + Flask Multi-stage + PostgreSQL + Healthcheck + Backup."

**👨‍💻 Acción en Consola / Pizarra:**
- Abrir la terminal en la carpeta del laboratorio.

**💡 Tip de Gestión del Aula:**
- Indicar a los alumnos que preparen sus terminales para la ejecución final.

---

### 📄 Diapositiva 25: Flujo del laboratorio de Sesión 5
**Contenido de la PPT:**
```text
FLUJO DEL LABORATORIO DE SESIÓN 5
RESULTADO ESPERADO:
Acceder por http://localhost:8080, mantener PostgreSQL interno, validar salud, revisar logs y generar backup.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "NUESTRO **Resultado Esperado**:
> Vamos a levantar el stack completo, accederemos a la aplicación ingresando únicamente a `http://localhost:8080` (a través de Nginx), verificaremos que PostgreSQL está aislado sin puertos expuestos, auditaremos la salud del contenedor con `docker compose ps` y generaremos un archivo de backup SQL."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar la arquitectura final que se desplegará en la terminal.

**💡 Tip de Gestión del Aula:**
- Guiar a los alumnos paso a paso en la ejecución de los comandos.

---

### 📄 Diapositiva 26: Comandos del laboratorio
**Contenido de la PPT:**
```text
COMANDOS DEL LABORATORIO
# 1. Levantar todo
docker compose up -d --build

# 2. Validar servicios
docker compose ps

# 3. Probar desde navegador
# http://localhost:8080

# 4. Observar
docker compose logs -f nginx
docker compose logs -f web
docker stats

# 5. Backup final
docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos la secuencia del laboratorio de producción:
> 1. Levanten la infraestructura: `docker compose up -d --build`.
> 2. Verifiquen con `docker compose ps` que Nginx escucha en el puerto `8080` y `db` indica `(healthy)`.
> 3. Abran su navegador en `http://localhost:8080`.
> 4. Auditen los logs de Nginx y Flask: `docker compose logs -f nginx`.
> 5. Revisen el consumo en vivo con `docker stats`.
> 6. Ejecuten el backup final: `docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker compose up -d --build
docker compose ps
curl http://localhost:8080
docker stats --no-stream
mkdir -p backups
docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql
```

**💡 Tip de Gestión del Aula:**
- Celebrar el éxito del despliegue en el puerto 8080.

---

### 📄 Diapositiva 27: Errores frecuentes en Sesión 5
**Contenido de la PPT:**
```text
ERRORES FRECUENTES EN SESIÓN 5
| ERROR | CAUSA PROBABLE | SOLUCIÓN RÁPIDA |
|---|---|---|
| Nginx muestra 502 Bad Gateway | web no está listo o puerto incorrecto | Revisar logs de web y la línea proxy_pass |
| Flask no conecta a BD | Host configurado como localhost | Usar db como host |
| Healthcheck queda unhealthy | Usuario, BD o comando incorrecto | Probar pg_isready dentro de db |
| Datos desaparecen | Falta volumen o se usó down -v | Revisar volumes y docker volume ls |
| Variables no llegan | .env mal ubicado o nombre incorrecto | Revisar env_file y docker compose config |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos la tabla de **Resolución de Errores Frecuentes**:
> 1. **Nginx muestra `502 Bad Gateway`:** Significa que Nginx no pudo conectarse a Flask. Solución: Verifiquen que en `default.conf` la línea diga `proxy_pass http://web:5000;` y revisen los logs con `docker compose logs web`.
> 2. **Flask no conecta a BD:** Colocaron `localhost` en vez de `db`.
> 3. **Healthcheck en estado `unhealthy`:** La contraseña o nombre de usuario en `pg_isready` no coinciden con los del `.env`.
> 4. **Variables no llegan:** El archivo `.env` no está en la misma carpeta que `docker-compose.yml`."

**👨‍💻 Acción en Consola / Pizarra:**
- Dejar la tabla visible para la resolución de dudas.

**💡 Tip de Gestión del Aula:**
- Explicar la causa clásica del error HTTP 502 Bad Gateway en Nginx.

---

### 📄 Diapositiva 28: Checklist de aprendizaje — Sesión 5
**Contenido de la PPT:**
```text
CHECKLIST DE APRENDIZAJE — SESIÓN 5
✔ Puedo explicar por qué volumen y backup no son lo mismo.
✔ Puedo agregar un healthcheck y validar el estado healthy.
✔ Puedo poner Nginx como reverse proxy delante de Flask.
✔ Puedo dejar Flask y PostgreSQL como servicios internos.
✔ Puedo construir una imagen optimizada con multi-stage build.
✔ Puedo separar configuración mediante .env y variables de entorno.
✔ Puedo diagnosticar problemas con logs, ps, inspect, exec y stats.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos nuestro **Checklist de Aprendizaje de la Sesión 5**:
> Hoy han aprendido la diferencia entre volúmenes y backups, configuran Healthchecks de salud, colocan Nginx como Reverse Proxy frontal en puerto 8080, mantienen los servicios de aplicación y base de datos aislados internamente, compilan imágenes optimizadas con Multi-stage builds, manejan credenciales seguras y dominan la rutina de diagnóstico con `logs`, `ps`, `inspect`, `exec` y `stats`.
> ¡Un nivel técnico de producción excelente!"

**👨‍💻 Acción en Consola / Pizarra:**
- Marcar los 7 logros alcanzados en la clase.

**💡 Tip de Gestión del Aula:**
- Felicitar al grupo por el avance hacia prácticas reales de arquitectura DevOps.

---

### 📄 Diapositiva 29: Resumen de la Sesión 5
**Contenido de la PPT:**
```text
RESUMEN DE LA SESIÓN 5
1. Reforzamos persistencia con volúmenes y recuperación con backups.
2. Usamos healthchecks para distinguir running de healthy.
3. Configuramos Nginx como reverse proxy y punto de entrada del stack.
4. Aplicamos multi-stage builds para separar build y runtime.
5. Revisamos credenciales, variables, logs y monitoreo básico.
6. Integramos el stack en un escenario de producción local.

PRÓXIMA SESIÓN:
Proyecto final y despliegue completo: entornos dev/prod, limpieza, debugging profesional y ejecución con un solo comando.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Sinteticemos el **Resumen de la Sesión 5**:
> 1. Persistencia local con volúmenes y recuperabilidad externa con backups.
> 2. Observabilidad de salud con Healthchecks.
> 3. Seguridad y enrutamiento con Reverse Proxy Nginx.
> 4. Optimización de imágenes con Multi-stage builds.
> 5. Diagnóstico profesional de recursos y bitácoras.
>
> **En nuestra próxima y última sesión (Sesión 6):** Desarrollaremos el **Proyecto Final y Despliegue Completo**: separación de entornos (Desarrollo vs Producción con Compose Overrides), automatización con scripts de despliegue `desplegar.sh` y checklist de entrega del curso PIT 2026.
> ¡Muchas gracias por su esfuerzo y nos vemos en la Sesión 6!"

**👨‍💻 Acción en Consola / Pizarra:**
- Despedida de la clase, recordar resolver el cuestionario de evaluación de la Sesión 5.

**💡 Tip de Gestión del Aula:**
- Recordar ingresar al aula virtual para la evaluación correspondiente.
