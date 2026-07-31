# 🐳 Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)
### Universidad Nacional de Ingeniería (UNI) - Programa de Iniciación Tecnológica (PIT)
**Docente:** Ing. Cristian Jampier Chileno Segundo | OTI - UNI  
**Repositorio de Laboratorios:** [github.com/Crsitian22/docker-desde-cero-pit](https://github.com/Crsitian22/docker-desde-cero-pit.git)

---

![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![UNI](https://img.shields.io/badge/UNI-PIT_2026-red?style=for-the-badge)

---

## 📌 Descripción del Repositorio
Este repositorio público contiene **el código fuente completo, archivos de configuración, Dockerfiles, compose.yml y laboratorios prácticos** para los estudiantes del curso **Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)** dictado en el Programa de Iniciación Tecnológica (PIT) de la Universidad Nacional de Ingeniería (UNI).

---

## 🗺️ Estructura de Laboratorios por Sesión

| Sesión | Tema | Tecnologías / Aprendizaje | Archivos del Laboratorio |
|---|---|---|---|
| **Sesión 1** | Fundamentos y Tu Primera App | VM vs Contenedor, CLI (
un, ps, stop), Nginx, App Flask | [codigos/sesion1/](codigos/sesion1/) |
| **Sesión 2** | Dockerfile Profesional y Buenas Prácticas | Capas UnionFS, Caché, .dockerignore, Multi-Stage Build, Alpine | [codigos/sesion2/](codigos/sesion2/) |
| **Sesión 3** | Orquestación Local con Docker Compose | compose.yml, DNS Interno, Variables .env, Flask + PostgreSQL | [codigos/sesion3/](codigos/sesion3/) |
| **Sesión 4** | Redes, Persistencia y Backups SQL | Volúmenes Nombrados, Bind Mounts, Healthchecks, pg_dump | [codigos/sesion4/](codigos/sesion4/) |
| **Sesión 5** | Reverse Proxy con Nginx y Producción | Reverse Proxy (proxy_pass), Aislamiento Multi-Red, docker stats | [codigos/sesion5/](codigos/sesion5/) |
| **Sesión 6** | Multi-Entorno, Debugging y Despliegue | Multi-entorno (dev vs prod), Debugging Profesional, deploy.sh | [codigos/sesion6/](codigos/sesion6/) |

---

## 📁 Estructura del Repositorio

`	ext
docker-desde-cero-pit/
├── README.md                      # Documentación del repositorio
├── LICENSE                        # Licencia MIT
├── .gitignore                     # Filtros para archivos temporales y secretos
├── codigos/                       # Código fuente runnable de los laboratorios
│   ├── sesion1/                   # Primera App Flask + Dockerfile
│   ├── sesion2/                   # Dockerfile Multi-Stage optimizado
│   ├── sesion3/                   # Docker Compose Flask + PostgreSQL
│   ├── sesion4/                   # Volúmenes, Healthchecks y Backups SQL
│   ├── sesion5/                   # Nginx Reverse Proxy + Multi-Red
│   └── sesion6/                   # Multi-entorno (dev/prod) + script deploy.sh
└── slides/                        # Referencia de diapositivas oficiales
    └── README.md
`

---

## ⚙️ Requisitos para la Clase

1. **Docker Desktop / Docker Engine:**
   - **Windows / macOS:** Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop/) (Habilitar WSL2 en Windows).
   - **Linux:** Instalar [Docker Engine](https://docs.docker.com/engine/install/).
2. **Git:**
   - Instalar [Git](https://git-scm.com/) para clonar los ejercicios.
3. **VS Code:**
   - Editor recomendado con la extensión oficial de Docker.

---

## 🚀 Cómo Clonar y Trabajar en Clase

`ash
# 1. Clonar el repositorio
git clone https://github.com/Crsitian22/docker-desde-cero-pit.git
cd docker-desde-cero-pit

# 2. Entrar a la carpeta de la sesión correspondiente (ejemplo: Sesión 1)
cd codigos/sesion1
docker build -t mi-flask:v1 .
docker run --name flask-app -d -p 5000:5000 mi-flask:v1

# 3. Probar en el navegador: http://localhost:5000
`

---

## 👨‍🏫 Docente
- **Ing. Cristian Jampier Chileno Segundo**  
- **Institución:** Universidad Nacional de Ingeniería (UNI) - OTI / CTIC  
- **Programa:** PIT 2026 - 10ma Edición
