<?php
// Simulación de prueba de conexión a MySQL estilo Laravel
$host = getenv('DB_HOST') ?: 'db';
$db   = getenv('DB_DATABASE') ?: 'laravel_db';
$user = getenv('DB_USERNAME') ?: 'laravel_user';
$pass = getenv('DB_PASSWORD') ?: 'secret123';

header('Content-Type: text/html; charset=utf-8');
?>
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>UNI | PHP Laravel + MySQL Demo</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: sans-serif; text-align: center; padding: 3rem; }
        .card { background: #1e293b; padding: 2.5rem; border-radius: 16px; border: 1px solid rgba(255,255,255,0.1); display: inline-block; max-width: 550px; text-align: left; }
        .badge { background: #ff2d20; color: white; padding: 0.4rem 0.8rem; border-radius: 9999px; font-weight: bold; font-size: 0.8rem; }
        .status { padding: 0.8rem; border-radius: 8px; font-weight: bold; margin-top: 1rem; }
        .ok { background: rgba(52, 211, 153, 0.15); border: 1px solid #34d399; color: #34d399; }
        .err { background: rgba(248, 113, 113, 0.15); border: 1px solid #f87171; color: #f87171; }
        code { color: #38bdf8; }
    </style>
</head>
<body>
    <div class="card">
        <span class="badge">PHP 8.2 • LARAVEL • MYSQL 8.0</span>
        <h2 style="color: #ffffff; margin-top: 1rem;">🏛️ Demo PHP Laravel + MySQL</h2>
        <p>Servicio web en PHP conectado a base de datos MySQL mediante Docker.</p>
        <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 1rem 0;">
        <p><strong>Host BD:</strong> <code><?= $host ?></code></p>
        <p><strong>Base de Datos:</strong> <code><?= $db ?></code></p>
        <p><strong>Usuario BD:</strong> <code><?= $user ?></code></p>

        <?php
        try {
            $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
            $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $version = $pdo->query('SELECT VERSION()')->fetchColumn();
            echo "<div class='status ok'>✅ Conexión Exitosa a MySQL!<br><small>Versión MySQL: $version</small></div>";
        } catch (PDOException $e) {
            echo "<div class='status err'>❌ Error de conexión: " . htmlspecialchars($e->getMessage()) . "</div>";
        }
        ?>
    </div>
</body>
</html>
