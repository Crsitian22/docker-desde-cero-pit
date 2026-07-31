# Banco de Evaluaciones y Quizzes: Fundamentos de Docker y Taller Semanal (10ma Edición 2026)
**Programa de Iniciación Tecnológica (PIT) 2026 | OTI - UNI**
**Docente:** Ing. Cristian Jampier Chileno Segundo
**Estructura:** 10 Preguntas de opción múltiple por cada evaluación (Sesiones 1 a 6 y Taller)

---

## 📝 PARTE 1: Evaluaciones del Curso Regular (Sesiones 1 a 6)

### **Test de la Sesión 1: Contenedores desde Cero**
1. **¿Cuál es la diferencia fundamental de arquitectura entre una Máquina Virtual (VM) y un Contenedor de Docker?**
   * a) Las VMs son más ligeras y veloces al arrancar que los contenedores.
   * b) Las VMs requieren empaquetar un Sistema Operativo Invitado completo encima de un hipervisor, mientras que los contenedores comparten el Kernel del Host.
   * c) Los contenedores virtualizan el hardware físico del servidor y las VMs aíslan procesos.
   * d) No existe diferencia de arquitectura.
2. **Si ejecutas el comando `docker run -d -p 8080:80 nginx`, ¿qué acción realiza el flag `-p 8080:80`?**
   * a) Abre el puerto 80 del host y lo bloquea internamente.
   * b) Enruta el tráfico del puerto 80 del Host hacia el puerto 8080 del contenedor.
   * c) Enruta el tráfico del puerto 8080 del Host hacia el puerto 80 interno del contenedor.
   * d) Establece los límites de descarga de red.
3. **¿Qué comando de gestión de Docker utilizarías para verificar el ID, nombre y estado de los contenedores en ejecución?**
   * a) `docker container status`
   * b) `docker image ls`
   * c) `docker ps` (o `docker container ls`)
   * d) `docker inspect --all`
4. **Si un contenedor en ejecución `flask-app` debe ser detenido y luego eliminado, ¿qué comandos se ejecutan?**
   * a) `docker stop flask-app` y luego `docker rm flask-app`
   * b) `docker rmi flask-app`
   * c) `docker kill --all`
   * d) `docker system prune`
5. **¿Qué sucede al ejecutar `docker run hello-world` si la imagen no se encuentra descargada localmente?**
   * a) Muestra error de red.
   * b) Busca la imagen localmente, y al no encontrarla, la descarga automáticamente de Docker Hub (pull) y la ejecuta.
   * c) Crea una imagen vacía.
   * d) Solicita permisos de root.

**🗝️ Solucionario Sesión 1:** 1-b | 2-c | 3-c | 4-a | 5-b

---

### **Test de la Sesión 2: Dockerfile Profesional y Registro**
1. **¿Para qué sirve la instrucción `WORKDIR` dentro de un archivo Dockerfile?**
   * a) Para descargar dependencias.
   * b) Para definir el directorio de trabajo interno donde se ejecutarán las instrucciones siguientes.
   * c) Para cambiar la clave de root.
   * d) Para compilar el kernel.
2. **¿Qué ventaja principal ofrece el patrón Multi-Stage Build en Docker?**
   * a) Aumentar el tamaño de la imagen final.
   * b) Separar la etapa de compilación de la etapa final de producción, logrando imágenes ultraligeras y seguras.
   * c) Evitar el uso de Docker Compose.
   * d) Duplicar la memoria RAM.

**🗝️ Solucionario Sesión 2:** 1-b | 2-b

---

### **Test de la Sesión 3: Orquestación Local con Docker Compose**
1. **¿Cómo se comunican dos contenedores en la misma red de Docker Compose?**
   * a) Usando la dirección IP privada de la laptop.
   * b) Usando el nombre del servicio definido en `compose.yml` como hostname gracias al DNS interno.
   * c) Mediante cables virtuales USB.
   * d) No se pueden comunicar.

**🗝️ Solucionario Sesión 3:** 1-b

---

### **Test de la Sesión 4: Persistencia de Datos, Redes y Backups**
1. **¿Dónde almacena Docker la información de un Volumen Nombrado (`named volume`)?**
   * a) En la memoria RAM del contenedor.
   * b) En el directorio interno del motor `/var/lib/docker/volumes/` en el host, aislado del código fuente.
   * c) En la nube de Docker Hub.
   * d) En la papelera de reciclaje.

**🗝️ Solucionario Sesión 4:** 1-b

---

### **Test de la Sesión 5: Reverse Proxy con Nginx**
1. **¿Qué función cumple la directiva `proxy_pass http://web:5000;` en Nginx?**
   * a) Bloquear el tráfico entrante al puerto 5000.
   * b) Redirigir las solicitudes HTTP recibidas en Nginx hacia el contenedor de la aplicación Flask en la red interna.
   * c) Descargar la imagen de Nginx.
   * d) Cambiar la clave de la base de datos.

**🗝️ Solucionario Sesión 5:** 1-b

---

### **Test de la Sesión 6: Multi-Entorno y Debugging**
1. **¿Cuál es el primer paso recomendado en el protocolo de diagnóstico profesional ante un fallo en un contenedor?**
   * a) Borrar todo el servidor con `rm -rf /`.
   * b) Revisar el estado con `docker compose ps` y auditar los logs con `docker compose logs -f <servicio>`.
   * c) Reinstalar Windows.
   * d) Formatear el disco duro.

**🗝️ Solucionario Sesión 6:** 1-b
