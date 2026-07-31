# Guía de Enseñanza Completa - Taller Semanal Intensivo de Docker (10ma Edición 2026)
**Programa de Iniciación Tecnológica (PIT) 2026 | OTI - UNI**
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Estructura del Curso:** 5 Sesiones de 2 horas (Lunes a Viernes)

---

## 🎯 Objetivo General del Taller Semanal (Nivel: Cero a Avanzado)
Capacitar a los alumnos en el uso profesional de Docker, basándose en la pedagogía secuencial del programa oficial del PIT 2026 de la UNI. El taller transita desde el origen de la tecnología (la analogía del transporte de McLean) y la configuración eficiente de WSL2 en Windows, hasta técnicas avanzadas de formateo de salida CLI (`--format`), ENTRYPOINT vs CMD, compilación Multi-Stage, registros efímeros (`ttl.sh`) y orquestación con Docker Compose y Swarm.

---

## 📅 Temario y Cronograma Semanal

### **Día 1: Introducción, Arquitectura y Configuración del Entorno**
- Bienvenida y validación de Docker Desktop / WSL2.
- La historia de los contenedores: Malcolm McLean (1956) y Solomon Hykes (2013).
- Virtualización tradicional vs Contenedores: consumo en disco (GBs vs MBs) y tiempo de arranque.
- Namespaces del Kernel (NET, PID, MNT, UTS, IPC) y Control Groups (cgroups).

### **Día 2: Consola CLI, Formateo Avanzado y Rutinas de Inspección**
- Comandos de gestión de Docker (`docker container run`, `docker image ls`).
- Formateo avanzado con `--format` (Golang templates) y `jq`.
- Diagnóstico en caliente: `docker logs --tail 50 -f`, `docker stats`, `docker system df`.

### **Día 3: Construcción de Imágenes, Registros Públicos y Hardening**
- Anatomía del Dockerfile y optimización de la caché de UnionFS.
- Registros efímeros (`ttl.sh`) y GitHub Packages (`ghcr.io`).
- Compilación Multi-Stage con objetivo `--target`.
- Seguridad y Hardening: Ejecución como usuario no-root (`USER appuser`).

### **Día 4: Compose Declarativo, DNS Interno y Persistencia**
- Sintaxis declarativa YAML de Compose V2 (`services`, `networks`, `volumes`).
- DNS interno de Docker (127.0.0.11) por alias de servicio.
- Persistencia de datos: Volúmenes nombrados vs Bind Mounts.

### **Día 5: Alta Disponibilidad, Reverse Proxy Nginx y Script Final**
- Arquitectura con Nginx como Reverse Proxy (Puerto 80/443).
- Limites de memoria RAM y CPU para prevenir caídas por OOM Killer.
- Script Bash de despliegue automatizado (`deploy.sh`) y respaldos de base de datos.
