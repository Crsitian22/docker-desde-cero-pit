#!/usr/bin/env bash
set -euo pipefail

echo "=========================================================="
echo "🚀 Desplegando Proyecto 1 en Producción (Stack Web UNI)..."
echo "=========================================================="

# 1. Crear archivo .env si no existe a partir del ejemplo
if [ ! -f .env ]; then
    echo "==> Copiando .env.example hacia .env..."
    cp .env.example .env
fi

# 2. Construir y levantar los contenedores en segundo plano
echo "==> Levantando servicios (Nginx, Flask, PostgreSQL)..."
docker compose up -d --build

# 3. Verificar estado de los contenedores
echo "==> Estado actual de los contenedores:"
docker compose ps

echo "=========================================================="
echo "✅ Despliegue completado con éxito."
echo "🌐 Accede a la aplicación en: http://localhost:8080"
echo "=========================================================="
