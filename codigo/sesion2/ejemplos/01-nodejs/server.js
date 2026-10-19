const express = require('express');
const os = require('os');
const app = express();

app.get('/', (req, res) => {
    res.send(`
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>UNI | Node.js Docker Demo</title>
            <style>
                body { background-color: #0f172a; color: #f8fafc; font-family: sans-serif; text-align: center; padding: 4rem; }
                h1 { color: #38bdf8; }
                .card { background: #1e293b; padding: 2rem; border-radius: 12px; display: inline-block; }
                code { color: #34d399; font-weight: bold; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🏛️ UNIVERSIDAD NACIONAL DE INGENIERÍA</h1>
                <h2>🐳 Demo en Node.js + Express (Puerto 3000)</h2>
                <p>ID del Contenedor: <code>${os.hostname()}</code></p>
                <p>Sistema Operativo: <code>${os.type()} ${os.release()}</code></p>
            </div>
        </body>
        </html>
    `);
});

app.listen(3000, () => {
    console.log('Servidor Node.js corriendo en puerto 3000');
});
