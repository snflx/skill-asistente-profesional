# Skills Integrados a Gemini — Auditor Técnico de Proyectos

[![skills.sh](https://skills.sh/b/anthropics/skills)](https://skills.sh)
![Licencia](https://img.shields.io/badge/licencia-MIT-12B5A5.svg)

**Actividad de Seguimiento** — Investigación y desarrollo de **Skills integrados a Gemini**, aplicados al ejercicio profesional de **Ingeniería de Sistemas / TI**.

Este proyecto implementa una Skill de Gemini que **automatiza la auditoría técnica de proyectos de software**: inventaría con evidencia, evalúa con rúbrica y entrega un informe accionable.

---

## ¿Qué es una Skill?

Una **Skill** es un paquete de conocimiento procedimental que extiende lo que un agente de IA puede hacer. No la ejecuta el modelo: la lee y la sigue cuando la tarea encaja. Aporta **instrucciones**, **buenas prácticas** y **recursos**. El formato es un estándar abierto adoptado por Google Antigravity y el agente de la Gemini API.

```
my-skill/
├── SKILL.md       # Requerido: frontmatter YAML + instrucciones
├── scripts/       # Opcional: código determinista
├── references/    # Opcional: rúbricas y documentos
└── assets/        # Opcional: plantillas de salida
```

## La Skill de este proyecto

**`auditor-tecnico-proyectos`** — vive en `.agents/skills/auditor-tecnico-proyectos/`.

Flujo de 3 pasos con criterios de término verificables:

1. **Inventaría con evidencia** → `scripts/escanear_proyecto.py` genera un inventario determinista (archivos, líneas por lenguaje, manifiestos y señales de riesgo).
2. **Evalúa cada dimensión** → `references/checklist-arquitectura.md` con 8 dimensiones (estructura, dependencias, seguridad, escalabilidad, calidad, observabilidad, documentación, mantenibilidad).
3. **Emite el informe** → `assets/plantilla-reporte.md`: resumen ejecutivo, hallazgos por severidad y plan priorizado por impacto × esfuerzo.

## Instalación y uso

### En Antigravity / Gemini (workspace)

La Skill ya vive en `.agents/skills/` y se autodescubre. Invócala por contexto o por nombre:

```
/auditor-tecnico-proyectos audita ./mi-proyecto
```

### Instalación global

```bash
# Copiar a la ruta global de Gemini
cp -r .agents/skills/auditor-tecnico-proyectos ~/.gemini/config/skills/
```

### Uso del escáner por separado

```bash
python .agents/skills/auditor-tecnico-proyectos/scripts/escanear_proyecto.py <ruta> --json reporte_scan.json
```

## Estructura del proyecto

```
skill-asistente-profesional/
├── .agents/skills/auditor-tecnico-proyectos/   # La Skill de Gemini
├── docs/                                        # Investigación y documentación
├── notebooks/cuaderno_datos.ipynb               # Cuaderno de datos
├── evals/evals.json                             # Pruebas de disparo de la Skill
├── examples/reporte_scan_ejemplo.json           # Salida de ejemplo del escáner
├── index.html                                   # Landing page
├── AGENTS.md                                    # Guía para agentes en el repo
└── README.md
```

## Entregables de la actividad

| # | Entregable | Estado | Ubicación |
|---|-----------|--------|-----------|
| 1 | Infografía (ChatGPT) | Pendiente de generar | Brief en `docs/03-brief-infografia-chatgpt.md` |
| 2 | Video corto (Flow) | Pendiente de producir | Guion en `docs/04-guion-video-flow.md` |
| 3 | Landing page (Antigravity + OpenCode) + README | Listo | `index.html`, `README.md` |
| 4 | Repositorio público en GitHub | Listo | https://github.com/snflx/skill-asistente-profesional |
| 5 | Skill orientada a Gemini | Listo | `.agents/skills/auditor-tecnico-proyectos/` |
| 6 | Documentación del desarrollo | Listo | `docs/02-desarrollo-skill.md` |
| 7 | Cuaderno de datos | Listo | `notebooks/cuaderno_datos.ipynb` |

> Los entregables 1 y 2 se producen en herramientas externas (ChatGPT y Flow); en este repositorio se incluye el **contenido y los prompts listos** para generarlos.

## Cómo validar

```bash
# Escáner (debe imprimir un JSON con el inventario)
python .agents/skills/auditor-tecnico-proyectos/scripts/escanear_proyecto.py .agents/skills/auditor-tecnico-proyectos

# Cuaderno de datos (ejecuta y regenera gráficos)
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/cuaderno_datos.ipynb
```

## Documentación

- [`docs/01-investigacion-skills-gemini.md`](docs/01-investigacion-skills-gemini.md) — investigación y fuentes.
- [`docs/02-desarrollo-skill.md`](docs/02-desarrollo-skill.md) — decisiones, pruebas y límites.
- [`docs/03-brief-infografia-chatgpt.md`](docs/03-brief-infografia-chatgpt.md) — brief de la infografía.
- [`docs/04-guion-video-flow.md`](docs/04-guion-video-flow.md) — guion del video.

## Licencia

MIT — ver [LICENSE](LICENSE).
