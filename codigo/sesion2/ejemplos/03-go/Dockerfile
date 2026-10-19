# Etapa 1: Compilación en Go
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY main.go .
RUN go build -o mi-app main.go

# Etapa 2: Ejecución ultra liviana en Alpine
FROM alpine:3.23
WORKDIR /app
COPY --from=builder /app/mi-app .
EXPOSE 8080
CMD ["./mi-app"]
