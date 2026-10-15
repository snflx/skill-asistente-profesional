# AGENTS.md — skill-asistente-profesional

Guía para agentes de IA (Gemini, Antigravity, OpenCode) que trabajen en este repositorio.

## Qué es este proyecto

Repositorio de la actividad **"Skills integrados a Gemini"**: una Skill reutilizable para el ejercicio profesional de Ingeniería de Sistemas/TI, más su landing page, documentación e investigación.

## Mapa del repositorio

- `.agents/skills/auditor-tecnico-proyectos/` — la Skill de Gemini (formato abierto `SKILL.md`).
- `docs/` — investigación, documentación de desarrollo y briefs de entregables.
- `notebooks/cuaderno_datos.ipynb` — cuaderno de datos con el análisis de la investigación.
- `index.html` — landing page de presentación del proyecto.
- `examples/reporte_scan_ejemplo.json` — salida de ejemplo del escáner de la Skill.

## Convenciones

- Idioma de documentación: español.
- Formato de Skill: frontmatter YAML con `name` y `description`; descripción con disparadores explícitos.
- Scripts en Python 3 con biblioteca estándar únicamente (portabilidad).
- No versionar secretos: `.env` está en `.gitignore`.

## Cómo validar

```bash
python .agents/skills/auditor-tecnico-proyectos/scripts/escanear_proyecto.py .agents/skills/auditor-tecnico-proyectos
```

## Cómo instalar la Skill en Gemini / Antigravity

- Workspace: ya vive en `.agents/skills/` (se autodescubre).
- Global: copiar la carpeta a `~/.gemini/config/skills/`.
- Antigravity IDE la detecta automáticamente y se invoca por nombre o por contexto.
