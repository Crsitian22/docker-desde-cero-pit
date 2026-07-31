# 🐳 Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)
### Universidad Nacional de Ingeniería (UNI) - Programa de Iniciación Tecnológica (PIT)
**Docente:** Ing. Cristian Jampier Chileno Segundo | OTI - UNI  
**Repositorio Oficial:** [github.com/Crsitian22/docker-desde-cero-pit](https://github.com/Crsitian22/docker-desde-cero-pit.git)

---

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![UNI](https://img.shields.io/badge/UNI-PIT_2026-red?style=for-the-badge)

---

## 📌 Descripción del Curso
Este repositorio contiene todo el **material teórico, guías docentes, código fuente de laboratorios, archivos Dockerfile, configuraciones de Docker Compose y proyectos prácticos** del curso **Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)** dictado en el Programa de Iniciación Tecnológica (PIT) de la Universidad Nacional de Ingeniería.

El curso está diseñado para llevar a los estudiantes desde el origen de la contenerización y el dilema *"en mi máquina sí funciona"*, hasta la arquitectura y despliegue de stacks multi-contenedor de grado de producción con proxies inversos Nginx, persistencia de datos y scripts de automatización.

---

## 🗺️ Mapa de Contenidos del Curso

| Sesión | Tema Principal | Tecnologías / Conceptos | Código / Laboratorio |
|---|---|---|---|
| **[Sesión 1](guias/guia_docente_sesion1.md)** | Introducción, Fundamentos y Tu Primera App | VM vs Contenedor, Engine, CLI (`run`, `ps`, `stop`), Nginx, App Flask | [`codigos/sesion1/`](codigos/sesion1/) |
| **[Sesión 2](guias/guia_docente_sesion2.md)** | Dockerfile Profesional y Buenas Prácticas | Capas UnionFS, Caché, `.dockerignore`, Multi-Stage, Alpine, Docker Hub | [`codigos/sesion2/`](codigos/sesion2/) |
| **[Sesión 3](guias/guia_docente_sesion3.md)** | Orquestación Local con Docker Compose | `compose.yml`, DNS Interno, Variables `.env`, Flask + PostgreSQL | [`codigos/sesion3/`](codigos/sesion3/) |
| **[Sesión 4](guias/guia_docente_sesion4.md)** | Redes Docker, Persistencia y Backups | Volúmenes Nombrados, Bind Mounts, Healthchecks, `pg_dump` | [`codigos/sesion4/`](codigos/sesion4/) |
| **[Sesión 5](guias/guia_docente_sesion5.md)** | Reverse Proxy con Nginx y Producción | Nginx Proxy (`proxy_pass`), Aislamiento Multi-Red, `docker stats` | [`codigos/sesion5/`](codigos/sesion5/) |
| **[Sesión 6](guias/guia_docente_sesion6.md)** | Multi-Entorno, Debugging y Despliegue | Multi-entorno (`dev` vs `prod`), Protocolo de Debugging, `deploy.sh` | [`codigos/sesion6/`](codigos/sesion6/) |

---

## 📁 Estructura del Repositorio

```text
docker-desde-cero-pit/
├── README.md                      # Documento principal del repositorio
├── MANUAL_DOCENTE.md              # Manual maestro completo del docente
├── LICENSE                        # Licencia MIT del proyecto
├── guias/                         # Guías docentes por sesión, talleres y banco de evaluaciones
│   ├── guia_docente_sesion1.md
│   ├── guia_docente_sesion2.md
│   ├── guia_docente_sesion3.md
│   ├── guia_docente_sesion4.md
│   ├── guia_docente_sesion5.md
│   ├── guia_docente_sesion6.md
│   ├── guia_taller_docker.md
│   └── evaluaciones_y_test_docker.md
├── codigos/                       # Código fuente runnable de los laboratorios
│   ├── sesion1/                   # Primera App Flask + Dockerfile
│   ├── sesion2/                   # Dockerfile Multi-Stage optimizado
│   ├── sesion3/                   # Docker Compose Flask + PostgreSQL
│   ├── sesion4/                   # Volúmenes, Healthchecks y Script de Backup SQL
│   ├── sesion5/                   # Nginx Reverse Proxy + Multi-Red
│   └── sesion6/                   # Multi-entorno (dev/prod) + script deploy.sh
└── slides/                        # Índice de diapositivas oficiales
    └── README.md
```

---

## ⚙️ Requisitos de Instalación

Para ejecutar los laboratorios en tu máquina local se requiere:

1. **Docker Desktop / Docker Engine:**
   - **Windows / macOS:** Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Requiere WSL2 en Windows).
   - **Linux:** Instalar [Docker Engine](https://docs.docker.com/engine/install/) e instalar el plugin `docker-compose-plugin`.
2. **Git:**
   - Instalar [Git](https://git-scm.com/) para clonar el repositorio.
3. **VS Code (Recomendado):**
   - Extensión [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker).

---

## 🚀 Guía Rápida de Inicio

1. **Clonar este repositorio:**
   ```bash
   git clone https://github.com/Crsitian22/docker-desde-cero-pit.git
   cd docker-desde-cero-pit
   ```

2. **Ejecutar el Laboratorio de la Sesión 1:**
   ```bash
   cd codigos/sesion1
   docker build -t mi-flask:v1 .
   docker run --name flask-app -d -p 5000:5000 mi-flask:v1
   # Probar en http://localhost:5000
   ```

3. **Ejecutar el Proyecto Final de la Sesión 6 (Producción Local):**
   ```bash
   cd codigos/sesion6
   chmod +x deploy.sh
   ./deploy.sh prod
   # Probar en http://localhost (Puerto 80 gestionado por Nginx)
   ```

---

## 📚 Material Complementario
- 📄 **[Manual Completo del Docente](MANUAL_DOCENTE.md):** Guía detallada con explicaciones teóricas, analogías y solucionario.
- 📝 **[Banco de Evaluaciones y Quizzes](guias/evaluaciones_y_test_docker.md):** Preguntas de opción múltiple con clave de respuestas por sesión.
- 🏋️ **[Guía del Taller Intensivo](guias/guia_taller_docker.md):** Planificación para talleres intensivos de 5 días.

---

## 👨‍🏫 Autor y Créditos
- **Docente:** Ing. Cristian Jampier Chileno Segundo
- **Institución:** Universidad Nacional de Ingeniería (UNI) - OTI / CTIC
- **Edición:** 10ma Edición (2026)
- **Licencia:** [MIT License](LICENSE)
