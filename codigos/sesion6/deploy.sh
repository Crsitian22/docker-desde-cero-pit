#!/bin/bash
# Script de Despliegue Automatizado - PIT 2026

ENTORNO=${1:-dev}

echo "🚀 Iniciando Despliegue en Entorno: $ENTORNO"

if [ "$ENTORNO" == "prod" ]; then
    docker compose -f compose.yml -f compose.prod.yml up -d --build
    echo "✅ Aplicación desplegada en PRODUCCIÓN en http://localhost"
else
    docker compose -f compose.yml -f compose.dev.yml up -d --build
    echo "🛠️ Aplicación desplegada en DESARROLLO en http://localhost:5000"
fi
