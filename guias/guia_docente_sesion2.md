# Guía Docente - Sesión 2: Dockerfile Profesional, Capas y Buenas Prácticas (10ma Edición 2026)
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones - 10ma Edición
**Programa:** Programa de Iniciación Tecnológica (PIT) 2026 - OTI - UNI

---

## Perfil del Alumno y Enfoque Pedagógico
*Los estudiantes tienden a ver la instalación de software como una serie de comandos secuenciales ejecutados manualmente. El Dockerfile debe presentarse como Infraestructura como Código (IaC), inmutable, auditable y reproducible. En esta sesión introduciremos la optimización avanzada mediante la caché de capas de UnionFS, la diferencia crucial entre CMD y ENTRYPOINT, compilaciones Multi-Stage profesional para producción y la publicación en registros públicos (Docker Hub).*

---

## 1. Planificación de la Clase (3 Horas)
*   **00:00 - 00:20 | Repaso de Comandos:** Resolver dudas de la Sesión 1 y revisar tareas.
*   **00:20 - 01:10 | Bloques 1 & 2: Anatomía del Dockerfile e Instrucciones Clave:** Analizar FROM, WORKDIR, COPY, RUN, ENV, EXPOSE y CMD. Diferencia fundamental entre CMD vs ENTRYPOINT y el formato Exec (JSON) vs Shell.
*   **01:10 - 01:40 | Bloques 3 & 4: Capas, Caché de Build y Multistage Builds:** Cómo funciona UnionFS, cómo reordenar instrucciones para maximizar el uso de caché, `.dockerignore`, y la técnica Multi-Stage (`AS builder` -> `COPY --from=builder`).
*   **01:40 - 01:55 | Receso / Break**
*   **01:55 - 02:40 | Bloques 5 & 6: Distribución en Docker Hub y Laboratorio Optimizada:** `docker login`, `docker tag`, `docker push`, `docker pull`. Construcción y comparativa de peso entre imagen estándar e imagen optimizada en Alpine.
*   **02:40 - 03:00 | Trabajo para el Hogar, Evaluación Teórica y Q&A.**

---

## 2. Guión Paso a Paso del Docente

### Introducción
> **Guión Sugerido:**
> *"Buenas tardes. En la sesión de hoy aprenderemos a fabricar nuestras propias imágenes personalizadas con nivel profesional. Veremos cómo estructurar un Dockerfile para aprovechar la caché del motor y compilar en segundos, cómo usar bases ultra livianas en Alpine Linux para reducir el tamaño de 1 GB a 50 MB y cómo publicar nuestras imágenes en Docker Hub."*

### Explicación del Temario

#### Bloque 1: Anatomía del Dockerfile (Instrucciones clave)
> **Guión Sugerido:**
> *"Un Dockerfile es una receta declarativa. Cada línea representa un paso:
> - `FROM`: La imagen base sobre la cual construimos.
> - `WORKDIR`: El directorio de trabajo dentro del contenedor (evita usar `cd` manuales).
> - `COPY`: Copia archivos locales al contenedor.
> - `RUN`: Ejecuta comandos durante la **construcción** (*build*) para instalar paquetes.
> - `ENV`: Define variables de entorno permanentes.
> - `EXPOSE`: Documenta el puerto en el que la app escucha.
> - `CMD`: Define el comando que se ejecutará cuando el contenedor se **encienda** (*runtime*)."*

#### Bloque 2: ENTRYPOINT vs CMD (Sobrescribir rutinas en caliente)
> **Guión Sugerido:**
> *"ENTRYPOINT establece el ejecutable principal fijo (ej. `ping`), mientras que CMD entrega los argumentos por defecto (ej. `localhost`). Si el usuario ejecuta `docker run mi-imagen google.com`, el parámetro `google.com` sobrescribe a CMD pero mantiene ENTRYPOINT, ejecutando `ping google.com`.
> Regla de oro: Usar siempre la sintaxis de lista JSON (Exec Form): `CMD ["python", "app.py"]` en lugar de la forma shell `CMD python app.py` para garantizar el manejo correcto de señales de apagado Linux (SIGTERM)."*

#### Bloque 3: Capas, Caché y Reordenamiento inteligente
> **Guión Sugerido:**
> *"Docker utiliza un sistema de archivos en capas de solo lectura (UnionFS). Si cambias una sola línea de tu código, Docker invalida la caché de esa capa y de todas las siguientes.
> Mal diseño: Copiar todo el código (`COPY . /app`) e instalar dependencias (`RUN pip install`). En cada cambio de código, Docker reinstalará todo desde cero.
> Buen diseño: Copiar primero el archivo de requerimientos (`COPY requirements.txt /app/`), ejecutar la instalación (`RUN pip install`), y luego copiar el código fuente (`COPY . /app`). Si el requerimiento no cambió, la instalación se recupera instantáneamente de la caché."*

#### Bloque 4: Patrón Multi-Stage Build (El secreto de producción)
> **Guión Sugerido:**
> *"En desarrollo necesitamos compiladores y herramientas pesadas. En producción solo necesitamos los binarios ejecutables o el runtime mínimo.
> Multi-Stage Build nos permite crear múltiples etapas en el mismo Dockerfile:
> 1. Etapa `builder` (basada en `python:3.9-slim`): instala compiladores y descarga paquetes.
> 2. Etapa `final` (basada en `python:3.9-alpine`): copia solo la carpeta de librerías resultantes con `COPY --from=builder /root/.local /root/.local`.
> Resultado: Una imagen segura, sin herramientas de compilación que los hackers puedan explotar y de solo 50 MB de peso."*

---

## 3. Práctica en Consola Paso a Paso (Guía Visual)

1.  **Crear archivo `.dockerignore`:**
    ```text
    __pycache__/
    *.pyc
    .git/
    .env
    venv/
    ```

2.  **Dockerfile Estándar vs Multistage:**
    Escribir `Dockerfile.multistage` en `codigo/sesion2/`:
    ```dockerfile
    FROM python:3.9-slim AS builder
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install --user --no-cache-dir -r requirements.txt

    FROM python:3.9-alpine
    WORKDIR /app
    COPY --from=builder /root/.local /root/.local
    COPY app.py .
    ENV PATH=/root/.local/bin:$PATH
    EXPOSE 5000
    CMD ["python", "app.py"]
    ```

3.  **Compilar y Comparar Pesos:**
    `docker build -t flask-app:normal -f Dockerfile .`
    `docker build -t flask-app:optimizada -f Dockerfile.multistage .`
    `docker images | grep flask-app`
    `docker history flask-app:optimizada`

4.  **Publicar en Docker Hub:**
    `docker login`
    `docker tag flask-app:optimizada tu_usuario/mi-flask:v1.0`
    `docker push tu_usuario/mi-flask:v1.0`

---

## 4. Taller Práctico / Ejercicio del Alumno - Solucionario

### Ejercicio: Optimización de App Node.js o Python
Los alumnos deberán convertir un Dockerfile simple que pesa 900 MB en una versión Multi-stage basada en Alpine Linux que pese menos de 100 MB y publicarla en su cuenta personal de Docker Hub.

---

## 5. Gestión del Aula y Errores Frecuentes
*   **Error: Falta paquete de compilación en Alpine (`musl` vs `glibc`).** Solución: Instalar `gcc` o `musl-dev` en la etapa builder si la librería requiere compilación C de bajo nivel.
*   **Error: Docker Hub Denied (`denied: requested access to the resource is denied`).** Solución: Verificar que el tag tenga el prefijo exacto de su nombre de usuario de Docker Hub antes de hacer `push`.
