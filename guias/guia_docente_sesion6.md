# Guía Docente - Sesión 6: Configuración Multi-Entorno, Debugging Profesional y Despliegue Final (10ma Edición 2026)
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones - 10ma Edición
**Programa:** Programa de Iniciación Tecnológica (PIT) 2026 - OTI - UNI

---

## Perfil del Alumno y Enfoque Pedagógico
*En esta última sesión los alumnos integrarán todo lo aprendido durante el curso. Diseñaremos una arquitectura multi-entorno que permita alternar entre desarrollo (`compose.dev.yml` con live-reload) y producción (`compose.prod.yml` con Nginx y reinicio automático). Además, estableceremos el protocolo profesional de 5 pasos para el diagnóstico de fallas y la automatización con scripts de despliegue (`deploy.sh`).*

---

## 1. Planificación de la Clase (3 Horas)
*   **00:00 - 00:20 | Bienvenida y Repaso de Arquitectura Nginx:** Breve revisión de la Sesión 5.
*   **00:20 - 01:10 | Bloque 1: Sobreescritura de Compose Multi-Entorno:** Archivo base `compose.yml` + extensión `compose.dev.yml` / `compose.prod.yml`.
*   **01:10 - 01:40 | Bloque 2: Protocolo de Diagnóstico y Debugging Profesional:** Protocolo de 5 pasos (`ps` -> `logs` -> `inspect` -> `exec` -> `prune`).
*   **01:40 - 01:55 | Receso / Break**
*   **01:55 - 02:40 | Bloque 3: Proyecto Final y Script de Despliegue `deploy.sh`:** Automatización en Bash para despliegue automatizado en un solo comando.
*   **02:40 - 03:00 | Cierre del Curso, Entrega de Certificados y Feedback.**

---

## 2. Guión Paso a Paso del Docente

### Introducción
> **Guión Sugerido:**
> *"Bienvenidos a nuestra última sesión. Hoy unificaremos todas las piezas del rompecabezas. Aprenderemos a reutilizar nuestra infraestructura para despliegues en Desarrollo y Producción sin duplicar código, crearemos un script de despliegue automatizado en Bash y dominaremos el protocolo de diagnóstico de fallas en producción."*

---

## 3. Práctica en Consola: Script de Despliegue `deploy.sh`

```bash
#!/bin/bash
# Script de Despliegue Automatizado - PIT 2026

ENTORNO=${1:-dev}

echo "🚀 Iniciando Despliegue en Entorno: $ENTORNO"

if [ "$ENTORNO" == "prod" ]; then
    docker compose -f compose.yml -f compose.prod.yml up -d --build
    echo "✅ Aplicación desplegada en PRODUCCIÓN en http://localhost"
else
    docker compose -f compose.yml -f compose.dev.yml up -d --build
    echo "🛠️ Aplicación desplegada en DESARROLLO en http://localhost:5000"
fi
```

#### Protocolo de Debugging de 5 Pasos:
1. `docker compose ps` (Revisar estado)
2. `docker compose logs -f web` (Revisar logs de error)
3. `docker inspect <contenedor>` (Auditar variables y volúmenes)
4. `docker compose exec web sh` (Entrar a la consola interactiva)
5. `docker system prune -a --volumes` (Limpieza profunda)

---

## 4. Cierre del Curso
Felicitar a los alumnos por haber completado exitosamente las 6 sesiones del programa **Docker desde Cero (10ma Edición 2026)** de la Universidad Nacional de Ingeniería.
