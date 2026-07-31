# Sesion 5: Docker En Produccion

## Objetivo

Configurar una aplicacion Docker lista para produccion con reverse proxy Nginx, multi-stage builds optimizados, seguridad basica de contenedores y monitoreo.

## 1. Reverse Proxy con Nginx

Un reverse proxy recibe peticiones del exterior y las redirige al servicio interno:

```text
Internet -> Nginx (puerto 80) -> Flask (puerto 5000, interno)
```

### Configuracion de Nginx

```nginx
server {
    listen 80;

    location / {
        proxy_pass http://web:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Arquitectura multi-red

```yaml
services:
  proxy:
    image: nginx:alpine
    ports:
      - "80:80"
    networks:
      - frontend

  web:
    build: .
    networks:
      - frontend
      - backend

  db:
    image: postgres:16
    networks:
      - backend

networks:
  frontend:
  backend:
```

- El proxy solo ve a `web` (red frontend)
- La DB solo es accesible desde `web` (red backend)
- El proxy **no** puede acceder directamente a la DB

## 2. Multi-Stage Build

Reduce el tamano de imagen separando la etapa de construccion de la etapa de produccion:

```dockerfile
# Etapa 1: Builder
FROM python:3.12-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Etapa 2: Produccion
FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY app/ .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app"]
```

## 3. Seguridad Basica

| Practica | Como |
|---|---|
| Usuario no-root | `RUN useradd appuser` + `USER appuser` |
| Read-only filesystem | `read_only: true` en Compose |
| Sin privilegios nuevos | `security_opt: ["no-new-privileges:true"]` |
| Limitar recursos | `deploy.resources.limits` en Compose |

## 4. Monitoreo

```bash
docker stats                          # Uso de CPU/RAM en vivo
docker compose logs -f --tail 50      # Ultimas 50 lineas de logs
docker inspect --format '{{.State.Health.Status}}' mi-contenedor
```

## 5. Restart Policies

```yaml
services:
  web:
    restart: unless-stopped
  db:
    restart: always
```

| Politica | Comportamiento |
|---|---|
| `no` | No reiniciar nunca |
| `always` | Reiniciar siempre |
| `unless-stopped` | Reiniciar excepto si se detuvo manualmente |
| `on-failure` | Reiniciar solo si falla |
