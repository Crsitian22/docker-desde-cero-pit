import express, { Request, Response } from 'express';
import os from 'os';

const app = express();
const PORT: number = 4000;

interface AppStatus {
    status: string;
    language: string;
    framework: string;
    hostname: string;
    arch: string;
    uptimeSeconds: number;
}

app.get('/', (req: Request, res: Response) => {
    const statusData: AppStatus = {
        status: "healthy",
        language: "TypeScript 5.4",
        framework: "Express.js",
        hostname: os.hostname(),
        arch: os.arch(),
        uptimeSeconds: Math.floor(process.uptime())
    };

    res.send(`
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <title>UNI | TypeScript Docker Demo</title>
            <style>
                body { background-color: #0f172a; color: #f8fafc; font-family: sans-serif; text-align: center; padding: 4rem; }
                .card { background: #1e293b; padding: 2.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); display: inline-block; max-width: 550px; text-align: left; }
                .badge { background: #3178c6; color: white; padding: 0.4rem 0.8rem; border-radius: 9999px; font-weight: bold; font-size: 0.8rem; }
                code { color: #38bdf8; font-family: monospace; font-weight: bold; }
                pre { background: #0f172a; padding: 1rem; border-radius: 8px; color: #34d399; font-size: 0.85rem; }
            </style>
        </head>
        <body>
            <div class="card">
                <span class="badge">TYPESCRIPT 5.4 • NODE.JS • DOCKER</span>
                <h2 style="color: #ffffff; margin-top: 1rem;">🏛️ Demo TypeScript Compilado</h2>
                <p>Aplicación web escrita en <strong>TypeScript</strong> con tipado estático, compilada en Docker (Multi-stage Build).</p>
                <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 1rem 0;">
                <p><strong>ID del Contenedor:</strong> <code>${statusData.hostname}</code></p>
                <p><strong>Arquitectura CPU:</strong> <code>${statusData.arch}</code></p>
                <p><strong>Puerto Expuesto:</strong> <code>${PORT}</code></p>
                <p><strong>Métricas de Estado JSON:</strong></p>
                <pre>${JSON.stringify(statusData, null, 2)}</pre>
            </div>
        </body>
        </html>
    `);
});

app.listen(PORT, () => {
    console.log(`🚀 Servidor TypeScript corriendo en puerto ${PORT}`);
});
