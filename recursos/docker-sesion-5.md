# Recursos Adicionales: Sesion 5 — Docker en Produccion

## Lecturas Recomendadas

- [Docker Best Practices](https://docs.docker.com/build/building/best-practices/)
- [Nginx Reverse Proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)
- [Docker Security](https://docs.docker.com/engine/security/)

## Checklist de Produccion

1. Usar imagenes base minimas (alpine o slim)
2. No ejecutar como root
3. Usar multi-stage builds
4. Configurar healthchecks
5. Limitar recursos (CPU/RAM)
6. Configurar restart policies
7. Usar logging driver con rotacion
8. Mantener secretos fuera del codigo
