# Sesion 1: Contenedores Desde Cero

## Objetivo

Comprender que problema resuelve Docker, diferenciar imagen y contenedor, ejecutar comandos esenciales y construir una primera aplicacion Flask en contenedor.

## El problema: funciona en mi maquina

Una aplicacion puede funcionar en la laptop del desarrollador y fallar en otro entorno por diferencias de versiones, librerias o configuracion. Docker reduce esa variacion empaquetando la aplicacion con sus dependencias.

```text
Codigo -> Dependencias -> Imagen Docker -> Contenedor
```

## Contenerizacion

Contenerizacion es empaquetar la app con sus dependencias y configuracion minima para lograr ejecucion aislada y uniforme.

```text
El contenedor reduce diferencias entre desarrollo, pruebas y produccion.
No elimina todas las diferencias: kernel, arquitectura, variables externas y permisos aun importan.
```

## Docker en una frase

Docker es una herramienta para construir, ejecutar y distribuir contenedores.

Flujo diario:
- **Imagen**: paquete reproducible
- **Contenedor**: ejecucion de la imagen
- **Registro**: lugar para compartir imagenes (Docker Hub)
- **CLI**: herramienta de control

## Docker vs maquina virtual

Una VM virtualiza una maquina completa e incluye un sistema operativo invitado. Un contenedor comparte el kernel del host y solo incluye lo necesario para ejecutar la aplicacion.

| Criterio | Maquina virtual | Contenedor |
|---|---|---|
| Sistema operativo | Incluye SO completo | Comparte kernel del host |
| Arranque | Mas lento | Rapido |
| Consumo | Mayor RAM y disco | Menor consumo |
| Uso comun | Laboratorios o servidores completos | Apps reproducibles |
| Aislamiento | Fuerte (kernel propio) | Proceso aislado (kernel compartido) |

### Hipervisores

| Tipo | Descripcion | Ejemplos |
|---|---|---|
| Tipo 1 | Corre directamente sobre hardware | Proxmox, ESXi |
| Tipo 2 | Corre como aplicacion sobre un SO | VirtualBox, VMware Workstation |

Docker **no** es un hipervisor. Usa aislamiento a nivel de sistema operativo (namespaces y cgroups).

## Que si veremos y que no veremos hoy

| Hoy si | Hoy no |
|---|---|
| Instalar y validar Docker | Kubernetes |
| Diferenciar imagen y contenedor | Redes avanzadas |
| Ejecutar contenedores | Docker Compose |
| Construir una primera imagen | Produccion |
| Publicar puertos | Volumenes |

## Comandos esenciales

### Validar instalacion

```bash
docker --version
docker info
docker run hello-world
```

Si `docker --version` funciona pero `docker info` falla, puede ser que el daemon/engine no este activo.

### Ejecutar un servicio web

```bash
docker run --name web-demo -d -p 8080:80 nginx
docker ps
```

- `--name web-demo`: nombre humano para el contenedor
- `-d`: modo detached (segundo plano)
- `-p 8080:80`: puerto host 8080 hacia puerto contenedor 80
- `nginx`: imagen

Abrir `http://localhost:8080`

### Detener y limpiar

```bash
docker stop web-demo
docker ps -a
docker rm web-demo
docker images
```

Contenedor detenido aun ocupa nombre y metadata. No puedes crear otro contenedor con el mismo nombre hasta borrar o renombrar el anterior. La imagen sigue en disco hasta que se elimine con `docker rmi`.

### Construir una imagen propia

```bash
cd codigo/sesion1
docker build -t mi-flask:v1 .
docker run -d --name flask-app -p 5000:5000 mi-flask:v1
```

Probar en `http://localhost:5000`

## Resumen

| Concepto | Descripcion |
|---|---|
| Imagen | Paquete reproducible con app + dependencias |
| Contenedor | Instancia ejecutandose de una imagen |
| `docker run` | Crea y ejecuta un contenedor |
| `docker build` | Construye una imagen desde un Dockerfile |
| `-p host:container` | Publica puertos |
| `-d` | Modo segundo plano |
