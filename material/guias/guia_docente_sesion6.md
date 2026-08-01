# 🎙️ Guía Docente Diapositiva por Diapositiva — Sesión 6: Proyecto Final y Despliegue Completo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Instructor:** Cristian Jampier Chileno Segundo | OTI - UNI  
**Programa:** Programa de Iniciación Tecnológica (PIT 2026) — Universidad Nacional de Ingeniería  
**Total Diapositivas:** 26 Diapositivas  

---

## 🎯 Instrucciones de Orientación Pedagógica
Esta guía contiene la explicación detallada y el guión profesional en primera persona para abordar **cada una de las 26 diapositivas** de la presentación oficial de la Sesión 6 (Sesión Final).
Está diseñada para guiar la clase de cierre del curso, enseñando a estructurar proyectos multi-entorno con Compose Overrides (`compose.yml` + `compose.dev.yml` / `compose.prod.yml`), realizar limpiezas seguras de recursos huérfanos, aplicar el protocolo de debugging profesional, escribir un script Bash de automatización `desplegar.sh` y evaluar el proyecto final integrador.

---

## 🖥️ Explicación Diapositiva por Diapositiva (1 a 26)

### 📄 Diapositiva 1: DOCKER DESDE CERO: Crea y Despliega Aplicaciones — Sesión 6
**Contenido de la PPT:**
```text
DOCKER DESDE CERO: Crea y Despliega Aplicaciones
INSTRUCTOR: Cristian Jampier Chileno Segundo
PROGRAMA DE INICIACIÓN TECNOLÓGICA — PIT 2026
Oficina de Tecnologías de la Información (OTI - UNI)
Programa Completo — PIT 2026
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Muy buenos días/tardes a todos. Bienvenidos a la **Sesión 6**, la sesión final de nuestro curso *Docker desde Cero: Crea y Despliega Aplicaciones* de la OTI-UNI.
> Hoy consolidaremos todo el conocimiento del programa. Integraremos nuestro stack completo (Flask + PostgreSQL + Nginx) en una arquitectura multi-entorno para Desarrollo y Producción, dominaremos las técnicas de limpieza e inspección profesional, automatizaremos el despliegue con un script de Bash y revisaremos los requisitos del Proyecto Final del curso."

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar la portada del curso y recordar la ruta del repositorio oficial: `https://github.com/Crsitian22/docker-desde-cero-pit`.

**💡 Tip de Gestión del Aula:**
- Felicitar al grupo por haber llegado a la sesión integradora de cierre.

---

### 📄 Diapositiva 2: SESIÓN 6 — Índice del Temario
**Contenido de la PPT:**
```text
SESIÓN 6
1. Configuración Multi-Entorno
2. Manejo de .env por Entorno
3. Limpieza de Recursos
4. Debugging Profesional
5. Reconstrucción desde Cero
6. Despliegue e Integración Final
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los 6 ejes temáticos de esta última sesión:
> 1. En **Configuración Multi-Entorno**, aprenderemos a combinar manifiestos Compose base con overrides.
> 2. En **Manejo de .env por Entorno**, alternaremos entre `.env.dev` y `.env.prod`.
> 3. En **Limpieza de Recursos**, diferenciaremos la eliminación de recursos efímeros de la conservación de volúmenes.
> 4. En **Debugging Profesional**, aplicaremos el protocolo de diagnóstico rápido ante fallas.
> 5. En **Reconstrucción desde Cero**, ejecutaremos el flujo de reset de laboratorio.
> 6. Y en **Despliegue e Integración Final**, ejecutaremos el script de automatización y validaremos el stack completo."

**👨‍💻 Acción en Consola / Pizarra:**
- Anotar los 6 bloques en la pizarra marcando la meta: `Despliegue automatizado reproducible`.

**💡 Tip de Gestión del Aula:**
- Indicar a los alumnos que abran la carpeta `codigo/sesion6` o `laboratorios/sesion-final/labs-finales/lab4`.

---

### 📄 Diapositiva 3: Objetivo de la Sesión 6
**Contenido de la PPT:**
```text
Objetivo de la sesión 6:
Al terminar la sesión 6 podrás:
• Separar configuración para entornos dev y prod.
• Ejecutar el proyecto final con archivos Compose específicos.
• Limpiar contenedores, imágenes, redes y volúmenes huérfanos.
• Diagnosticar fallas usando logs, inspect, exec y stats.
• Destruir y reconstruir el stack completo con un flujo reproducible.
• Validar que Flask, PostgreSQL y Nginx queden listos en minutos.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Nuestro **Objetivo de la Sesión 6** es la maestría operativa:
> Al finalizar esta clase, cada uno de ustedes sabrá ejecutar un stack usando múltiples manifiestos Compose con el flag `-f`, limpiará recursos huérfanos de su máquina sin borrar bases de datos por error, solucionará problemas inspeccionando bitáoras y reconstruirá una infraestructura completa de producción en minutos mediante un solo script."

**👨‍💻 Acción en Consola / Pizarra:**
- Enfatizar las palabras clave: **MULTI-ENTORNO (DEV/PROD)**, **CLEANUP SEGURO**, **REPRODUCIBILIDAD TOTAL**.

**💡 Tip de Gestión del Aula:**
- Explicar que un entorno profesional exige que el despliegue no dependa de intervenciones manuales complejas.

---

### 📄 Diapositiva 4: Bloque 1 — Multi-entorno
**Contenido de la PPT:**
```text
Multi-entorno
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Iniciamos el **Bloque 1: Multi-entorno**. Vamos a aprender cómo reutilizar un archivo Compose base agregando variaciones según el entorno de trabajo."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar la ecuación YAML en la pizarra: `compose.yml (Base) + compose.dev.yml (Override Dev) = Stack de Desarrollo`.

**💡 Tip de Gestión del Aula:**
- Preguntar cuántos han tenido la tentación de duplicar todo un archivo `docker-compose.yml` grande solo para cambiar un puerto o una variable.

---

### 📄 Diapositiva 5: Por qué separar dev y prod
**Contenido de la PPT:**
```text
Por qué separar dev y prod
• En desarrollo necesitamos recarga rápida, logs visibles y bind mounts.
• En producción preferimos imagen construida, menos puertos y configuración cerrada.
• El mismo proyecto debe poder levantarse con reglas distintas según el entorno.
• Compose permite combinar archivos para reutilizar una base común.

REGLA PRÁCTICA: No copies todo el YAML: define una base y agrega diferencias por entorno.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Entendamos **Por qué separar Dev y Prod**:
> Las necesidades de un desarrollador y de un servidor de producción son radicalmente opuestas:
> - **En Desarrollo:** Queremos recarga de código en vivo (hot-reload mediante Bind Mounts), puertos de base de datos expuestos para conectar nuestro IDE local, logs interactivos y variables de depuración (`FLASK_DEBUG=1`).
> - **En Producción:** Queremos imágenes estáticas inmutables, cero puertos de base de datos expuestos, proxy frontal Nginx, políticas de reinicio automático (`restart: unless-stopped`) y variables cerradas.
> **Regla Práctica:** *Nunca dupliquen todo el YAML de Compose. Creen un archivo `compose.yml` con la arquitectura base comun, y redacten archivos pequeños de override (`compose.dev.yml` y `compose.prod.yml`) para aplicar solo las diferencias*."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir la comparación de necesidades en la pizarra:
  - `Dev:` Bind Mounts + Debug On + Ports DB Expuestos.
  - `Prod:` Imágenes Inmutables + Hardening + Restart Always + Nginx Proxy.

**💡 Tip de Gestión del Aula:**
- Resaltar el principio DRY (Don't Repeat Yourself) aplicado a la infraestructura como código.

---

### 📄 Diapositiva 6: Archivos del proyecto final
**Contenido de la PPT:**
```text
ARCHIVOS DEL PROYECTO FINAL
IDEA:
El archivo base describe la arquitectura; los archivos por entorno solo cambian lo necesario.

Estructura sugerida:
• compose.yml           (Arquitectura base compartida)
• compose.dev.yml       (Overrides para desarrollo local)
• compose.prod.yml      (Overrides para producción)
• .env.dev              (Variables de desarrollo)
• .env.prod             (Variables de producción)
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Estructura del Proyecto Final**:
> 1. `compose.yml`: Define la arquitectura base (servicios `web`, `db`, `nginx`, volumen `postgres_data`).
> 2. `compose.dev.yml`: Agrega los bind mounts (`./app:/app`) y activa el modo debug para el desarrollador.
> 3. `compose.prod.yml`: Asigna tags de imágenes de producción, políticas de restart y límites de recursos.
> 4. `.env.dev` y `.env.prod`: Contienen las variables de cada ambiente."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar en VS Code los 5 archivos estructurados en la raíz del proyecto.

**💡 Tip de Gestión del Aula:**
- Verificar que entiendan cómo la combinación de manifiestos reduce la duplicación de código.

---

### 📄 Diapositiva 7: compose.yml base
**Contenido de la PPT:**
```text
COMPOSE.YML BASE
services:
  web:
    build: .
    expose:
      - "5000"
    env_file:
      - .env
    depends_on:
      db:
        condition: service_healthy
  db:
    image: postgres:16
    volumes:
      - postgres_data:/var/lib/postgresql/data
  nginx:
    image: nginx:1.27-alpine
    ports:
      - "8080:80"

volumes:
  postgres_data:
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Inspeccionemos nuestro `compose.yml` base:
> Contiene la arquitectura común a cualquier ambiente:
> - Define los tres servicios: `web`, `db` y `nginx`.
> - `web` expone internamente el puerto `5000` y depende del estado `healthy` de `db`.
> - `db` usa `postgres:16` y declara el volumen `postgres_data`.
> - `nginx` mapea el puerto `8080:80` hacia el host.
> Noten que aquí NO hay bind mounts locales ni configuraciones exclusivas de un solo entorno."

**👨‍💻 Acción en Consola / Pizarra:**
- Resaltar que el `compose.yml` base es agnóstico del ambiente donde se ejecute.

**💡 Tip de Gestión del Aula:**
- Mostrar la limpieza del manifiesto base.

---

### 📄 Diapositiva 8: Diferencias entre dev y prod
**Contenido de la PPT:**
```text
DIFERENCIAS ENTRE DEV Y PROD

compose.dev.yml (Desarrollo):
services:
  web:
    volumes:
      - ./app:/app
    environment:
      FLASK_ENV: development
      FLASK_DEBUG: "1"

compose.prod.yml (Producción):
services:
  web:
    image: usuario/flask-app:prod
    restart: unless-stopped
    environment:
      FLASK_ENV: production
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Comparemos los dos archivos de override en pantalla:
> - **En `compose.dev.yml`:** Inyectamos el Bind Mount `./app:/app` para que el desarrollador edite código en tiempo real y activamos `FLASK_DEBUG: "1"`.
> - **En `compose.prod.yml`:** Reemplazamos la compilación por la imagen precompilada en el registro `usuario/flask-app:prod`, agregamos `restart: unless-stopped` para que si el contenedor se cae Docker lo levante automáticamente, y definimos `FLASK_ENV: production`."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar cómo Compose fusiona los bloques YAML al ejecutarse con múltiples flags `-f`.

**💡 Tip de Gestión del Aula:**
- Explicar la regla de fusión: las propiedades especificadas en el segundo archivo pisan o se añaden a las del primero.

---

### 📄 Diapositiva 9: Comandos por entorno
**Contenido de la PPT:**
```text
COMANDOS POR ENTORNO

Desarrollo:
cp .env.dev .env
docker compose     -f compose.yml     -f compose.dev.yml     up -d --build

Producción local:
cp .env.prod .env
docker compose     -f compose.yml     -f compose.prod.yml     up -d

VALIDACIÓN: Ambos entornos deben responder desde http://localhost:8080, pero con configuración distinta.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Veamos cómo se ejecutan los comandos por entorno usando la opción **`-f`**:
> - **Para Desarrollo:** Copiamos `.env.dev` a `.env` y pasamos dos banderas `-f`:
>   `docker compose -f compose.yml -f compose.dev.yml up -d --build`
>   *Compose lee la base y aplica las modificaciones de desarrollo.*
> - **Para Producción:** Copiamos `.env.prod` a `.env` y ejecutamos:
>   `docker compose -f compose.yml -f compose.prod.yml up -d`
>   *Compose lee la base y aplica las reglas estrictas de producción.*"

**👨‍💻 Acción en Consola / Pizarra:**
```bash
# Probar sintaxis en desarrollo
cp .env.dev .env
docker compose -f compose.yml -f compose.dev.yml up -d --build
docker compose ps
```

**💡 Tip de Gestión del Aula:**
- Enfatizar el orden de las banderas `-f`: el archivo que se coloca en segundo lugar sobrescribe los valores del primero.

---

### 📄 Diapositiva 10: Bloque 2 — Limpieza del proyecto
**Contenido de la PPT:**
```text
Limpieza del proyecto
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 2: Limpieza del proyecto**. Vamos a aprender cómo mantener un servidor limpio sin borrar datos valiosos por descuido."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `Limpieza Selectiva = Mantener espacio libre sin destruir volúmenes de producción`.

**💡 Tip de Gestión del Aula:**
- Advertir sobre los peligros de ejecutar comandos de limpieza masiva a ciegas.

---

### 📄 Diapositiva 11: Qué significa limpiar en Docker
**Contenido de la PPT:**
```text
QUÉ SIGNIFICA LIMPIAR EN DOCKER
CUIDADO: Limpiar no siempre es borrar todo. Los volúmenes pueden contener datos importantes.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Tengan mucho **Cuidado con el término 'Limpiar' en Docker**:
> Al compilar e iterar repetidamente, Docker acumula recursos efímeros descartables (contenedores detenidos, redes en desuso, capas huérfanas o *dangling images*).
> Limpiar el servidor significa liberar ese espacio en disco descartable.
> **Pero ATENCIÓN:** Nunca ejecuten comandos de borrado de volúmenes (`volume prune` o `down -v`) en servidores donde residan bases de datos reales a menos que estén 100% seguros."

**👨‍💻 Acción en Consola / Pizarra:**
- Clasificar los recursos en la pizarra:
  - *Descartables:* Contenedores detenidos, redes huérfanas, imágenes sin tag (`dangling`).
  - *Valiosos / Críticos:* Volúmenes nombrados con datos SQL (`postgres_data`).

**💡 Tip de Gestión del Aula:**
- Preguntar si alguno ha borrado por error una base de datos local usando `down -v`.

---

### 📄 Diapositiva 12: Limpieza segura del stack
**Contenido de la PPT:**
```text
LIMPIEZA SEGURA DEL STACK
# Detener y eliminar contenedores/red
docker compose down

# Quitar contenedores huérfanos
docker compose down --remove-orphans

# Ver estado global
docker ps -a
docker images
docker volume ls

# Limpieza general segura
docker container prune
docker image prune
docker network prune

# CUIDADO: borra volúmenes no usados
docker volume prune
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los comandos de **Limpieza Segura del Stack**:
> 1. `docker compose down --remove-orphans`: Detiene los servicios y elimina contenedores huérfanos de ejecuciones o servicios anteriores que cambiaron de nombre.
> 2. `docker container prune`: Elimina solo los contenedores que están detenidos.
> 3. `docker image prune`: Elimina las imágenes huérfanas sin etiqueta (`<none>:<none>`).
> 4. `docker network prune`: Elimina redes virtuales sin uso.
> 5. **`docker volume prune` (CUIDADO EXTREMO):** Borra todos los volúmenes que no estén conectados a un contenedor activo en ese segundo."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker system df    # Muestra el espacio ocupado por categoría
docker image prune -f
```

**💡 Tip de Gestión del Aula:**
- Mostrar cómo `docker system df` ofrece una radiografía exacta del disco antes de limpiar.

---

### 📄 Diapositiva 13: Destruir todo para reconstruir desde cero
**Contenido de la PPT:**
```text
DESTRUIR TODO PARA RECONSTRUIR DESDE CERO
REGLA DE LABORATORIO FINAL: Este flujo debe dejar el proyecto funcional aunque la máquina empiece sin contenedores previos.

Comandos:
# 1. Bajar el stack y borrar volúmenes del proyecto
docker compose down -v --remove-orphans

# 2. Eliminar imagen local del proyecto si existe
docker image rm mi-flask:prod || true

# 3. Reconstruir desde cero
docker compose -f compose.yml -f compose.prod.yml up -d --build
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Regla de la Prueba de Fuego del Laboratorio Final**:
> Su proyecto debe ser tan profesional y reproducible que, si destruimos absolutamente todos sus contenedores, imágenes y volúmenes, debe poder reconstruirse y levantarse en 1 minuto ejecutando su secuencia de comandos.
> Prueben la secuencia de reset completo:
> `docker compose down -v --remove-orphans`
> `docker compose -f compose.yml -f compose.prod.yml up -d --build`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker compose down -v --remove-orphans
docker compose -f compose.yml -f compose.prod.yml up -d --build
docker compose ps
```

**💡 Tip de Gestión del Aula:**
- Verificar que los stacks de los alumnos se levanten limpios y funcionales.

---

### 📄 Diapositiva 14: Bloque 3 — Debugging profesional
**Contenido de la PPT:**
```text
Debugging profesional
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 3: Debugging profesional**. Vamos a repasar el orden de diagnóstico de fallas antes de modificar cualquier línea de código."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `Primero Diagnosticar (Logs/Inspect) -> Luego Mutar Código`.

**💡 Tip de Gestión del Aula:**
- Reiterar que adivinar las causas de los errores es la marca de un principiante.

---

### 📄 Diapositiva 15: Orden recomendado de diagnóstico
**Contenido de la PPT:**
```text
ORDEN RECOMENDADO DE DIAGNÓSTICO
REGLA PRÁCTICA: Primero mira qué está pasando; recién después cambia YAML, Dockerfile o código.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Regla Práctica de Debugging Profesional**:
> *'Primero inspecciona y lee las bitácoras para entender exactamente qué está sucediendo; recién después modifica tu archivo YAML, tu Dockerfile o tu código Python'*.
> Cambiar configuraciones al azar sin leer los logs suele generar más problemas de los que soluciona."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar la pirámide de troubleshooting en la pizarra.

**💡 Tip de Gestión del Aula:**
- Hacer reflexionar a los alumnos sobre el tiempo que ahorra leer el log exacto de la falla.

---

### 📄 Diapositiva 16: Herramientas de debugging
**Contenido de la PPT:**
```text
HERRAMIENTAS DE DEBUGGING
| COMANDO | PREGUNTA QUE RESPONDE | CUÁNDO USARLO |
|---|---|---|
| docker compose ps | ¿Qué servicio está arriba? | Primer chequeo |
| docker compose logs -f web | ¿Qué error imprime la app? | Fallas de arranque |
| docker inspect <id> | ¿Qué red, env y mounts tiene? | Configuración dudosa |
| docker compose exec web sh | ¿Qué pasa dentro del contenedor? | Pruebas manuales |
| docker stats | ¿Consume demasiados recursos? | Rendimiento básico |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos las **5 Herramientas de Debugging**:
> 1. `docker compose ps`: Responde qué servicios están activos, reiniciando o detenidos.
> 2. `docker compose logs -f web`: Revela la traza de la excepción o error de código.
> 3. `docker inspect`: Muestra las variables inyectadas, redes e IPs exactas.
> 4. `docker compose exec web sh`: Permite entrar al contenedor para hacer `curl` o pings internos.
> 5. `docker stats`: Muestra el consumo de RAM y CPU en tiempo real."

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar la tabla como referencia obligatoria de consulta.

**💡 Tip de Gestión del Aula:**
- Preguntar si tienen alguna duda sobre cómo ejecutar cualquiera de estas 5 herramientas.

---

### 📄 Diapositiva 17: Laboratorio: Diagnosticar el stack
**Contenido de la PPT:**
```text
LABORATORIO: DIAGNOSTICAR EL STACK
Comandos:
# Estado general
docker compose ps

# Logs por servicio
docker compose logs -f nginx
docker compose logs -f web
docker compose logs -f db

# Entrar a la app
docker compose exec web sh

# Probar desde dentro
env | grep DB_
curl http://localhost:5000

# Recursos
docker stats
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos la rutina del **Laboratorio de Diagnóstico**:
> 1. Verifiquen el estado general con `docker compose ps`.
> 2. Lean los logs de Nginx y de la app web: `docker compose logs -f web`.
> 3. Entren a la shell del servicio `web`: `docker compose exec web sh`.
> 4. Dentro del contenedor, inspeccionen las variables leídas: `env | grep DB_`.
> 5. Prueben la conectividad local interna: `curl http://localhost:5000`.
> 6. Salgan con `exit` y monitoreen recursos con `docker stats`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker compose ps
docker compose exec web sh
# Dentro del contenedor:
env | grep DB_
curl http://localhost:5000
exit
```

**💡 Tip de Gestión del Aula:**
- Mostrar cómo `env | grep DB_` permite confirmar al instante si las credenciales fueron leídas del `.env`.

---

### 📄 Diapositiva 18: Bloque 4 — Despliegue completo
**Contenido de la PPT:**
```text
Despliegue completo
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 4: Despliegue completo**. Vamos a construir el script Bash de automatización e integrar la arquitectura final."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `Automatización = Script desplegar.sh reproducible`.

**💡 Tip de Gestión del Aula:**
- Explicar la importancia de los scripts de automatización en pipelines de CI/CD.

---

### 📄 Diapositiva 19: Arquitectura final del curso
**Contenido de la PPT:**
```text
ARQUITECTURA FINAL DEL CURSO
RESULTADO FINAL:
Nginx actúa como proxy frontal en puerto 8080. Flask y PostgreSQL se ejecutan en la red interna aislada. Los datos de la base de datos se conservan en un volumen nombrado.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Arquitectura Final del Curso Docker desde Cero (10ma Edición 2026)**:
> - **Nginx:** Recibe las peticiones de los usuarios en `http://localhost:8080` y las enruta internamente.
> - **Flask Web:** Procesa la lógica de negocio en el puerto 5000 dentro de la red privada `backend`, sin exponer puertos directos al host.
> - **PostgreSQL 16:** Almacena los datos en la red privada `backend`, monitoreado por un Healthcheck `pg_isready` y persistido duraderamente en el volumen nombrado `postgres_data`."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar el esquema de arquitectura final completo en la pizarra con todos sus componentes.

**💡 Tip de Gestión del Aula:**
- Destacar cómo los alumnos han pasado de no conocer Docker a construir esta arquitectura completa de producción.

---

### 📄 Diapositiva 20: Script de despliegue final
**Contenido de la PPT:**
```text
SCRIPT DE DESPLIEGUE FINAL
#!/usr/bin/env bash
set -euo pipefail

cp .env.prod .env

docker compose     -f compose.yml     -f compose.prod.yml     down -v --remove-orphans

docker compose     -f compose.yml     -f compose.prod.yml     up -d --build

docker compose ps
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Analicemos nuestro **Script de Despliegue Final (`desplegar.sh`)**:
> - `#!/usr/bin/env bash`: Define el intérprete de comandos Bash.
> - `set -euo pipefail`: **Seguridad estricta en Bash**. Si un comando falla (`-e`), si se usa una variable no definida (`-u`) o si falla una tubería (`-o pipefail`), el script se detiene inmediatamente evitando desplegar estados corruptos.
> - Copia las variables de producción: `cp .env.prod .env`.
> - Apaga y limpia el stack anterior: `docker compose -f compose.yml -f compose.prod.yml down -v --remove-orphans`.
> - Reconstruye y levanta el stack actualizado: `docker compose -f compose.yml -f compose.prod.yml up -d --build`.
> - Muestra el estado final con `docker compose ps`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
# Otorgar permisos de ejecución y correr
chmod +x desplegar.sh
./desplegar.sh
```

**💡 Tip de Gestión del Aula:**
- Explicar por qué la bandera `set -euo pipefail` es una buena práctica obligatoria en scripts Bash profesionales.

---

### 📄 Diapositiva 21: Validación final
**Contenido de la PPT:**
```text
VALIDACIÓN FINAL
DEBE CUMPLIRSE:
• Nginx responde en puerto 8080.
• Flask corre sin exponer puerto directo.
• PostgreSQL conserva datos en volumen.
• El stack se reconstruye sin pasos manuales.

Comandos:
# 1. Ver servicios
docker compose ps

# 2. Probar endpoint
curl http://localhost:8080

# 3. Revisar logs
docker compose logs --tail=50 web
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Criterios de **Validación Final**:
> Su proyecto integrador final se considerará aprobado cuando cumpla estas 4 condiciones:
> 1. Nginx responde correctamente en `http://localhost:8080`.
> 2. Flask opera de forma aislada sin exponers directamente al host.
> 3. PostgreSQL mantiene los datos guardados en el volumen `postgres_data`.
> 4. Todo el stack se levanta automáticamente ejecutando `./desplegar.sh` sin requerir intervenciones manuales intermedias."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
./desplegar.sh
curl http://localhost:8080
docker compose logs --tail=50 web
```

**💡 Tip de Gestión del Aula:**
- Verificar que los 4 criterios de aceptación se cumplan en las pantallas de los estudiantes.

---

### 📄 Diapositiva 22: Errores frecuentes en el proyecto final
**Contenido de la PPT:**
```text
ERRORES FRECUENTES EN EL PROYECTO FINAL
| ERROR | CAUSA PROBABLE | SOLUCIÓN RÁPIDA |
|---|---|---|
| Usa configuración equivocada | Se mezcló .env.dev con prod | Copiar el .env correcto |
| Nginx no llega a Flask | Servicio o puerto incorrecto | Revisar proxy_pass y compose ps |
| BD inicia pero app falla | PostgreSQL no está listo | Healthcheck y logs de db |
| Datos desaparecen | Se ejecutó down -v | Restaurar backup o evitar borrar volumen |
| Rebuild no cambia nada | Caché o imagen antigua | Usar up -d --build y revisar tags |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos la tabla de **Resolución de Errores Frecuentes del Proyecto Final**:
> 1. **Configuración equivocada:** Olvidaron copiar `.env.prod`. Solución: Asegurar la copia en el script.
> 2. **Nginx no llega a Flask:** Typo en la directiva `proxy_pass http://web:5000;`.
> 3. **BD arranca pero la app cae:** La app intentó conectarse antes de que Postgres estuviera `healthy`.
> 4. **Los datos desaparecieron:** Ejecutaron `down -v` sin querer. Solución: Restaurar el backup con `psql < backups/appdb.sql`.
> 5. **Los cambios no se reflejan:** No agregaron la bandera `--build` al comando `up -d`."

**👨‍💻 Acción en Consola / Pizarra:**
- Dejar la tabla visible durante el tiempo de consultas finales.

**💡 Tip de Gestión del Aula:**
- Repasar las soluciones rápidas de cada error.

---

### 📄 Diapositiva 23: Checklist de aprendizaje — Sesión 6
**Contenido de la PPT:**
```text
CHECKLIST DE APRENDIZAJE — SESIÓN 6
✔ Puedo explicar por qué separar desarrollo y producción.
✔ Puedo combinar archivos Compose con -f compose.yml -f compose.prod.yml.
✔ Puedo limpiar recursos huérfanos sin borrar datos por accidente.
✔ Puedo diagnosticar fallas con estado, logs, inspect, exec y stats.
✔ Puedo destruir y reconstruir el stack completo desde cero.
✔ Puedo validar que Flask, PostgreSQL y Nginx funcionen como proyecto integrado.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos nuestro **Checklist de Aprendizaje de la Sesión 6**:
> Hoy pueden explicar por qué separar entornos, combinan archivos Compose con `-f`, limpian recursos de forma segura, diagnostican fallas con el protocolo de 5 pasos, destruyen y reconstruyen stacks reproducibles en minutos y han validado un proyecto integrador completo con Flask, PostgreSQL y Nginx.
> ¡Felicitaciones a todos!"

**👨‍💻 Acción en Consola / Pizarra:**
- Marcar los 6 checks finales en la pizarra.

**💡 Tip de Gestión del Aula:**
- Reconocer el gran esfuerzo de los estudiantes a lo largo del curso.

---

### 📄 Diapositiva 24: Resumen de la Sesión 6
**Contenido de la PPT:**
```text
RESUMEN DE LA SESIÓN 6
1. La sesión 6 es mayormente práctica e integradora; la teoría se limita a dev/prod, limpieza y debugging.
2. Multi-entorno permite reutilizar una base Compose y aplicar cambios por contexto.
3. La limpieza debe distinguir entre recursos descartables y volúmenes con datos.
4. Debugging profesional sigue un orden: estado, logs, inspect, exec y recursos.
5. El proyecto final debe reconstruirse desde cero con comandos reproducibles.

RESULTADO DEL CURSO:
Aplicación Flask + PostgreSQL + Nginx containerizada, con entornos dev/prod y despliegue reproducible.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Sinteticemos las **5 Conclusiones Clave de la Sesión 6**:
> 1. Integramos práctica, teoría de entornos y automatización.
> 2. Reutilizamos la base Compose adaptándola a dev o prod.
> 3. Limpiamos con responsabilidad separando recursos de volúmenes.
> 4. Diagnosticamos metodológicamente.
> 5. Logramos un proyecto 100% reproducible.
>
> **Resultado del Curso:** Han construido una infraestructura completa de producción con Nginx, Flask y PostgreSQL en contenedores Docker."

**👨‍💻 Acción en Consola / Pizarra:**
- Resaltar el Resultado del Curso en la pizarra.

**💡 Tip de Gestión del Aula:**
- Transición hacia el resumen general de todo el programa PIT 2026.

---

### 📄 Diapositiva 25: Resumen final del programa
**Contenido de la PPT:**
```text
RESUMEN FINAL DEL PROGRAMA
• Docker resuelve la reproducibilidad entre entornos.
• Imágenes y contenedores son la base del flujo.
• Dockerfile permite construir imágenes propias.
• Compose levanta stacks multi-contenedor.
• Redes y volúmenes ordenan comunicación y datos.
• Nginx actúa como punto de entrada del stack.
• Multi-stage reduce tamaño y superficie de ataque.
• Variables y archivos .env separan configuración.
• Logs, inspect, exec y stats ayudan a depurar.
• Dev/prod se separan con archivos Compose por entorno.

RESULTADO FINAL:
Aplicación completa: Flask, PostgreSQL y Nginx containerizados, listos para dev/prod y levantables en minutos.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Repasemos la **Escalera Completa del Aprendizaje del Curso Docker desde Cero (PIT 2026)**:
> - **Sesión 1:** Entendimos la contenerización y los comandos básicos (`run`, `ps`, `stop`, `rm`).
> - **Sesión 2:** Escribimos nuestras primeras recetas `Dockerfile` y publicamos en Docker Hub.
> - **Sesión 3:** Unificamos múltiples servicios con `docker compose`.
> - **Sesión 4:** Aislamos redes y aseguramos la persistencia con `volumes` y backups `pg_dump`.
> - **Sesión 5:** Colocamos `Nginx` como Reverse Proxy e implementamos `Multi-stage builds`.
> - **Sesión 6:** Estructuramos pipelines multi-entorno (`dev`/`prod`) y automatizamos el despliegue.
>
> Hoy cada uno de ustedes domina el estándar de contenedores de la industria tecnológica."

**👨‍💻 Acción en Consola / Pizarra:**
- Repasar los 10 hitos del resumen final en la pizarra.

**💡 Tip de Gestión del Aula:**
- Invitar a los alumnos a incluir este proyecto en sus portafolios de GitHub y currículums.

---

### 📄 Diapositiva 26: ¡Muchas gracias! — Preguntas y Respuestas
**Contenido de la PPT:**
```text
¡MUCHAS GRACIAS!
Preguntas y Respuestas

DOCKER DESDE CERO: Crea y Despliega Aplicaciones
Docente: Cristian Jampier Chileno Segundo
Programa de Iniciación Tecnológica (PIT 2026)
Oficina de Tecnologías de la Información (OTI - UNI)
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Llegamos al final de nuestro curso.
> Quiero agradecer sinceramente a cada uno de ustedes por su dedicación, puntualidad y esfuerzo a lo largo de estas 6 sesiones del **Programa de Iniciación Tecnológica (PIT 2026)** de la Universidad Nacional de Ingeniería.
> Mi nombre es **Cristian Jampier Chileno Segundo** y ha sido un honor inmenso ser su instructor.
> Quedo a su entera disposición para responder las preguntas finales sobre el examen y la entrega del proyecto integrador.
> ¡Muchos éxitos en su carrera profesional y nos vemos en los próximos programas de la OTI-UNI! ¡Hasta pronto!"

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar los datos de contacto, repositorio oficial de GitHub y abrir la ronda final de preguntas y respuestas.

**💡 Tip de Gestión del Aula:**
- Brindar un aplauso virtual/presencial al grupo y dar las indicaciones para la obtención del certificado del curso.
