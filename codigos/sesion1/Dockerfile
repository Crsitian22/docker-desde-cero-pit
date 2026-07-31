# Imagen base liviana con Python 3.9
FROM python:3.9-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de requerimientos e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY app.py .

# Declarar el puerto expuesto
EXPOSE 5000

# Comando por defecto para ejecutar la aplicación
CMD ["python", "app.py"]
