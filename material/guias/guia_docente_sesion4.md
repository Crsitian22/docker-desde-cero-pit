# 🎙️ Guía Docente Diapositiva por Diapositiva — Sesión 4: Redes, Volúmenes y Persistencia
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Instructor:** Cristian Jampier Chileno Segundo | OTI - UNI  
**Programa:** Programa de Iniciación Tecnológica (PIT 2026) — Universidad Nacional de Ingeniería  
**Total Diapositivas:** 28 Diapositivas  

---

## 🎯 Instrucciones de Orientación Pedagógica
Esta guía contiene la explicación detallada y el guión profesional en primera persona para abordar **cada una de las 28 diapositivas** de la presentación oficial de la Sesión 4.
Está diseñada para guiar la clase paso a paso, enseñando a gestionar redes en Docker, diferenciar comunicación interna de puertos publicados, aislar bases de datos perimetralmente, elegir entre Volúmenes Nombrados y Bind Mounts, configurar Healthchecks con `pg_isready` y ejecutar backups/restauraciones duraderas con `pg_dump`.

---

## 🖥️ Explicación Diapositiva por Diapositiva (1 a 28)

### 📄 Diapositiva 1: DOCKER DESDE CERO: Crea y Despliega Aplicaciones — Sesión 4
**Contenido de la PPT:**
```text
DOCKER DESDE CERO: Crea y Despliega Aplicaciones
INSTRUCTOR: Cristian Jampier Chileno Segundo
PROGRAMA DE INICIACIÓN TECNOLÓGICA — PIT 2026
Oficina de Tecnologías de la Información (OTI - UNI)
Programa Completo — PIT 2026
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Muy buenos días/tardes a todos. Bienvenidos a la **Sesión 4** del curso *Docker desde Cero: Crea y Despliega Aplicaciones*, organizado por la OTI-UNI.
> En la sesión anterior aprendimos a levantar stacks multi-contenedor con Docker Compose. Hoy resolveremos dos aspectos fundamentales de producción: la **seguridad de las redes de comunicación interna** y la **persistencia duradera de los datos**. Aprenderemos a aislar la base de datos de internet, a configurar volúmenes persistentes, a implementar Healthchecks de salud y a automatizar respaldos SQL."

**👨‍💻 Acción en Consola / Pizarra:**
- Proyectar la portada del curso y recordar la ruta del repositorio en GitHub: `https://github.com/Crsitian22/docker-desde-cero-pit`.

**💡 Tip de Gestión del Aula:**
- Preguntar al grupo: *"¿Qué pasaría con la información de sus clientes si un contenedor de PostgreSQL se borra y no configuraron un volumen?"*

---

### 📄 Diapositiva 2: SESIÓN 4 — Índice del Temario
**Contenido de la PPT:**
```text
SESIÓN 4
1. Redes Docker
2. Puertos Publicados vs. Internos
3. Volúmenes Nombrados
4. Bind Mounts
5. Healthchecks
6. Backup y Restauración
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los 6 ejes temáticos de esta cuarta sesión:
> 1. En **Redes Docker**, entenderemos cómo se comunican los contenedores a nivel de Kernel.
> 2. Analizaremos **Puertos Publicados vs. Internos** y el principio de menor exposición.
> 3. Implementaremos **Volúmenes Nombrados** para almacenar bases de datos.
> 4. Configuraremos **Bind Mounts** para desarrollo ágil en caliente.
> 5. Configuraremos **Healthchecks** para monitorear si un servicio está saludable.
> 6. Y ejecutaremos la secuencia de **Backup y Restauración** con `pg_dump` y `psql`."

**👨‍💻 Acción en Consola / Pizarra:**
- Anotar el mapa conceptual en la pizarra: `Redes Aisladas + Volúmenes Nombrados + Healthchecks + Backups SQL`.

**💡 Tip de Gestión del Aula:**
- Indicar a los estudiantes que esta clase junta conceptos de redes, almacenamiento y seguridad de infraestructura.

---

### 📄 Diapositiva 3: Objetivo de la Sesión 4
**Contenido de la PPT:**
```text
Objetivo de la sesión 4:
Al terminar la sesión 4 podrás:
• Explicar cómo se comunican contenedores mediante redes Docker.
• Diferenciar red interna, puertos publicados y nombres de servicio.
• Usar volúmenes nombrados y bind mounts para persistencia.
• Aislar servicios internos como bases de datos.
• Agregar healthchecks para validar disponibilidad.
• Realizar backup y restauración básica de datos del proyecto.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Nuestro **Objetivo de la Sesión 4** es muy claro:
> Al finalizar esta clase, cada uno de ustedes sabrá aislar PostgreSQL retirando sus puertos públicos, configurará volúmenes declarados en Compose para resguardar la información ante reinicios, sabrá medir la salud real del motor con `pg_isready` y ejecutará scripts de backup duraderos en archivos `.sql`."

**👨‍💻 Acción en Consola / Pizarra:**
- Subrayar las palabras **PERSISTENCIA** y **AISLAMIENTO PERIMETRAL**.

**💡 Tip de Gestión del Aula:**
- Motivar a los alumnos: *"Hoy dejarán de perder datos en sus bases de datos Docker"*.

---

### 📄 Diapositiva 4: Bloque 1 — Redes Docker
**Contenido de la PPT:**
```text
Redes Docker
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Iniciamos el **Bloque 1: Redes Docker**. Vamos a analizar el funcionamiento del motor de red virtual interna de Docker y cómo se descubren los servicios."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar una nube de red interna en la pizarra conectando los servicios `web` y `db`.

**💡 Tip de Gestión del Aula:**
- Recordar que en Docker Compose no hace falta configurar direcciones IP fijas manualmente.

---

### 📄 Diapositiva 5: Qué problema resuelven las redes
**Contenido de la PPT:**
```text
Qué problema resuelven las redes
• Los contenedores necesitan comunicarse sin depender de IPs manuales.
• Compose crea una red interna por proyecto automáticamente.
• Cada servicio puede resolverse por su nombre: web, db, cache.
• Solo publicamos hacia el host lo que debe ser accesible desde fuera.

IDEA CLAVE: Dentro de la red Docker, el nombre del servicio funciona como DNS interno.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Analicemos **Qué problema resuelven las redes**:
> Cuando lanzas contenedores, Docker les asigna direcciones IP virtuales dinámicas (por ejemplo `172.18.0.2` o `172.18.0.3`). Si un contenedor se reinicia, su IP puede cambiar. Si hubieras escrito la IP fija en tu código, la conexión fallaría.
> **La Idea Clave:** Las redes de Docker y Docker Compose crean un **resolvedor DNS interno**. El servicio web simplemente consulta a `db`, y el DNS de Docker devuelve la IP actual del contenedor de PostgreSQL automáticamente."

**👨‍💻 Acción en Consola / Pizarra:**
- Ilustrar el resolvedor DNS de Docker:
  `web -> Consulta 'db' -> DNS de Docker (127.0.0.11) -> IP 172.18.0.3`.

**💡 Tip de Gestión del Aula:**
- Hacer notar cómo la abstracción de nombres facilita la escalabilidad.

---

### 📄 Diapositiva 6: Red interna vs Puerto publicado
**Contenido de la PPT:**
```text
RED INTERNA VS PUERTO PUBLICADO
REGLA PRÁCTICA:
Publica la app web si necesitas navegador. No publiques la base de datos si solo la consume otro contenedor.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Regla Práctica de Seguridad Perimetral**:
> - **Puerto Publicado (`ports:`):** Abre un túnel entre el puerto del host (tu laptop/servidor) y el contenedor. Debe usarse ÚNICAMENTE para los servicios que el usuario final debe acceder desde su navegador o cliente externo (ej. la app web en puerto 5000 o Nginx en puerto 80).
> - **Red Interna:** Todos los contenedores del mismo Compose ya se comunican libremente entre sí en todos sus puertos internos.
> **Por lo tanto:** La base de datos PostgreSQL debe permanecer dentro de la red interna SIN exponer su puerto 5432 al exterior."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar el perímetro de seguridad:
  `Usuario Internet -> [App Web :5000 (PÚBLICO)] <---Red Interna---> [PostgreSQL :5432 (PRIVADO / SIN PORTS)]`

**💡 Tip de Gestión del Aula:**
- Preguntar: *"Si no publicamos el puerto 5432 de Postgres, ¿un hacker desde internet puede intentar contraseñas a nuestra BD?"* (Respuesta: No, porque el puerto no está abierto en la interfaz física del servidor).

---

### 📄 Diapositiva 7: Definir una red explícita en Compose
**Contenido de la PPT:**
```text
DEFINIR UNA RED EXPLÍCITA EN COMPOSE
CUÁNDO HACERLO: Define redes explícitas para separar tráfico o documentar mejor la arquitectura.

Ejemplo:
services:
  web:
    build: .
    networks:
      - backend
  db:
    image: postgres:16
    networks:
      - backend

networks:
  backend:
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Aunque Compose crea una red por defecto, en arquitecturas profesionales podemos **definir redes explícitas**:
> Declaramos la red `backend:` en la sección raíz `networks:`, y luego se la asignamos a los servicios `web` y `db` con `networks: - backend`.
> Esto nos permite segmentar el tráfico, crear múltiples redes aisladas (ej. `frontend` y `backend`) y documentar la arquitectura de forma declarativa."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar la sintaxis YAML de la sección `networks:` raíz y dentro de cada servicio.

**💡 Tip de Gestión del Aula:**
- Explicar que un servicio conectado a la red `frontend` no podrá comunicarse con uno conectado únicamente a `backend`.

---

### 📄 Diapositiva 8: Comandos útiles para redes
**Contenido de la PPT:**
```text
COMANDOS ÚTILES PARA REDES
| COMANDO | USO |
|---|---|
| docker network ls | Lista redes existentes |
| docker network inspect <red> | Muestra contenedores conectados e IPs |
| docker compose ps | Relaciona servicios y puertos publicados |
| docker compose exec web sh | Permite probar conectividad desde el servicio |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los **Comandos Útiles para Redes**:
> 1. `docker network ls`: Muestra las redes virtuales activas en el motor de Docker.
> 2. `docker network inspect <red>`: Muestra los detalles JSON de la red, incluyendo las IPs asignadas a cada contenedor.
> 3. `docker compose ps`: Muestra los puertos expuestos hacia el host.
> 4. `docker compose exec web sh`: Permite entrar al contenedor `web` para probar pings internos hacia `db`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker network ls
docker network inspect sesion4_default
```

**💡 Tip de Gestión del Aula:**
- Mostrar cómo el comando `docker network inspect` revela la subred IP (ej. `172.18.0.0/16`).

---

### 📄 Diapositiva 9: Bloque 2 — Volúmenes y persistencia
**Contenido de la PPT:**
```text
Volúmenes y persistencia
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 2: Volúmenes y persistencia**. Vamos a resolver el dilema de la volatilidad del almacenamiento dentro de los contenedores."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `Contenedor = Efímero` | `Volumen = Persistente`.

**💡 Tip de Gestión del Aula:**
- Indicar que comprender la diferencia entre Volúmenes Nombrados y Bind Mounts es clave para la administración de servidores.

---

### 📄 Diapositiva 10: Por qué se pierden datos
**Contenido de la PPT:**
```text
Por qué se pierden datos
• Un contenedor es reemplazable: puede eliminarse y recrearse.
• Los datos escritos dentro del filesystem del contenedor no son una estrategia durable.
• Las bases de datos necesitan almacenamiento externo al ciclo de vida del contenedor.
• Docker ofrece volúmenes y bind mounts para resolverlo.

REGLA MENTAL: Contenedor reemplazable; datos persistentes.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Entendamos **Por qué se pierden los datos**:
> Los contenedores están diseñados para ser efímeros e inmutables. Al borrar un contenedor con `docker rm`, su capa de escritura temporal se destruye por completo.
> Si escribes información de tu base de datos dentro del filesystem interno del contenedor, cuando actualices la imagen o recrees el contenedor, **todos los datos desaparecerán**.
> **Regla Mental:** *El contenedor es reemplazable y desechable; los datos deben ser persistentes y externos al contenedor*."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar la separación:
  `[ Contenedor Efímero (Desechable) ] <==== Montaje ====> [ Volumen Persistente (Disco Host) ]`

**💡 Tip de Gestión del Aula:**
- Hacer la analogía: *"El contenedor es una computadora alquilada; el volumen es tu disco duro externo donde guardas tus documentos reales"*.

---

### 📄 Diapositiva 11: Volumen nombrado vs Bind mount
**Contenido de la PPT:**
```text
VOLUMEN NOMBRADO VS BIND MOUNT
ANALOGÍA: El contenedor es una laptop prestada; el volumen es el disco externo donde guardas lo importante.

| TIPO | VENTAJAS | CUÁNDO USARLO |
|---|---|---|
| Volumen nombrado | Almacenamiento administrado por Docker | Datos de bases de datos |
| Bind mount | Carpeta local montada en el contenedor | Desarrollo y edición de código |
| Sin volumen | Datos dentro del contenedor | Solo pruebas descartables |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Comparemos los dos tipos de persistencia que ofrece Docker:
> 1. **Volumen Nombrado (Named Volume):** Es una unidad de almacenamiento gestionada al 100% por Docker en una ruta reservada del motor (`/var/lib/docker/volumes/`). Ofrece el máximo rendimiento I/O y está aislado de modificaciones accidentales del usuario. **Ideal para bases de datos (PostgreSQL, MySQL, MongoDB)**.
> 2. **Bind Mount:** Enlaza de forma directa una carpeta exacta de tu laptop (ej. `./app`) con un directorio dentro del contenedor (`/app`). Cualquier cambio en tu IDE se refleja al instante. **Ideal para desarrollo de código fuente**."

**👨‍💻 Acción en Consola / Pizarra:**
- Resumir en la pizarra:
  - `Volumen Nombrado` -> Manejado por Docker -> Bases de Datos en Producción y Dev.
  - `Bind Mount` -> Manejado por el Usuario -> Código Fuente en Desarrollo (Hot-Reload).

**💡 Tip de Gestión del Aula:**
- Verificar que entiendan por qué NO usamos bind mounts para bases de datos pesadas en producción (por temas de permisos y performance del SO host).

---

### 📄 Diapositiva 12: Volumen nombrado para PostgreSQL
**Contenido de la PPT:**
```text
VOLUMEN NOMBRADO PARA POSTGRESQL
CLAVE: Si eliminas el contenedor, el volumen puede seguir existiendo y conservar los datos.

Ejemplo:
services:
  db:
    image: postgres:16
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Veamos cómo se declara un **Volumen Nombrado** en Compose:
> En el servicio `db` añadimos el montaje `postgres_data:/var/lib/postgresql/data`.
> La ruta `/var/lib/postgresql/data` es donde PostgreSQL almacena físicamente las tablas y archivos de la BD dentro del contenedor.
> Luego debemos declarar obligatoriamente el nombre `postgres_data:` en la sección raíz `volumes:`.
> **La clave:** Si ejecutas `docker compose down`, los contenedores se borran, pero el volumen `postgres_data` permanece intacto. Al hacer `docker compose up` de nuevo, PostgreSQL volverá a montar los mismos datos sin perder nada."

**👨‍💻 Acción en Consola / Pizarra:**
- Señalar en el YAML la correspondencia entre la sección `volumes:` del servicio y la sección `volumes:` del nivel raíz.

**💡 Tip de Gestión del Aula:**
- Advertir a los alumnos: *"Cuidado con `docker compose down -v`. El flag `-v` sí elimina los volúmenes nombrados del proyecto"*.

---

### 📄 Diapositiva 13: Bind mount para desarrollo
**Contenido de la PPT:**
```text
BIND MOUNT PARA DESARROLLO
USO TÍPICO: Montar código local dentro del contenedor para desarrollo. Para producción, normalmente se prefiere copiar el código en la imagen.

Ejemplo:
services:
  web:
    build: .
    volumes:
      - ./app:/app
    ports:
      - "5000:5000"
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Veamos cómo se declara un **Bind Mount** en Compose para desarrollo:
> En el servicio `web` escribimos: `volumes: - ./app:/app`.
> El punto `./app` indica la carpeta local en tu laptop.
> `/app` es la carpeta interna dentro del contenedor.
> Gracias a este montaje, cuando edites el archivo `app.py` en tu VS Code de Windows/macOS, el archivo cambiará inmediatamente dentro del contenedor sin necesidad de ejecutar `docker build` de nuevo."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar cómo la sintaxis con punto y barra `./ruta_local:ruta_contenedor` distingue a un Bind Mount de un Volumen Nombrado.

**💡 Tip de Gestión del Aula:**
- Recordar que en producción el código se copia mediante `COPY` en el Dockerfile para generar imágenes cerradas e inmutables.

---

### 📄 Diapositiva 14: Comandos útiles para volúmenes
**Contenido de la PPT:**
```text
COMANDOS ÚTILES PARA VOLÚMENES
| COMANDO | USO |
|---|---|
| docker volume ls | Lista volúmenes nombrados |
| docker volume inspect <volumen> | Muestra detalles del volumen |
| docker compose down | Borra contenedores y red, conserva volúmenes |
| docker compose down -v | Borra también los volúmenes del proyecto |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos los **Comandos Útiles para Volúmenes**:
> 1. `docker volume ls`: Muestra todos los volúmenes nombrados gestionados por Docker.
> 2. `docker volume inspect <volumen>`: Muestra la ruta física en el disco del host donde se guardan los archivos (`Mountpoint`).
> 3. `docker compose down`: Elimina contenedores y redes del stack, pero **RESPETA Y CONSERVA los volúmenes**.
> 4. `docker compose down -v`: Elimina contenedores, redes **Y TAMBIÉN DESTRUYE LOS VOLÚMENES Y DATOS del proyecto**."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker volume ls
docker volume inspect sesion4_postgres_data
```

**💡 Tip de Gestión del Aula:**
- Enfatizar la precaución necesaria antes de escribir `down -v` en servidores de producción.

---

### 📄 Diapositiva 15: Bloque 3 — Servicios internos
**Contenido de la PPT:**
```text
Servicios internos
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 3: Servicios internos**. Vamos a reforzar el principio de arquitectura segura retirando la exposición de puertos innecesarios."

**👨‍💻 Acción en Consola / Pizarra:**
- Dibujar un candado de seguridad sobre el contenedor de PostgreSQL en la pizarra.

**💡 Tip de Gestión del Aula:**
- Explicar la frase *Hardening de Infraestructura*.

---

### 📄 Diapositiva 16: Qué servicios deben ser internos
**Contenido de la PPT:**
```text
QUÉ SERVICIOS DEBEN SER INTERNOS
REGLA PRÁCTICA: Si el usuario no necesita entrar directamente, no publiques el puerto.

• La app web suele publicar un puerto para el navegador.
• La base de datos normalmente solo debe recibir tráfico desde la app.
• Redis, workers y colas suelen ser servicios internos.
• Menos puertos publicados significa menor superficie de exposición.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos **Qué servicios deben ser internos**:
> En una arquitectura profesional:
> - **Servicios Públicos:** La app web o el Proxy Nginx (necesitan puertos mapeados hacia el host para ser visitados por los usuarios).
> - **Servicios Internos:** La base de datos (PostgreSQL), el caché (Redis), los workers y colas de mensajes.
> **Regla de Hardening:** Si un servicio no necesita ser accedido directamente por el usuario desde fuera, **NO expongan su puerto**. Reducir el número de puertos abiertos minimiza la superficie de ataque del servidor."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar en la pizarra el concepto de Superficie de Ataque:
  - 5 Puertos Abiertos (80, 5000, 5432, 6379, 22) -> Riesgo Alto.
  - 1 Puerto Abierto (80) + Red Interna Aislada -> Riesgo Mínimo.

**💡 Tip de Gestión del Aula:**
- Preguntar si un desarrollador necesita conectarse a la BD en producción directamente desde su laptop (Respuesta: No, usa túneles SSH o herramientas de administración internas).

---

### 📄 Diapositiva 17: Base de datos interna en Compose
**Contenido de la PPT:**
```text
BASE DE DATOS INTERNA EN COMPOSE
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
  db:
    image: postgres:16
    # Sin ports: no se expone al host

LECTURA: web está publicado para el navegador. db solo está disponible dentro de la red Docker del proyecto.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Observen la lectura de este manifiesto Compose:
> En el servicio `web` tenemos la directiva `ports: - "5000:5000"`, lo que permite que nuestro navegador web abra la aplicación.
> En el servicio `db` **hemos omitido por completo la clave `ports:`**.
> PostgreSQL sigue escuchando en su puerto 5432 interno dentro de la red del proyecto Compose, de modo que `web` puede realizar consultas SQL sin ningún problema, pero nadie desde internet puede conectarse directamente a PostgreSQL."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar en la consola con `docker compose ps` cómo `db` no tiene puertos mapeados hacia el Host.

**💡 Tip de Gestión del Aula:**
- Hacer notar cómo eliminar la línea `ports:` en `db` mejora instantáneamente la seguridad sin cambiar el código de la app.

---

### 📄 Diapositiva 18: Bloque 4 — Healthchecks y backup
**Contenido de la PPT:**
```text
Healthchecks y backup
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 4: Healthchecks y backup**. Aprenderemos a verificar el estado de salud de nuestros servicios y a crear copias de respaldo exportables."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir en la pizarra: `Healthcheck = Diagnóstico Automático` | `Backup = Copia SQL Exportable`.

**💡 Tip de Gestión del Aula:**
- Preguntar cuántos han visto un contenedor en estado `running` pero cuyo servicio fallaba al responder peticiones.

---

### 📄 Diapositiva 19: Por qué usar healthchecks
**Contenido de la PPT:**
```text
POR QUÉ USAR HEALTHCHECKS
IDEA CLAVE: running no siempre significa healthy.

• Un contenedor puede estar encendido pero no listo.
• PostgreSQL puede tardar segundos en aceptar conexiones.
• Un healthcheck permite declarar cómo verificar el estado real.
• Mejora la observabilidad durante laboratorios y despliegues.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Esta es la **Idea Clave de la Observabilidad**:
> **`running` NO siempre significa `healthy`**.
> Cuando el motor de Docker muestra que un contenedor está en estado `running`, solo indica que su proceso principal no se ha cerrado. Pero la base de datos dentro del contenedor puede estar recuperando archivos o iniciando sockets y aún no acepta conexiones SQL.
> Un **Healthcheck** es un comando de diagnóstico interno que Docker ejecuta periódicamente (ej. cada 10 segundos) para determinar si el servicio está verdaderamente saludable (`healthy`) y listo para recibir tráfico."

**👨‍💻 Acción en Consola / Pizarra:**
- Escribir los 3 estados de salud de un contenedor:
  - `starting` (Inicializando).
  - `healthy` (Saludable y listo).
  - `unhealthy` (Con fallas o no responde).

**💡 Tip de Gestión del Aula:**
- Mostrar cómo el estado de salud se puede ver con `docker compose ps`.

---

### 📄 Diapositiva 20: Healthcheck para PostgreSQL
**Contenido de la PPT:**
```text
HEALTHCHECK PARA POSTGRESQL
LECTURA: Docker ejecuta pg_isready. Si responde correctamente, marca el servicio como saludable.

Ejemplo:
services:
  db:
    image: postgres:16
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U appuser -d appdb"]
      interval: 10s
      timeout: 5s
      retries: 5
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Analicemos la configuración del **Healthcheck para PostgreSQL**:
> - `test:` Ejecuta la utilidad nativa `pg_isready` pasándole el usuario y la base de datos. Si la base de datos acepta conexiones, la herramienta devuelve un código de salida 0 (éxito).
> - `interval: 10s`: Ejecuta la prueba de salud cada 10 segundos.
> - `timeout: 5s`: Espera máximo 5 segundos por cada prueba.
> - `retries: 5`: Si falla 5 veces consecutivas, el motor marca el contenedor en estado `unhealthy`."

**👨‍💻 Acción en Consola / Pizarra:**
```yaml
db:
  image: postgres:16
  healthcheck:
    test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
    interval: 10s
    timeout: 5s
    retries: 5
```

**💡 Tip de Gestión del Aula:**
- Mostrar cómo la app web puede usar `depends_on: db: condition: service_healthy` para esperar a que Postgres esté totalmente listo.

---

### 📄 Diapositiva 21: Backup básico de PostgreSQL
**Contenido de la PPT:**
```text
BACKUP BÁSICO DE POSTGRESQL
REGLA PRÁCTICA: Un volumen conserva datos localmente, pero backup significa tener una copia exportable fuera del contenedor.

Comandos:
# Crear carpeta local para backups
mkdir backups

# Exportar datos desde el servicio db
docker compose exec -T db pg_dump     -U appuser appdb > backups/appdb.sql
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Llegamos a la práctica de **Backup Básico de PostgreSQL**:
> **Diferencia conceptual fundamental:** Un volumen nombrado conserva los datos dentro del servidor Docker, pero si el disco duro falla o necesitamos mover la base de datos a otro servidor, necesitamos una **copia de respaldo exportable (Dump SQL)**.
> Para respaldar la base de datos en caliente ejecutamos:
> `docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql`.
> **Detalle técnico vital:** Usamos el flag **`-T`** para desactivar la asignación de un terminal TTY interactivo, permitiendo que la salida binaria o SQL del comando se redirija limpiamente a nuestro archivo local `backups/appdb.sql`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
mkdir -p backups
docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql
cat backups/appdb.sql
```

**💡 Tip de Gestión del Aula:**
- Remarcar la importancia del flag `-T`: sin este flag, el archivo de backup contendrá caracteres invisibles de consola que corruptan la restauración.

---

### 📄 Diapositiva 22: Restaurar información
**Contenido de la PPT:**
```text
RESTAURAR INFORMACIÓN
ANTES DE RESTAURAR: Verifica que el servicio db esté arriba, que el usuario sea correcto y que el archivo exista en tu máquina.

Comando:
# Restaurar desde el archivo SQL
docker compose exec -T db psql     -U appuser appdb < backups/appdb.sql
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Veamos el procedimiento inverso: **Restaurar la Información**:
> Si necesitamos recuperar un respaldo previo o migrar datos a un servidor nuevo, enviamos de regreso el archivo `.sql` hacia el servicio PostgreSQL activo:
> `docker compose exec -T db psql -U appuser appdb < backups/appdb.sql`.
> El comando lee el archivo local `backups/appdb.sql` y lo inyecta dentro de la utilitaria `psql` del contenedor, recreando todas las tablas y registros al instante."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
# Restauración paso a paso
docker compose exec -T db psql -U appuser appdb < backups/appdb.sql
```

**💡 Tip de Gestión del Aula:**
- Demostrar el flujo completo: insertar datos -> hacer backup -> borrar volumen -> restaurar backup -> verificar datos.

---

### 📄 Diapositiva 23: Bloque 5 — Laboratorio datos y redes
**Contenido de la PPT:**
```text
Laboratorio datos y redes
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ingresamos al **Bloque 5: Laboratorio datos y redes**. Vamos a ejecutar la práctica completa en la consola."

**👨‍💻 Acción en Consola / Pizarra:**
- Abrir la terminal en la carpeta `codigo/sesion4`.

**💡 Tip de Gestión del Aula:**
- Verificar que los estudiantes tengan su archivo `.env` listo.

---

### 📄 Diapositiva 24: Flujo del laboratorio
**Contenido de la PPT:**
```text
FLUJO DEL LABORATORIO
META:
Mejorar el stack Flask + PostgreSQL para que la base de datos sea interna, persistente y respaldable.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Nuestra **Meta del Laboratorio**:
> Vamos a tomar la app de la Sesión 4, configuraremos PostgreSQL como un servicio interno sin puertos expuestos, le asignaremos un volumen nombrado para persistencia, agregaremos healthcheck y ejecutaremos la secuencia de backup y restauración."

**👨‍💻 Acción en Consola / Pizarra:**
- Mostrar en VS Code los archivos del laboratorio `codigo/sesion4`.

**💡 Tip de Gestión del Aula:**
- Indicar que sigan los comandos paso a paso.

---

### 📄 Diapositiva 25: Comandos del laboratorio
**Contenido de la PPT:**
```text
COMANDOS DEL LABORATORIO
# 1. Levantar stack
docker compose up -d --build

# 2. Revisar puertos
docker compose ps

# 3. Inspeccionar red
docker network ls
docker network inspect <red>

# 4. Ver volúmenes
docker volume ls

# 5. Backup
mkdir backups
docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Ejecutemos la secuencia del laboratorio:
> 1. Levanten el stack: `docker compose up -d --build`.
> 2. Verifiquen puertos con `docker compose ps` (verán que `db` no publica puertos hacia el host).
> 3. Inspeccionen la red con `docker network ls` y `docker network inspect sesion4_backend`.
> 4. Verifiquen el volumen persistente con `docker volume ls`.
> 5. Creen un registro de prueba ingresando a `http://localhost:5000/add`.
> 6. Ejecuten el backup: `docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql`."

**👨‍💻 Acción en Consola / Pizarra:**
```bash
docker compose up -d --build
docker compose ps
docker volume ls
mkdir -p backups
docker compose exec -T db pg_dump -U appuser appdb > backups/appdb.sql
```

**💡 Tip de Gestión del Aula:**
- Confirmar que el archivo `backups/appdb.sql` se ha generado correctamente en el explorador de archivos local.

---

### 📄 Diapositiva 26: Errores frecuentes en datos y redes
**Contenido de la PPT:**
```text
ERRORES FRECUENTES EN DATOS Y REDES
| ERROR | CAUSA PROBABLE | SOLUCIÓN RÁPIDA |
|---|---|---|
| App no conecta a BD | Host incorrecto o red distinta | Usar db y misma red |
| BD expuesta al host | Se agregó ports en db | Quitar ports si no es necesario |
| Datos desaparecen | Sin volumen persistente | Agregar volumen nombrado |
| Backup falla | Usuario o BD incorrectos | Revisar DB_USER y DB_NAME |
| Servicio no está listo | Falta healthcheck o espera | Revisar logs y estado healthy |
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos la tabla de **Resolución de Errores Frecuentes**:
> 1. **App no conecta:** Mismatch de red o host. Usen el hostname `db` dentro de la misma red.
> 2. **BD expuesta:** Mantienen `ports:` en `db`. Solución: Quiten la clave `ports:`.
> 3. **Datos desaparecen:** Olvidaron declarar el volumen nombrado en la sección `volumes:`.
> 4. **Backup falla:** Error en el nombre del usuario o de la base de datos en `pg_dump`.
> 5. **Servicio no responde:** PostgreSQL aún está arrancando. Solución: Agregar Healthcheck."

**👨‍💻 Acción en Consola / Pizarra:**
- Dejar la tabla de solución de errores proyectada durante las consultas.

**💡 Tip de Gestión del Aula:**
- Guiar a los alumnos para que aprendan a diagnosticar si un problema es de red o de volumen.

---

### 📄 Diapositiva 27: Checklist de aprendizaje — Sesión 4
**Contenido de la PPT:**
```text
CHECKLIST DE APRENDIZAJE — SESIÓN 4
✔ Puedo explicar cómo Docker resuelve nombres de servicios en una red.
✔ Puedo diferenciar puerto publicado y comunicación interna.
✔ Puedo usar volúmenes nombrados para persistir datos.
✔ Puedo usar bind mounts para desarrollo local.
✔ Puedo mantener PostgreSQL como servicio interno.
✔ Puedo crear un backup y restaurarlo con comandos básicos.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Revisemos nuestro **Checklist de Aprendizaje de la Sesión 4**:
> Hoy han aprendido cómo funciona el DNS interno de las redes Docker, diferencian puertos públicos de redes privadas, utilizan volúmenes nombrados para resguardar bases de datos y bind mounts para desarrollar código, mantienen PostgreSQL aislado perimetralmente y ejecutan respaldos y restauraciones SQL con `pg_dump` y `psql`.
> ¡Un avance enorme en seguridad e infraestructura!"

**👨‍💻 Acción en Consola / Pizarra:**
- Marcar los 6 ticks en la pizarra haciendo énfasis en la persistencia.

**💡 Tip de Gestión del Aula:**
- Felicitar al grupo por dominar la persistencia de datos.

---

### 📄 Diapositiva 28: Resumen de la Sesión 4
**Contenido de la PPT:**
```text
RESUMEN DE LA SESIÓN 4
1. Los servicios se comunican por nombre dentro de redes Docker.
2. Los puertos publicados son para acceso desde el host, no para comunicación interna.
3. Los volúmenes nombrados conservan datos aunque se recree el contenedor.
4. Los bind mounts son útiles para desarrollo y edición local.
5. Los healthchecks verifican disponibilidad real, no solo ejecución.
6. Backup y restauración convierten datos persistentes en datos recuperables.

PRÓXIMA SESIÓN:
Docker en producción: Nginx, multi-stage builds, credenciales seguras, logging y monitoreo.
```

**🗣️ Guión del Docente (Lo que debes decir a los alumnos):**
> "Sinteticemos las **6 Conclusiones Clave de la Sesión 4**:
> 1. Los servicios se comunican por nombre en redes privadas de Docker.
> 2. Los puertos publicados solo se usan para lo que necesita el usuario final.
> 3. Los volúmenes nombrados protegen la información de la base de datos.
> 4. Los bind mounts agilizan el desarrollo de código en vivo.
> 5. Los healthchecks miden la salud real del servicio (`healthy`).
> 6. Los backups SQL garantizan la recuperabilidad del sistema.
>
> **En la Próxima Sesión (Sesión 5):** Ingresaremos a **Docker en Producción**: Reverse Proxy Nginx, Multi-stage builds profesionales, credenciales seguras, rotación de logs y monitoreo de recursos.
> ¡Muchas gracias y nos vemos en la Sesión 5!"

**👨‍💻 Acción en Consola / Pizarra:**
- Despedida de la sesión, recordar resolver la evaluación de 12 preguntas de la Sesión 4.

**💡 Tip de Gestión del Aula:**
- Recordar ingresar al aula virtual para la evaluación correspondiente.
