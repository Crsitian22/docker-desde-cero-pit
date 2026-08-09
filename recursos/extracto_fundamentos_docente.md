# 🎙️ EXTRACTO DE FUNDAMENTOS TÉCNICOS Y GUIÓN DEL DOCENTE (10MA EDICION 2026)
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones en Producción  
**Instructor:** Cristian Jampier Chileno Segundo | OTI - UNI  
**Propósito:** Apuntes de apoyo teórico y explicaciones profundas para el docente durante la clase en vivo.

---

## 📌 1. INSTALACIÓN Y PREPARACIÓN DEL ENTORNO
- **Mecanismo en Windows (WSL2 Backend):** Explicar a los alumnos que en Windows, Docker Desktop no utiliza virtualización completa pesada (Hyper-V tradicional), sino **Windows Subsystem for Linux v2 (WSL2)** con una distribución ultraligera Linux basada en el Kernel nativo.
- **Daemon de Docker (`dockerd`):** El motor principal que corre en segundo plano como servicio de sistema. Maneja imágenes, contenedores, redes y volúmenes.
- **Socket UNIX (`/var/run/docker.sock`):** Es el canal de comunicación IPC por donde la CLI (`docker`) le envía comandos en formato JSON a la API REST de `dockerd`.
- **Tip de Gestión de Clase durante la Instalación:** *La instalación en las máquinas de los alumnos suele tomar de 15 a 25 minutos. Durante este lapso, usar la teoría de relleno (Virtualización vs Contenedores, Historia de Solomon Hykes y Dotcloud) para mantener entretenido y atento al aula.*

---

## 📌 2. ANATOMÍA INTERNA DE IMÁGENES Y CAPAS INMUTABLES
- **Sistema de Archivos en Capas (UnionFS / Overlay2):** Una imagen de Docker no es un archivo monolítico ISO, sino una pila de **capas de sólo lectura (Read-Only Layers)** superpuestas mediante el driver `Overlay2`.
- **Inmutabilidad de la Imagen:** Cada instrucción del Dockerfile (`FROM`, `RUN`, `COPY`) crea una nueva capa de sólo lectura identificada por un hash criptográfico SHA-256. Ninguna capa existente se puede modificar.
- **Capa del Contenedor (Read-Write Layer):** Al ejecutar `docker run`, Docker añade una delgada capa de escritura (**Container Layer / Writeable Layer**) sobre la pila inmutable.
- **Copy-on-Write (CoW):** Si un proceso dentro del contenedor intenta modificar un archivo de la imagen base, el archivo se copia primero a la capa de escritura del contenedor antes de ser modificado. Esto garantiza que la imagen original permanezca 100% intacta para otros contenedores.

---

## 📌 3. COMPARATIVA TÉCNICA: VIRTUALIZACIÓN (VMs) VS CONTENEDORIZACIÓN
- **Máquinas Virtuales (VMs):**
  - Requieren un **Hipervisor (Tipo 1 / Tipo 2)**.
  - Cada VM emula hardware completo (BIOS, CPU virtual, RAM, Disco) e instala un **Guest OS (Sistema Operativo Huesped completo)**.
  - Duplicación de Kernels y consumo masivo de memoria RAM/Disco (GBs). Tiempo de inicio: minutos.
- **Contenedores de Docker:**
  - Comparten el **Kernel del Host (Host Linux Kernel)**.
  - **Namespaces de Linux (Aislamiento de Recursos):**
    - `PID Namespace`: Aísla la tabla de procesos (el contenedor cree ser el PID 1).
    - `NET Namespace`: Aísla interfaces de red y tablas de enrutamiento IP.
    - `MNT Namespace`: Aísla puntos de montaje de sistema de archivos.
    - `IPC Namespace`: Aísla comunicación inter-proceso (Shared Memory, Semáforos).
    - `UTS Namespace`: Aísla el Hostname del sistema.
    - `USER Namespace`: Mapea usuarios dentro del contenedor a usuarios no root en el Host.
  - **Control Groups (cgroups v2):** Limita y mide el consumo de recursos físicos (cuotas de CPU, límite de RAM, I/O de disco).

---

## 📌 4. ENFOQUE IMPERATIVO VS DECLARATIVO Y ARCHIVOS YAML
- **Comandos Imperativos (`docker run`):** Indican *cómo* hacer las cosas paso a paso. Ejemplo: `docker run -d -p 8080:80 --name mi_web nginx`. Es propenso a errores humanos y difícil de replicar en equipos de trabajo.
- **Enfoque Declarativo (`compose.yml`):** Define el *estado deseado* de la infraestructura (Infraestructura como Código - IaC). Se describe qué servicios, redes y volúmenes deben existir.
- **Sintaxis YAML:** Archivos estructurados mediante identación estricta de espacios (sin tabuladores).
- **Idempotencia:** Propiedad fundamental de `docker compose up`. Si ejecutas el comando $N$ veces, Docker evalúa la diferencia entre el estado actual y el archivo `compose.yml`. Si nada ha cambiado, **no recrea ni destruye nada**, garantizando un estado constante y predecible.

---

## 📌 5. REDES, VOLÚMENES Y REDIRECCIÓN DE PUERTOS
- **Volúmenes Nombrados (Named Volumes):**
  - Administrados 100% por Docker en la ruta interna del Host Linux `/var/lib/docker/volumes/`.
  - Desacoplados del ciclo de vida del contenedor: si destruyes el contenedor con `docker rm -f`, **los datos en el volumen persisten intactos**.
- **Bind Mounts:**
  - Mapeo directo de un directorio o archivo del Host local (ej: `./app:/app`). Ideal para entornos de desarrollo con recarga en tiempo real (*hot-reload*).
- **Redirección de Puertos (Port Forwarding `-p Host:Contenedor`):**
  - Mapeo gestionado por el demonio de Docker e `iptables` NAT. Ejemplo: `-p 8080:80` redirige las peticiones entrantes del puerto 8080 del host físico al puerto 80 del servidor web dentro del contenedor.
- **Driver de Red Bridge (`bridge`):** Red virtual interna predeterminada que permite la comunicación por DNS/Hostname interno entre contenedores conectados a la misma red.
