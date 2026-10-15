# Documentación del desarrollo de la Skill

**Skill:** `auditor-tecnico-proyectos`
**Ámbito:** Ingeniería de Sistemas / TI
**Formato:** estándar abierto `SKILL.md` (compatible con Gemini / Antigravity)

## 1. Problema y objetivo

En el ejercicio de TI, las auditorías y revisiones técnicas dependen del criterio del ingeniero y varían entre ejecuciones. El objetivo fue **convertir ese criterio en un procedimiento reproducible** que un agente Gemini pueda ejecutar de forma consistente.

**Objetivo de la Skill:** dado un proyecto de software, inventariarlo con evidencia, evaluarlo contra una rúbrica y emitir un informe priorizado y accionable.

## 2. Diseño (decisiones)

| Decisión | Alternativa descartada | Motivo |
|----------|------------------------|--------|
| Inventariar **antes** de opinar | Analizar y opinar a la vez | Elimina el sesgo de intuición sin datos. |
| Escáner **determinista** en Python stdlib | Cálculo hecho "a mano" por el modelo | Reproducible, sin dependencias, resultados iguales cada vez. |
| Rúbrica en `references/` | Rúbrica dentro de `SKILL.md` | Divulgación progresiva: solo se carga lo necesario. |
| Plantilla en `assets/` | Formato libre | Estructura de salida consistente. |
| Descripción con disparadores explícitos | Descripción genérica | Combate el sub-disparo (*undertriggering*) de las Skills. |

## 3. Estructura entregada

```
.agents/skills/auditor-tecnico-proyectos/
├── SKILL.md                          # Flujo de 3 pasos + criterios de término
├── scripts/escanear_proyecto.py      # Inventario determinista (stdlib)
├── references/checklist-arquitectura.md  # Rúbrica de 8 dimensiones
└── assets/plantilla-reporte.md       # Formato del informe
```

## 4. El flujo de la Skill

1. **Inventaría con evidencia** → ejecuta el escáner, obtiene hechos (`reporte_scan.json`).
2. **Evalúa cada dimensión** → recorre la checklist de 8 dimensiones contra el inventario.
3. **Emite el informe** → aplica la plantilla, prioriza por impacto × esfuerzo.

Cada paso tiene un **criterio de término** verificable; por ejemplo, el paso 2 exige que cada dimensión tenga una nota *anclada a un hecho*, no a una impresión.

## 5. Pruebas de funcionamiento

### 5.1 Prueba unitaria del escáner

```bash
python .agents/skills/auditor-tecnico-proyectos/scripts/escanear_proyecto.py .agents/skills/auditor-tecnico-proyectos
```

Salida (extracto):

```json
{
  "total_archivos": 4,
  "total_lineas_codigo": 303,
  "archivos_por_lenguaje": {"Markdown": 3, "Python": 1},
  "senales_riesgo": {"env_versionado": [], "posibles_secretos": [], "pendientes": 6, "archivos_pesados": []}
}
```

### 5.2 Pruebas de disparo (evals)

Ver `evals/evals.json`: 6 casos (4 que deben disparar la Skill, 2 que no). Se usan para validar que la descripción activa la Skill en el momento correcto y no en tareas vecinas.

### 5.3 Validación del formato

El frontmatter YAML contiene `name` y `description`; la carpeta sigue la estructura del estándar. Validable con el `quick_validate.py` de `skill-creator`.

Resultado:

```
$ python .../quick_validate.py .agents/skills/auditor-tecnico-proyectos
Skill is valid!
```

### 5.4 Prueba integrada de extremo a extremo

Se ejecutó el flujo completo sobre un proyecto ficticio con riesgos intencionales (`examples/proyecto-demo`):

1. **Inventario:** el escáner reportó `env_versionado: [".env"]`, `posibles_secretos: ["src\\db.py"]`, `pendientes: 2` y el manifiesto `requirements.txt`.
2. **Evaluación:** se puntuaron las 8 dimensiones con evidencia.
3. **Informe:** se generó `examples/proyecto-demo/informe-auditoria.md` con 5 hallazgos priorizados (2 de severidad Alta).

Esto demuestra el funcionamiento de la Skill de extremo a extremo a nivel lógico. La validación dentro de la interfaz de Gemini/Antigravity se realiza como paso final de integración (ver sección 6).

## 6. Resultados y limitaciones

- **Resultado:** la Skill produce un inventario reproducible y un informe estructurado; el criterio experto queda capturado y versionado.
- **Limitación 1:** el escáner es estático y no ejecuta el código; no detecta vulnerabilidades en tiempo de ejecución.
- **Limitación 2:** la severidad requiere contexto de negocio; la Skill pregunta una vez cuando el impacto depende de si el proyecto es producción o prototipo.
- **Limitación 3:** la prueba end-to-end dentro de la interfaz de Gemini se realiza en el paso de integración final.

## 7. Referencias

- `docs/01-investigacion-skills-gemini.md`
- Estándar de Skills: https://antigravity.google/docs/skills
