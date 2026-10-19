# Etapa 1: Builder (Instala dependencias de desarrollo y compila TS ➔ JS)
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json tsconfig.json ./
RUN npm install
COPY src ./src
RUN npm run build

# Etapa 2: Producción (Copia solo el JS compilado y dependencias livianas de producción)
FROM node:20-alpine AS production
WORKDIR /app
COPY package*.json ./
RUN npm install --only=production
COPY --from=builder /app/dist ./dist

EXPOSE 4000
CMD ["node", "dist/server.js"]
