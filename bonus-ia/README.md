# Bonus: Inteligencia Artificial para Operaciones — Conceptos Fundamentales

Introduccion a los conceptos de IA generativa, agentes, tokens, MCP, skills, LLMs y herramientas como Claude y opencode, orientados a profesionales de infraestructura y seguridad.

---

## 1. Large Language Models (LLMs)

### Que es un LLM?

Un **Large Language Model** es un modelo de inteligencia artificial entrenado sobre billones de textos para predecir cual es el proximo token mas probable dado un contexto. No "entiende" el texto como un humano; calcula probabilidades estadisticas sobre secuencias de tokens.

### Modelos principales

| Modelo | Desarrollador | Contexto maximo | Caracteristicas |
|--------|---------------|----------------|-----------------|
| **GPT-4o** | OpenAI | 128K tokens | Multimodal (texto, imagen, audio). |
| **Claude 3.5 Sonnet / Opus** | Anthropic | 200K tokens | Alto razonamiento, baja alucinacion. |
| **Gemini 1.5 Pro** | Google | 1M+ tokens | Ventana de contexto masiva. |
| **Llama 3** | Meta | 128K tokens | Open-weight. Se puede correr localmente. |
| **Mistral / Mixtral** | Mistral AI | 32K tokens | Eficiente, open-weight. MoE. |

### Parametros de generacion

| Parametro | Que controla | Rango tipico |
|-----------|-------------|-------------|
| **Temperature** | Aleatoriedad. 0 = determinista, 1 = creativo | 0.0 - 2.0 |
| **Top-p** | Porcentaje acumulado de tokens probables | 0.1 - 1.0 |
| **Max tokens** | Longitud maxima de respuesta | 1 - contexto max. |

> **Temperatura baja (0-0.3)**: ideal para codigo, datos tecnicos.
> **Temperatura alta (0.7-1.5)**: ideal para escritura creativa.

---

## 2. Tokens

Un **token** es la unidad atomica que un LLM procesa:

- `"Docker"` → 1 token
- `"containerizacion"` → 2-3 tokens
- `docker compose up -d` → 5-7 tokens

### Costos por tokens

Los proveedores cobran por **tokens procesados**:

| Tipo | Costo por 1M tokens (referencial) |
|------|-----------------------------------|
| Input | $3.00 |
| Output | $15.00 |

---

## 3. Agentes de IA

Un agente es un LLM que puede usar **herramientas** para interactuar con el mundo real:

```text
Usuario -> Agente -> [Herramientas: Terminal, Archivos, APIs] -> Resultado
```

### Ejemplos de agentes

- **Claude Code**: agente que puede leer/escribir archivos y ejecutar comandos.
- **GitHub Copilot**: asistente de codigo integrado en el editor.
- **Antigravity**: agente que puede controlar el navegador, terminal y archivos.

---

## 4. MCP (Model Context Protocol)

MCP es un protocolo que permite a los LLMs conectarse a herramientas externas de forma estandarizada:

```text
LLM <-> MCP Server <-> [PostgreSQL, Docker, APIs, Archivos]
```

### Ejemplo: MCP con Docker

Un servidor MCP para Docker podria exponer tools como:
- `docker_ps`: listar contenedores
- `docker_logs`: ver logs de un contenedor
- `docker_exec`: ejecutar comandos dentro de un contenedor

---

## 5. Aplicacion en Infraestructura

| Caso de uso | Herramienta | Beneficio |
|-------------|-------------|-----------|
| Troubleshooting Docker | Claude + MCP Docker | Diagnostico automatizado |
| Escritura de Dockerfiles | Claude / Copilot | Genera Dockerfiles optimizados |
| Monitoreo inteligente | Agentes + prometheus | Alertas con contexto |
| Documentacion automatica | LLMs + codigo fuente | Genera docs actualizados |
