# Guía Docente - Sesión 5: Reverse Proxy con Nginx y Producción (10ma Edición 2026)
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones - 10ma Edición
**Programa:** Programa de Iniciación Tecnológica (PIT) 2026 - OTI - UNI

---

## Perfil del Alumno y Enfoque Pedagógico
*En producción no es aceptable exponer aplicaciones web en puertos no estándares como el 5000 o 8000 directamente a internet. En esta sesión enseñaremos a colocar un servidor **Nginx como Reverse Proxy** en el puerto público 80/443, actuando como escudo protector de la aplicación Flask y la base de datos PostgreSQL mediante una arquitectura multi-red segura.*

---

## 1. Planificación de la Clase (3 Horas)
*   **00:00 - 00:20 | Repaso de Persistencia:** Verificar scripts de backup SQL desarrollados en la Sesión 4.
*   **00:20 - 01:10 | Bloque 1: Arquitectura con Reverse Proxy Nginx:** Por qué colocar un proxy frontal. Ventajas de seguridad, terminación SSL, balanceo de carga y aislamiento de microservicios.
*   **01:10 - 01:40 | Bloque 2: Configuración de Nginx e Integración en Compose:** Directiva `proxy_pass http://web:5000`, cabeceras de proxy (`X-Forwarded-For`), y separación de redes (`red-front` vs `red-back`).
*   **01:40 - 01:55 | Receso / Break**
*   **01:55 - 02:40 | Bloque 3: Monitoreo y Diagnóstico de Recursos:** Uso de `docker stats`, inspección de consumo de CPU/RAM y prevención de sobrecargas.
*   **02:40 - 03:00 | Prueba de Conexión HTTP Local y Tarea.**

---

## 2. Guión Paso a Paso del Docente

### Introducción
> **Guión Sugerido:**
> *"Buenas tardes. Hoy daremos el salto hacia una arquitectura de producción local. Ninguna empresa seria expone la aplicación Flask o la base de datos directamente al público. Colocaremos un servidor Nginx en el puerto 80 que recibirá todas las peticiones y las derivará internamente a nuestros servicios tras una red privada segura."*

### Explicación de la Arquitectura
```nginx
# nginx.conf
server {
    listen 80;
    server_name localhost;

    location / {
        proxy_pass http://web:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

#### Multi-Red de Seguridad:
- `red-front`: Conecta únicamente a Nginx y a la app Flask.
- `red-back`: Conecta únicamente a la app Flask y a PostgreSQL.
- **Resultado:** Nginx no tiene acceso directo a la BD y la BD no tiene acceso al exterior.

---

## 3. Práctica en Consola Paso a Paso

1. Levantar el stack completo con Nginx: `docker compose up -d`
2. Validar acceso en el navegador a `http://localhost` (Puerto 80 por defecto).
3. Monitorear recursos en consola: `docker stats`

---

## 4. Gestión del Aula y Errores Frecuentes
*   **Error `502 Bad Gateway` en Nginx.** Solución: Nginx no puede resolver el hostname `web` o la app Flask no está escuchando en el puerto 5000. Verificar que compartan la red `red-front`.
