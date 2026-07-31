# LAB 1 — Fundamentos: Docker CLI desde Cero

En este laboratorio recorreremos los comandos esenciales de Docker: gestion de imagenes, contenedores, redes, volumenes y transferencia de archivos.

## Objetivo

- Comprender el ciclo de vida completo de un contenedor.
- Dominar `docker run`, `docker ps`, `docker exec`, `docker cp`.
- Gestionar imagenes locales: `pull`, `tag`, `rmi`, `inspect`.
- Crear y usar redes y volumenes desde la CLI.

---

## Conceptos Clave

| Termino | Descripcion |
|---------|-------------|
| **Imagen** | Plantilla de solo lectura. Es el "molde" del contenedor. |
| **Contenedor** | Instancia en ejecucion de una imagen. |
| **Docker Daemon** | Proceso que corre en background y gestiona todo (`dockerd`). |
| **Registry** | Repositorio de imagenes. Docker Hub es el publico por defecto. |
| **Volume** | Directorio persistente gestionado por Docker. |
| **Bind Mount** | Monta una carpeta del host dentro del contenedor. |
| **Network** | Red virtual que conecta contenedores entre si. |

---

## Paso 1 — Gestion de Imagenes

```bash
docker pull nginx
docker pull nginx:1.25-alpine
docker images
docker image inspect nginx
docker tag nginx:latest mi-nginx:v1.0
docker rmi mi-nginx:v1.0
```

## Paso 2 — Ciclo de Vida de Contenedores

```bash
docker run hello-world
docker run -d -p 8080:80 --name mi-web nginx
curl http://localhost:8080
docker ps
docker stop mi-web
docker ps -a
docker start mi-web
docker rm -f mi-web
```

## Paso 3 — Interactuar con Contenedores

```bash
docker run -d --name mi-web nginx
docker exec -it mi-web bash
docker exec mi-web cat /etc/nginx/nginx.conf
docker logs mi-web
docker logs -f --tail 20 mi-web
```

## Paso 4 — Volumenes

```bash
docker volume create mis-datos
docker volume ls
docker run -d --name web-vol -v mis-datos:/usr/share/nginx/html nginx
docker exec web-vol sh -c 'echo "Hola Volumen" > /usr/share/nginx/html/index.html'
docker rm -f web-vol
docker run -d --name web-vol2 -v mis-datos:/usr/share/nginx/html -p 8080:80 nginx
curl http://localhost:8080
```

## Paso 5 — Redes

```bash
docker network create mi-red
docker run -d --name app1 --network mi-red nginx
docker run -d --name app2 --network mi-red nginx
docker exec app1 ping -c 3 app2
```

## Paso 6 — Limpieza

```bash
docker rm -f $(docker ps -aq)
docker volume prune -f
docker network prune -f
docker system df
```
