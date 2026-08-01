# 🧪 Laboratorio 05: Docker en Producción (Nginx Reverse Proxy & Multi-Stage Builds)
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Instructor:** Cristian Jampier Chileno Segundo | OTI - UNI  

## 🎯 Objetivos
1. Implementar Nginx como Reverse Proxy frontal escuchando en el puerto 8080.
2. Aislar los servicios web (Flask) y db (PostgreSQL) dentro de la red privada interna de Docker.
3. Optimizar el Dockerfile de Flask aplicando el patrón Multi-Stage Build (uilder + 
untime).
4. Configurar límites de memoria RAM/CPU (deploy.resources) y auditar el consumo con docker stats.

---

## 📁 Archivos del Laboratorio
El código listo para ejecutar se encuentra en: [codigo/sesion5](../../codigo/sesion5/)
O también disponible en: [laboratorios/sesion-final/labs-finales/lab3](../sesion-final/labs-finales/lab3/)

## 🚀 Pasos a Ejecutar
`ash
# 1. Entrar a la carpeta del laboratorio
cd codigo/sesion5

# 2. Levantar los servicios en segundo plano
docker compose up -d --build

# 3. Probar en el navegador
curl http://localhost:8080

# 4. Monitorear recursos en vivo
docker stats
`
