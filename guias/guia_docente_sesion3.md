# Guía Docente - Sesión 3: Orquestación Local con Docker Compose (10ma Edición 2026)
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones - 10ma Edición
**Programa:** Programa de Iniciación Tecnológica (PIT) 2026 - OTI - UNI

---

## Perfil del Alumno y Enfoque Pedagógico
*Los estudiantes ya dominan la creación de imágenes individuales, pero al enfrentarse a aplicaciones reales (Web + Base de Datos) intentan ejecutar múltiples comandos `docker run` conectándolos manualmente con IPs dinámicas. En esta sesión introduciremos Docker Compose como la herramienta estándar de orquestación local declarativa en YAML, destacando la resolución DNS interna por nombre de servicio y la gestión de secretos con archivos `.env`.*

---

## 1. Planificación de la Clase (3 Horas)
*   **00:00 - 00:20 | Repaso & Validación:** Revisión de imágenes subidas a Docker Hub en la Sesión 2.
*   **00:20 - 01:10 | Bloques 1 & 2: Anatomía de Docker Compose y Sintaxis YAML:** Conceptos de servicios, diferencia entre `image` y `build`, puertos (`ports`), variables de entorno (`environment`) y dependencias (`depends_on`).
*   **01:10 - 01:40 | Bloque 3: DNS Interno y Stack Web + PostgreSQL:** Cómo se comunican Flask y PostgreSQL usando el nombre del servicio `db` como hostname. Integración de variables de entorno mediante `.env`.
*   **01:40 - 01:55 | Receso / Break**
*   **01:55 - 02:40 | Bloques 4 & 5: Ciclo de Vida con la CLI de Compose:** Comandos `docker compose up -d`, `ps`, `logs -f`, `exec web python ...`, `down`.
*   **02:40 - 03:00 | Diagnóstico de Errores Frecuentes y Tarea para el Hogar.**

---

## 2. Guión Paso a Paso del Docente

### Introducción
> **Guión Sugerido:**
> *"Bienvenidos a la Sesión 3. Hasta hoy hemos trabajado con contenedores individuales. Pero en el mundo real, una aplicación nunca vive sola: requiere una base de datos, un caché o un servidor de mensajes. Ejecutar todo esto con comandos `docker run` individuales es caótico. Hoy aprenderemos a definir toda nuestra infraestructura en un solo archivo `compose.yml`."*

### Explicación del Temario

#### Bloque 1: ¿Por qué Docker Compose? (Infraestructura como Código)
> **Guión Sugerido:**
> *"Docker Compose nos permite declarar en un archivo YAML todos los servicios que componen nuestra arquitectura. En lugar de ejecutar 5 comandos `docker run` con parámetros larguísimos, simplemente ejecutamos `docker compose up -d` y el motor levanta toda la arquitectura en el orden correcto."*

#### Bloque 2: DNS Interno entre Servicios
> **Guión Sugerido:**
> *"Cuando Docker Compose levanta un proyecto, crea automáticamente una red privada. Dentro de esa red, los contenedores no se conectan por direcciones IP (que son dinámicas y cambian al reiniciar), sino **por el nombre del servicio** definido en el YAML.
> Si en `compose.yml` el servicio de base de datos se llama `db`, la app web se conectará a PostgreSQL utilizando `host="db"`. Docker resuelve internamente el nombre mediante su servidor DNS propio (127.0.0.11)."*

#### Bloque 3: Archivo `.env` y Seguridad de Credenciales
> **Guión Sugerido:**
> *"Nunca debemos colocar contraseñas ni credenciales de base de datos hardcodeadas dentro del `compose.yml` ni en el código Python. Creamos un archivo `.env` local y referenciamos las variables en el YAML con la sintaxis `${VARIABLE}`. El archivo `.env` debe incluirse obligatoriamente en `.gitignore`."*

---

## 3. Práctica en Consola Paso a Paso (Guía Visual)

Estructura en `codigo/sesion3/`:
- `app.py` (App Flask conectándose a PostgreSQL usando `psycopg2`)
- `requirements.txt` (`Flask==3.0.0`, `psycopg2-binary==2.9.9`, `python-dotenv==1.0.0`)
- `Dockerfile`
- `.env`
- `compose.yml`

```yaml
services:
  web:
    build: .
    container_name: flask_web
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=${DB_HOST}
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    container_name: postgres_db
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
```

Comandos de Ejecución:
1. `docker compose up -d`
2. `docker compose ps`
3. `docker compose logs -f`
4. `docker compose exec web python -c "import psycopg2; print('OK')"`
5. `docker compose down`

---

## 4. Gestión del Aula y Errores Frecuentes
*   **Error de sangría YAML (`yaml: line X: mapping values are not allowed here`).** Solución: Usar siempre 2 espacios de sangría y nunca tabuladores.
*   **Error de conexión inicial a BD (`psycopg2.OperationalError: could not connect to server`).** Solución: Explicar que la BD tarda unos segundos en iniciar en el primer arranque; se solucionará en la Sesión 4 con `healthcheck`.
