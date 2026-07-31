# Guía Docente - Sesión 4: Persistencia de Datos, Redes y Backups (10ma Edición 2026)
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones - 10ma Edición
**Programa:** Programa de Iniciación Tecnológica (PIT) 2026 - OTI - UNI

---

## Perfil del Alumno y Enfoque Pedagógico
*Los alumnos sufren frecuentemente el desastre de perder datos cuando un contenedor de base de datos se detiene o destruye. En esta sesión enseñaremos la diferencia crítica entre el almacenamiento efímero del contenedor y la persistencia en disco usando **Volúmenes Nombrados** (*Named Volumes*) vs **Bind Mounts**. Además, implementaremos redes privadas cerradas y verificaciones de salud con **Healthchecks** para evitar errores de arranque.*

---

## 1. Planificación de la Clase (3 Horas)
*   **00:00 - 00:20 | Repaso:** Revisar la arquitectura Flask + PostgreSQL de la Sesión 3.
*   **00:20 - 01:10 | Bloques 1 & 2: Persistencia de Datos:** Naturaleza efímera de los contenedores. Volúmenes nombrados (`named volumes`) para producción vs Bind Mounts (`./codigo:/app`) para desarrollo.
*   **01:10 - 01:40 | Bloque 3: Aislamiento de Redes y Healthchecks:** Redes explícitas de Compose (`driver: bridge`). Ocultar la BD sin exporner el puerto 5432 al host. Verificación de salud con `pg_isready` y `condition: service_healthy`.
*   **01:40 - 01:55 | Receso / Break**
*   **01:55 - 02:40 | Bloque 4: Backup y Restauración de PostgreSQL:** Generación de dumps SQL con `docker compose exec -T db pg_dump` y restauración con `psql`.
*   **02:40 - 03:00 | Simulación de Desastres en Vivo y Tarea.**

---

## 2. Guión Paso a Paso del Docente

### Introducción
> **Guión Sugerido:**
> *"Hoy resolveremos la pregunta más importante del curso: ¿Qué pasa con los datos de mi base de datos cuando mi contenedor se destruye? Si no configuramos un volumen persistente, la información desaparece para siempre. Hoy aprenderemos a proteger los datos con Volúmenes Nombrados, a aislar la BD de internet y a realizar copias de respaldo automáticas."*

### Explicación del Temario

#### Bloque 1: Volúmenes Nombrados vs Bind Mounts
> **Guión Sugerido:**
> *"Un contenedor es por definición efímero. Al destruirse, su capa de escritura se elimina.
> - **Volumen Nombrado (`named volume`):** Es gestionado internamente por Docker en `/var/lib/docker/volumes/`. Es ultra rápido, seguro y es el estándar obligatorio para bases de datos en producción.
> - **Bind Mount:** Mapea una carpeta exacta de nuestro disco local (ej. `./app:/app`). Es ideal para entorno de desarrollo porque nos permite editar código en VS Code y ver los cambios reflejados al instante en el contenedor."*

#### Bloque 2: Healthcheck (Arranque síncrono garantizado)
> **Guión Sugerido:**
> *"El parámetro `depends_on` estándar solo espera a que el contenedor de la BD se encienda, pero la BD demora varios segundos en inicializar sus archivos de sistema. Para evitar que la app web falle al arrancar, añadimos un `healthcheck` en la BD usando `pg_isready` y en la app web indicamos `depends_on: db: { condition: service_healthy }`."*

---

## 3. Práctica en Consola Paso a Paso

#### Archivo `compose.yml` Profesional (Sesión 4)
```yaml
services:
  web:
    build: .
    container_name: app_web_s4
    ports:
      - "5000:5000"
    environment:
      - DB_HOST=db
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    networks:
      - red-interna
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:15-alpine
    container_name: app_db_s4
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - datos_postgres:/var/lib/postgresql/data
    networks:
      - red-interna
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 5s
      timeout: 5s
      retries: 5

networks:
  red-interna:
    driver: bridge

volumes:
  datos_postgres:
```

#### Comandos de Backup y Restore:
```bash
# 1. Generar Copia de Respaldo (Dump SQL)
docker compose exec -T db pg_dump -U admin_user posgrado_db > respaldo_backup.sql

# 2. Simular Desastre (Eliminar volumen)
docker compose down -v

# 3. Volver a levantar el stack
docker compose up -d

# 4. Restaurar Base de Datos desde el archivo SQL
docker compose exec -T db psql -U admin_user -d posgrado_db < respaldo_backup.sql
```

---

## 4. Gestión del Aula y Errores Frecuentes
*   **Pérdida accidental de datos al ejecutar `docker compose down -v`.** Advertir a los alumnos que el flag `-v` elimina los volúmenes persistentes. En producción solo debe usarse `docker compose down`.
