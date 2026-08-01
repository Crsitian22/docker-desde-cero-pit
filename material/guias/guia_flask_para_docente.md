# 🐍 Guía Pedagógica: Cómo Enseñar Flask desde Cero a tus Alumnos
**Curso:** Docker desde Cero: Crea y Despliega Aplicaciones (10ma Edición 2026)  
**Docente:** Cristian Jampier Chileno Segundo (Astra) | OTI - UNI  

---

## 🎯 ¿Qué es Flask y por qué lo usamos en el Curso de Docker?

### 🗣️ Explicación en 1ª Persona para Decir en Clase:
> *"Alumnos, antes de meter nuestra aplicación dentro de un contenedor Docker, debemos entender qué aplicación vamos a empaquetar. Para este curso utilizaremos **Flask**, un micro-framework web escrito en Python.*
>
> *¿Por qué elegimos Flask y no Django o Node.js?*
> *1. **Es Ultra Ligero:** Con menos de 10 líneas de código tenemos un servidor web HTTP completo funcionando.*
> *2. **Es Transparente:** No oculta configuraciones complejas detrás de archivos ocultos, lo que nos permite ver exactamente cómo un proceso escucha peticiones de red.*
> *3. **Es el Estándar en Microservicios:** La gran mayoría de empresas utilizan Python con Flask o FastAPI para construir APIs ligeras y microservicios empaquetados en contenedores Docker."*

---

## 💻 Paso a Paso: Cómo Crear una Aplicación Flask desde Cero

Para construir la aplicación web que el alumno contenerizará, enséñales a crear la siguiente estructura de archivos en su carpeta de trabajo:

```text
mi-proyecto-flask/
├── app.py                # Script principal de la aplicación en Python
├── requirements.txt      # Lista de dependencias de Python
└── templates/
    └── index.html        # Plantilla HTML que se renderiza en el navegador
```

---

### 📄 Paso 1: El Archivo de Dependencias (`requirements.txt`)
Enséñales que en el ecosistema de Python, `requirements.txt` cumple el mismo rol que `package.json` en Node.js.

Crear el archivo `requirements.txt`:
```text
Flask==3.0.2
psycopg2-binary==2.9.9
gunicorn==21.2.0
```

**🗣️ Explicación del Docente:**
- `Flask`: El servidor web micro.
- `psycopg2-binary`: El driver de conexión que le permite a Python comunicarse con la base de datos PostgreSQL.
- `gunicorn`: El servidor WSGI de producción que usaremos en las Sesiones 5 y 6.

---

### 📄 Paso 2: El Script Principal de Python (`app.py`) Explicado Línea por Línea

Crea el archivo `app.py`:

```python
from flask import Flask, render_template, request, redirect, url_for

# 1. Crear la instancia de la aplicación Flask
app = Flask(__name__)

# 2. Definir la ruta principal (Endpoint '/')
@app.route('/')
def inicio():
    # Renderiza la página HTML almacenada en la carpeta templates/
    return render_template('index.html', mensaje="¡Hola desde nuestro contenedor Docker!")

# 3. Definir una ruta secundaria (Endpoint '/saludo/<nombre>')
@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"<h1>¡Bienvenido a la clase de Docker, {nombre}!</h1>"

# 4. Punto de entrada para ejecutar el servidor
if __name__ == '__main__':
    # IMPORTANTE DOCKER: host='0.0.0.0' permite que el servidor escuche fuera del contenedor
    app.run(host='0.0.0.0', port=5000, debug=True)
```

---

## 🧠 Explicación Detallada Línea por Línea (Para Responder Dudas en Pizarra)

1. **`from flask import Flask, render_template`**
   - *¿Qué hace?* Importa la clase principal `Flask` para levantar el servidor y la función `render_template` para enviar páginas HTML al navegador.

2. **`app = Flask(__name__)`**
   - *¿Qué hace?* Crea la instancia de la aplicación web. El argumento `__name__` le indica a Flask dónde buscar las carpetas de recursos como `templates/` y `static/`.

3. **`@app.route('/')`**
   - *¿Qué hace?* Es un **decorador de Python**. Asocia una URL (en este caso la raíz `/`) con la función que está inmediatamente abajo (`def inicio()`). Cada vez que un usuario ingrese a `http://localhost:5000/`, Flask ejecutará esa función.

4. **`return render_template('index.html', mensaje=...)`**
   - *¿Qué hace?* Busca el archivo `index.html` dentro de la carpeta `templates/` y le inyecta la variable `mensaje`.

5. **`app.run(host='0.0.0.0', port=5000)` ⚠️ (CONCEPTO CLAVE DE DOCKER)**
   - **PREGUNTA TÍPICA DE ALUMNO:** *"Profesor, ¿por qué ponemos `host='0.0.0.0'` y no `host='localhost'`?"*
   - **RESPUESTA DEL DOCENTE:**  
     > *"Si configuramos `localhost` (`127.0.0.1`), Flask solo escuchará peticiones generadas DENTRO del mismo contenedor. Como nosotros queremos que la laptop anfitriona acceda desde fuera del contenedor, debemos poner `0.0.0.0`, que significa: **'Escuchar en TODAS las interfaces de red disponibles dentro del contenedor'**. Sin este parámetro, el mapeo de puertos `-p 5000:5000` de Docker fallará y el navegador mostrará conexión rechazada."*

---

### 📄 Paso 3: La Plantilla HTML (`templates/index.html`)

Crea la carpeta `templates` y dentro el archivo `index.html`:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi App Flask en Docker - PIT 2026</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0d1117; color: #c9d1d9; text-align: center; padding-top: 50px; }
        .card { background-color: #161b22; border: 1px solid #30363d; border-radius: 10px; display: inline-block; padding: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
        h1 { color: #58a6ff; }
        .badge { background-color: #238636; color: white; padding: 5px 15px; border-radius: 15px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h1>🐳 Docker desde Cero - PIT 2026</h1>
        <p><strong>Docente:</strong> Cristian Jampier Chileno Segundo (Astra)</p>
        <p class="badge">{{ mensaje }}</p>
    </div>
</body>
</html>
```

---

## 🐳 Paso a Paso: Cómo Contenerizar la App Flask con Docker

Una vez creada la app Flask, enseña a los alumnos la secuencia de contenerización:

### 1️⃣ Crear el `Dockerfile`
En la raíz del proyecto, crear el archivo `Dockerfile`:

```dockerfile
# 1. Imagen base oficial ligera de Python
FROM python:3.12-slim

# 2. Directorio de trabajo interno del contenedor
WORKDIR /app

# 3. Copiar primero el archivo de dependencias (para aprovechar la caché)
COPY requirements.txt .

# 4. Instalar las librerías necesarias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código fuente
COPY . .

# 6. Documentar el puerto que usa Flask
EXPOSE 5000

# 7. Comando de arranque del contenedor
CMD ["python", "app.py"]
```

### 2️⃣ Crear el `.dockerignore`
Para evitar enviar archivos basura a la imagen:
```text
__pycache__/
*.pyc
.git
.venv
```

### 3️⃣ Compilar y Ejecutar en Consola (Demostración del Docente)
```bash
# Paso A: Compilar la imagen
docker build -t mi-flask-app:v1 .

# Paso B: Ejecutar el contenedor mapeando el puerto 5000
docker run -d -p 5000:5000 --name contenedor-flask mi-flask-app:v1

# Paso C: Probar en el navegador web
# Abrir en Chrome/Edge: http://localhost:5000
```

---

## 🔗 Conexión de Flask con PostgreSQL en Docker Compose (Sesiones 3 a 6)

Cuando llegues a la **Sesión 3**, explica cómo Flask lee las credenciales desde las variables de entorno inyectadas por Docker Compose:

```python
import os
import psycopg2

def obtener_conexion_db():
    # Lee las variables inyectadas desde el archivo .env vía Docker Compose
    conn = psycopg2.connect(
        host=os.environ.get('POSTGRES_HOST', 'db'),  # 'db' es el hostname del servicio Compose
        database=os.environ.get('POSTGRES_DB', 'appdb'),
        user=os.environ.get('POSTGRES_USER', 'appuser'),
        password=os.environ.get('POSTGRES_PASSWORD', 'apppass'),
        port=5432
    )
    return conn
```

**🗣️ Explicación del Docente:**
> *"Fíjense en `host=os.environ.get('POSTGRES_HOST', 'db')`. Dentro del contenedor de Flask no ponemos `localhost`, ponemos `'db'`. Gracias al DNS interno de Docker Compose, la palabra `'db'` se traduce automáticamente a la dirección IP privada del contenedor de PostgreSQL."*
