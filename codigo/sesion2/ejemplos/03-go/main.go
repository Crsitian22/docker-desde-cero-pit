package main

import (
	"fmt"
	"net/http"
	"os"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		hostname, _ := os.Hostname()
		w.Header().Set("Content-Type", "text/html; charset=utf-8")
		fmt.Fprintf(w, `
			<!DOCTYPE html>
			<html>
			<head><title>UNI | Go Docker Demo</title></head>
			<body style="background-color:#0f172a; color:#f8fafc; font-family:sans-serif; text-align:center; padding:4rem;">
				<div style="background:#1e293b; padding:2rem; border-radius:12px; display:inline-block;">
					<h1 style="color:#818cf8;">🏛️ UNIVERSIDAD NACIONAL DE INGENIERÍA</h1>
					<h2>🚀 Servidor Web Compilado en Go (Golang)</h2>
					<p>ID del Contenedor: <code style="color:#34d399;">%s</code></p>
					<p>Puerto: <code style="color:#38bdf8;">8080</code></p>
				</div>
			</body>
			</html>
		`, hostname)
	})

	fmt.Println("Servidor Go corriendo en puerto 8080...")
	http.ListenAndServe(":8080", nil)
}
