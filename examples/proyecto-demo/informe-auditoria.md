# Informe de Auditoría Técnica — Proyecto Demo

- **Fecha:** 2026-10-15
- **Alcance:** `examples/proyecto-demo` (proyecto ficticio de demostración)
- **Herramienta de inventario:** `escanear_proyecto.py` → `reporte_scan.json`

> Informe de demostración generado siguiendo el flujo de la Skill `auditor-tecnico-proyectos` (inventario → rúbrica → informe).

## 1. Resumen ejecutivo

Proyecto pequeño (6 archivos, 22 líneas) con **riesgos de seguridad de severidad Alta**: se versiona un `.env` con credenciales y se embeben secretos en el código (`src/db.py`). La estructura de dependencias carece de bloqueo de versiones. Recomendación: no exponer credenciales y moverlas a variables de entorno, antes de cualquier uso en producción.

## 2. Inventario

- Archivos analizados: 6
- Líneas de código: 22
- Lenguajes principales: Python (2 archivos / 17 líneas), JavaScript (1 / 3), Markdown (1 / 2)
- Manifiestos de dependencias: `requirements.txt`

## 3. Puntuación por dimensión

| Dimensión | Nota (1-5) | Evidencia |
|-----------|-----------|-----------|
| Estructura y capas | 3 | `src/` separa módulos, pero `db.py` mezcla configuración y acceso a datos. |
| Dependencias | 2 | `requirements.txt` sin versiones fijadas (`flask==2.0.1` vs `requests` libre). |
| Seguridad | 1 | `.env` versionado + `DB_PASSWORD` embebida en `src/db.py`. |
| Escalabilidad y rendimiento | 2 | Sin capa de conexión real; N/A por tamaño, pero sin diseño. |
| Calidad y pruebas | 1 | Sin pruebas ni linter; 2 pendientes `TODO`/`FIXME`. |
| Observabilidad | 1 | Solo `print`/`console.log`; sin logging estructurado. |
| Documentación | 2 | `README.md` mínimo, sin instalación ni API. |
| Mantenibilidad y deuda técnica | 3 | Código pequeño y legible; deuda concentrada en seguridad. |

## 4. Hallazgos

| # | Hallazgo | Severidad | Evidencia | Impacto |
|---|----------|-----------|-----------|---------|
| 1 | Archivo `.env` versionado | Alta | `senales_riesgo.env_versionado = [".env"]` | Fuga de credenciales en el repositorio. |
| 2 | Secreto embebido en el código | Alta | `src/db.py` (coincidencia de `password=`) | Exposición de contraseña de base de datos. |
| 3 | Dependencias sin versiones fijadas | Media | `requirements.txt` (`requests` sin pin) | Builds no reproducibles; riesgo de breaking changes. |
| 4 | Pendientes sin resolver | Baja | 2 coincidencias `TODO`/`FIXME` | Deuda técnica acumulada. |
| 5 | Falta de logging estructurado | Baja | `print`/`console.log` | Dificulta el diagnóstico en producción. |

## 5. Plan de mejora

| Prioridad | Acción | Esfuerzo | Resultado esperado |
|-----------|--------|----------|--------------------|
| 1 | Añadir `.env` a `.gitignore` y `git rm --cached .env`; rotar credenciales. | Bajo | Credenciales fuera del control de versiones. |
| 2 | Leer `DB_PASSWORD` desde `os.environ` en `src/db.py` y eliminar el literal. | Bajo | Sin secretos en el código. |
| 3 | Fijar versiones en `requirements.txt` y generar un lock. | Bajo | Builds reproducibles. |
| 4 | Añadir logging estructurado y manejo de errores. | Medio | Mejor observabilidad. |
| 5 | Resolver los `TODO`/`FIXME` y añadir pruebas básicas. | Medio | Menor deuda técnica. |

## 6. No verificado

No se ejecutó el código ni se analizó en tiempo de ejecución; el análisis es estático. La severidad asume una intención de producción; en un prototipo descartable, la severidad de los hallazgos 3–5 sería Baja.
