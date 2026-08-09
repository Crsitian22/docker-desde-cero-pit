# 🧪 Laboratorio 06: Proyectos Finales en Producción
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Instructor:** Cristian Jampier Chileno Segundo | OTI - UNI  

En este laboratorio integrador final, los alumnos ejecutan dos proyectos de nivel profesional:

---

## 🔹 Proyecto 1: Stack Web Multi-Contenedor (Flask + PostgreSQL + Nginx)

### 🎯 Objetivos:
1. Integrar la arquitectura multi-entorno usando Compose Overrides (`compose.yml` base + `compose.dev.yml` / `compose.prod.yml`).
2. Alternar configuraciones entre Desarrollo (hot-reload con Bind Mounts) y Producción (imágenes inmutables).
3. Automatizar la actualización mediante el script en Bash `desplegar.sh`.

### 🚀 Pasos de Ejecución:
```bash
# 1. Entrar a la carpeta del Proyecto 1
cd codigo/sesion6

# 2. Ejecutar script de despliegue automático
chmod +x desplegar.sh
./desplegar.sh

# 3. Probar en el navegador web
http://localhost:8080
```

---

## 🔹 Proyecto 2 (Capstone): Nube Privada Institucional (UNI Drive + OnlyOffice)

### 🎯 Objetivos:
1. Desplegar una suite empresarial completa de almacenamiento en la nube e integración de edición de documentos en tiempo real (Nextcloud + OnlyOffice Document Server + MariaDB 11.4 + Redis).
2. Aplicar aislamiento de redes Zero-Trust y persistencia total mediante volúmenes nombrados.

### 🚀 Pasos de Ejecución:
```bash
# 1. Entrar a la carpeta del Proyecto 2 (Drive)
cd codigo/sesion6/proyecto_drive

# 2. Levantar la infraestructura en segundo plano
docker compose up -d

# 3. Acceso a los servicios locales:
# Nube Privada Nextcloud Drive: http://localhost:8080
# OnlyOffice Document Server: http://localhost:8081
```

- **📂 Ver Guía Detallada del Proyecto 2:** [`proyecto_drive/README.md`](./proyecto_drive/README.md)
