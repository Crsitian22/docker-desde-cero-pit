# 🧪 Laboratorio 06: Proyecto Final y Despliegue Completo
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Instructor:** Ing. Cristian Jampier Chileno Segundo | OTI - UNI  

## 🎯 Objetivos
1. Integrar la arquitectura multi-entorno usando Compose Overrides (compose.yml base + compose.dev.yml / compose.prod.yml).
2. Alternar configuraciones entre Desarrollo (hot-reload con Bind Mounts) y Producción (imágenes inmutables).
3. Automatizar el proceso de actualización mediante un script en Bash desplegar.sh con set -euo pipefail.
4. Ejecutar la prueba de reconstrucción limpia 100% reproducible.

---

## 📁 Archivos del Laboratorio
El código listo para ejecutar se encuentra en: [codigo/sesion6](../../codigo/sesion6/)
O también disponible en: [laboratorios/sesion-final/labs-finales/lab4](../sesion-final/labs-finales/lab4/)

## 🚀 Pasos a Ejecutar
`ash
# 1. Entrar a la carpeta del laboratorio
cd codigo/sesion6

# 2. Dar permisos y ejecutar el script de despliegue
chmod +x desplegar.sh
./desplegar.sh

# 3. Verificar el estado final del stack
docker compose ps
`
