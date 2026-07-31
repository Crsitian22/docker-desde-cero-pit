# Guía Docente - Sesión 1: Contenedores desde Cero (10ma Edición 2026)
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones - 10ma Edición
**Programa:** Programa de Iniciación Tecnológica (PIT) 2026 - OTI - UNI

---

# 🌟 INTRODUCCIÓN PEDAGÓGICA AL CURSO: DE CERO A HÉROE EN DOCKER

### ¿Qué es Docker? (La explicación definitiva)
Imaginen que quieren enviar una carta y un regalo a un amigo en otro país. En lugar de enviarle las instrucciones de cómo armar el regalo, las piezas sueltas, y esperar que él tenga las herramientas correctas en su casa (lo cual podría fallar si le falta un destornillador específico), ustedes meten el regalo completamente armado y listo dentro de una caja estándar de cartón resistente.
Docker es esa caja. En el mundo del desarrollo de software, llamamos a esta caja **Contenedor**. Docker es la plataforma que nos permite empaquetar nuestro código fuente, junto con la versión exacta de la base de datos, librerías, variables de entorno y el sistema operativo mínimo que necesita para funcionar, todo dentro de una unidad ligera e inmutable llamada **Imagen**.

### ¿Cómo funciona por debajo?
A diferencia de las máquinas virtuales tradicionales que virtualizan el hardware físico y cargan un sistema operativo completo (con su propio Kernel pesado, controladores y servicios de fondo que consumen gigabytes de memoria), Docker comparte el mismo Kernel del sistema operativo anfitrión (Host).
Utiliza características nativas del kernel de Linux llamadas **Namespaces** (para aislar procesos, red, sistema de archivos y usuarios) y **Control Groups o cgroups** (para limitar y medir los recursos físicos asignados a cada contenedor, como RAM, CPU e I/O).

### ¿Para qué usar Docker? (Los beneficios reales)
1. **Portabilidad absoluta:** El famoso lema *"en mi máquina sí funciona"*. Si corre en tu laptop local, correrá exactamente igual en el servidor de producción.
2. **Arranque en milisegundos:** Al ser solo un proceso aislado y no un sistema operativo completo emulado, un contenedor prende y apaga en menos de un segundo.
3. **Ahorro masivo de infraestructura:** Puedes correr decenas de contenedores en el mismo servidor donde antes solo podías correr dos o tres máquinas virtuales.
4. **Facilidad de actualización:** Puedes cambiar o actualizar la versión de tu aplicación simplemente reemplazando el contenedor por uno nuevo en segundos, sin afectar el resto del servidor.

### 📈 El Camino de la Experiencia (Subiendo el nivel paso a paso)
*   **Paso 1 (Fundamentos):** Entender los comandos básicos para encender, apagar y listar contenedores existentes en la nube.
*   **Paso 2 (Empaquetamiento):** Aprender a escribir nuestras propias "recetas" (Dockerfiles) optimizando el peso y la caché de capas.
*   **Paso 3 (Orquestación local):** Unificar múltiples contenedores (Web + Base de datos) en un único archivo declarativo usando Docker Compose.
*   **Paso 4 (Persistencia y Redes):** Aislar las bases de datos de internet, configurar redes privadas seguras y realizar respaldos automatizados.
*   **Paso 5 (Producción y Hardening):** Colocar proxies inversos (Nginx), optimizar imágenes con compilaciones Multi-stage y limitar recursos RAM/CPU para prevenir caídas del servidor.
*   **Paso 6 (Automatización y Alta Disponibilidad):** Crear scripts Bash de despliegue continuo en caliente (`deploy.sh`) y balanceo distribuido en clústeres.

---

## Perfil del Alumno y Enfoque Pedagógico
*Los estudiantes son administradores de sistemas y desarrolladores junior que únicamente conocen arquitecturas tradicionales ("sistemas planos"): servidores físicos, máquinas virtuales clásicas (VMware, VirtualBox), instalación directa de dependencias locales y apertura manual de puertos de red. No poseen conocimientos previos sobre aislamiento a nivel de kernel. Es fundamental iniciar con la analogía del transporte físico de Malcolm McLean (1956) para conectar el problema del software "en mi máquina funciona" con una solución tangible.*

---

## 1. Planificación de la Clase (3 Horas)
*   **00:00 - 00:20 | Bienvenida e Índice de Contenidos:** Presentación del docente, del programa PIT de la UNI y revisión del mapa del curso.
*   **00:20 - 00:50 | Bloques 1 & 2: Introducción y Fundamentos, Virtualización e Hipervisores:** El dilema de entornos inconsistentes, la contenerización, hipervisores Tipo 1 vs Tipo 2, diferencias de recursos (VM vs Contenedor) y flujo recomendado de instalación de una VM Linux.
*   **00:50 - 01:20 | Bloque 3: Instalación de Docker:** Criterio del curso (guía oficial), componentes a instalar (Engine/Desktop, Compose, Validación), rutas según sistema operativo y regla práctica de documentación.
*   **01:20 - 01:40 | Bloque 4: Imágenes y Contenedores:** Diferencia conceptual, regla mental de la receta y el plato, y flujo del ciclo de vida básico (Obtener -> Ejecutar -> Ver -> Detener).
*   **01:40 - 01:55 | Receso / Break**
*   **01:55 - 02:40 | Bloques 5 & 6: Comandos Esenciales y Primera Aplicación:** Ejecución de comandos en consola (Labs 1, 2 y 3). Creación y compilación de la primera aplicación Flask con su Dockerfile, ejecución en puerto 5000 y limpieza del laboratorio.
*   **02:40 - 03:00 | Talleres Complementarios (Apache + docker cp), Explicación del Trabajo para el Hogar y Q&A.**

---

## 2. Guión Paso a Paso del Docente (Qué decir y cómo explicar cada punto)

### Introducción: Cómo comenzar la clase
> **Guión Sugerido (Lo que debes decir):**
> *"Muy buenos días con todos. Bienvenidos a la primera sesión del curso 'Docker desde Cero: Crea y Despliega Aplicaciones' (10ma Edición) de la UNI. Mi nombre es Cristian Jampier Chileno Segundo y seré su docente. Hoy comenzaremos desde cero absoluto. Entenderemos de dónde viene la tecnología de contenedores, por qué es superior a las máquinas virtuales clásicas y daremos nuestros primeros pasos en la terminal."*

### Explicación del Temario

#### Bloque 1: Introducción y Fundamentos (El dilema del software)
> **Guión Sugerido (Lo que debes decir):**
> *"Antes de 1956, cargar un barco mercante era un caos: sacos de azúcar, cajas y barriles de todos los tamaños se estibaban de forma manual. Esto hacía que la carga fuera lenta y propensa a daños. Malcolm McLean revolucionó el transporte con el contenedor metálico estándar. A los barcos y grúas no les importa qué hay dentro del contenedor; el método de enganche y apilamiento es universal.
> En el desarrollo de software sufríamos el mismo caos. Una app web requiere versiones específicas de librerías, bases de datos y configuraciones. Cuando pasamos el código a otra laptop o servidor, el sistema falla: el dilema de 'en mi máquina funciona'. Solomon Hykes fundó dotCloud y en 2013 liberó Docker. Docker hace exactamente lo mismo que McLean: empaqueta la aplicación con todo su runtime y dependencias en una caja estándar llamada contenedor, garantizando que corra igual en cualquier máquina."*

#### Bloque 2: Virtualización e Hipervisores (Tipo 1 vs Tipo 2)
> **Guión Sugerido (Lo que debes decir):**
> *"Una máquina virtual clásica ejecuta un sistema operativo completo sobre hardware virtualizado. Esto consume gigabytes de disco y gigabytes de RAM. Un contenedor no es una máquina virtual: comparte el kernel del sistema operativo del host. Es un proceso aislado en el mismo kernel, consumiendo solo megabytes de disco y milisegundos para arrancar.
> Los hipervisores que gestionan las VM se dividen en dos tipos:
> - **Tipo 1 (Bare Metal):** Corre directamente sobre el hardware (ej. VMware ESXi, Hyper-V Server, Proxmox).
> - **Tipo 2 (Hosted):** Corre como una aplicación sobre el sistema operativo host (ej. VirtualBox, VMware Workstation).
> Para este curso, si necesitan un laboratorio limpio y aislado, se recomienda instalar una VM con Linux (Ubuntu Server) configurándole 2 CPU, 4 GB de RAM, 25 GB de disco y red tipo NAT."*

#### Bloque 3: Instalación de Docker (Desktop vs Engine)
> **Guión Sugerido (Lo que debes decir):**
> *"No memoricen comandos de instalación, ya que estos varían por sistema operativo. Sigan siempre la documentación oficial de Docker.
> - Si usan Windows o macOS, instalen **Docker Desktop** (que ya incluye el motor de Docker, la consola de comandos y Docker Compose de forma integrada). En Windows, recuerden que requiere el componente WSL2 (Windows Subsystem for Linux 2) para proveer un kernel de Linux ligero.
> - Si usan Linux o una VM Linux local, instalen **Docker Engine** según la distribución correspondiente y recuerden configurar los permisos post-instalación y habilitar el servicio."*

#### Bloque 4: Imágenes y Contenedores (Diferencias clave)
> **Guión Sugerido (Lo que debes decir):**
> *"La diferencia entre imagen y contenedor es fundamental. La **Imagen** es una plantilla inmutable y de solo lectura que contiene el sistema base, las dependencias y el código de la app. El **Contenedor** es la instancia en ejecución creada a partir de esa imagen.
> Regla mental: La imagen es la receta; el contenedor es el plato de comida ya servido y listo para comer en la mesa.
> El ciclo de vida básico consiste en: Obtener (docker pull) -> Ejecutar (docker run) -> Ver (docker ps) -> Detener (docker stop)."*

#### Bloque 5: Comandos Esenciales (Práctica en Consola)
> **Guión Sugerido (Lo que debes decir):**
> *"Para interactuar con Docker, abrimos la terminal. Si ejecutamos `docker run hello-world`, Docker verifica si tiene la imagen localmente. Si no, la descarga de Docker Hub (pull), crea el contenedor, ejecuta el saludo y se detiene.
> Levantaremos un servidor web Nginx en el puerto 8080 del host con el nombre 'mi-nginx': `docker run --name mi-nginx -d -p 8080:80 nginx`. El flag `-d` corre el contenedor en segundo plano (detached), `-p 8080:80` mapea el puerto 8080 de nuestra máquina física al 80 interno del contenedor y `--name mi-nginx` le da un alias claro. 
> Podemos ver el contenedor activo con `docker ps` y todos con `docker ps -a`. Detenemos el contenedor con `docker stop mi-nginx`, lo eliminamos con `docker rm mi-nginx` y revisamos las imágenes descargadas con `docker images`."*

#### Bloque 6: Primera aplicación: Configuración y Ejecución de Flask
> **Guión Sugerido (Lo que debes decir):**
> *"Ahora crearemos nuestra propia aplicación web en la ruta `codigo/sesion1/`. Escribiremos una app web Flask muy sencilla con tres archivos:
> 1. Un archivo `requirements.txt` con las dependencias: `Flask==3.0.0`, `werkzeug==3.0.1`.
> 2. Un archivo Python `app.py` que importará Flask, definirá la ruta base `/` que devolverá el texto '¡Hola Docker desde el PIT 2026 - UNI! 🚀' y escuchará en el puerto 5000 (`host='0.0.0.0'`).
> 3. Un archivo llamado `Dockerfile`, que es la receta de pasos para fabricar la imagen:
>    - `FROM python:3.9-slim` indica que usaremos una versión base ligera de Python.
>    - `WORKDIR /app` define el directorio de trabajo interno.
>    - `COPY requirements.txt .` copia el archivo al contenedor.
>    - `RUN pip install --no-cache-dir -r requirements.txt` instala las librerías.
>    - `COPY app.py .` copia el código fuente.
>    - `EXPOSE 5000` documenta el puerto expuesto.
>    - Y finalmente, `CMD ["python", "app.py"]` define el comando de inicio en tiempo de ejecución.
> Compilaremos la imagen con: `docker build -t mi-flask:v1 .`. La ejecutaremos con: `docker run --name flask-app -d -p 5000:5000 mi-flask:v1`. Probaremos en http://localhost:5000, y finalmente limpiaremos deteniendo y eliminando el contenedor y la imagen."*

---

## 3. Dinámica e Interacción en el Aula
*   **Pregunta para lanzar al aula:** *"¿Qué pasa si actualizas la versión de Java o Node.js directamente en tu servidor de producción de forma clásica? ¿Por qué nos da tanto miedo esa pantalla de comandos?"*
    *   *Respuesta esperada:* Porque puede romper otras aplicaciones más antiguas que dependan de versiones anteriores. Docker soluciona esto porque cada contenedor tiene su propio runtime aislado y sus librerías correspondientes.
*   **Pregunta técnica:** *"¿Un contenedor de Linux puede correr sobre Windows de manera nativa?"*
    *   *Respuesta pedagógica:* No de forma nativa, por eso Docker Desktop en Windows requiere obligatoriamente **WSL2** para proveer el Kernel de Linux real que haga funcionar los Namespaces y cgroups.

---

## 4. Preguntas Frecuentes de los Alumnos (FAQs)
1.  **¿Docker consume recursos si no hay contenedores activos?**
    *   *Respuesta:* A diferencia de las máquinas virtuales que consumen RAM fija desde que se encienden, Docker no consume CPU si los contenedores están apagados, ya que no hay emulación de hardware.
2.  **¿Qué es la red NAT en una máquina virtual?**
    *   *Respuesta:* Es una red que permite que la VM se conecte a internet utilizando la dirección IP de la máquina física (Host), ideal para empezar a practicar sin conflictos en la red local.

---

## 5. Práctica en Consola Paso a Paso (Guía Visual del Docente)
1.  **Validación de Docker:**
    `docker --version`
    `docker info`
    `docker run hello-world`
2.  **Desplegar Nginx:**
    `docker run --name mi-nginx -d -p 8080:80 nginx`
3.  **Detener y Eliminar Nginx:**
    `docker stop mi-nginx`
    `docker ps -a`
    `docker rm mi-nginx`
    `docker images`
4.  **Construir y levantar la App Flask:**
    `cd codigo/sesion1`
    `docker build -t mi-flask:v1 .`
    `docker run --name flask-app -d -p 5000:5000 mi-flask:v1`
5.  **Limpieza Final:**
    `docker stop flask-app`
    `docker rm flask-app`
    `docker rmi mi-flask:v1`

---

## 6. Taller Práctico / Ejercicio del Alumno - Solucionario Docente

### Taller Práctico A (Core): Construcción y Ejecución de App Flask
Los estudiantes deberán ingresar a `codigo/sesion1`, revisar los archivos del proyecto, compilar la imagen de Docker `mi-flask:v1` y validar su correcta ejecución y respuesta HTTP en el puerto 5000.

### Taller Práctico B (Complementario): Manipulación en Caliente y `docker cp`
**Consigna para la Clase:**
Desplegar un servidor Apache HTTP (`httpd`) en el puerto 8081 en modo detached, crear un archivo `index.html` local con la frase "Bienvenido a UNI PIT 2026", copiarlo dentro de la ruta pública de Apache en el contenedor (`/usr/local/apache2/htdocs/`) usando `docker cp`, y luego limpiar el sistema.

**Solución Paso a Paso:**
1. `docker run --name apache-test -d -p 8081:80 httpd`
2. `echo "<h1>Bienvenido a UNI PIT 2026</h1>" > index.html`
3. `docker cp index.html apache-test:/usr/local/apache2/htdocs/index.html`
4. Validar abriendo http://localhost:8081 en el navegador.
5. `docker stop apache-test && docker rm apache-test`

---

## 7. Trabajo para el Hogar
Desplegar dos servidores web en paralelo en tu máquina local:
*   Un servidor Nginx expuesto en el puerto `8080`.
*   Un servidor Apache (`httpd`) expuesto en el puerto `8081`.
*   Modificar la página principal de cada servidor usando `docker cp` con textos descriptivos personalizados ("Servidor 1: Nginx - UNI 2026" y "Servidor 2: Apache - UNI 2026").
*   **Entregable:** Captura de pantalla de los dos navegadores mostrando la conexión concurrente a ambos puertos y la personalización de las páginas.

---

## 8. Solucionario del Trabajo para el Hogar
1. `docker run --name web-nginx -d -p 8080:80 nginx`
2. `docker run --name web-apache -d -p 8081:80 httpd`
3. `echo "Servidor 1: Nginx - UNI 2026" > nginx.html`
   `docker cp nginx.html web-nginx:/usr/share/nginx/html/index.html`
   `echo "Servidor 2: Apache - UNI 2026" > apache.html`
   `docker cp apache.html web-apache:/usr/local/apache2/htdocs/index.html`

---

## 9. Gestión del Aula y Errores Frecuentes
*   **Error: Puerto ocupado (`bind: address already in use`).** Solución: `-p 8082:80`.
*   **Error: No abre en navegador (Contenedor detenido).** Solución: `docker ps -a` y `docker logs <nombre>`.
*   **Error: El motor de Docker no responde (`docker daemon is not running`).** Solución: Abrir Docker Desktop o `sudo systemctl start docker`.
