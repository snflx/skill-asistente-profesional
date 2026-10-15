---
name: auditor-tecnico-proyectos
description: Auditoría técnica y revisión de arquitectura de proyectos de software para Ingeniería de Sistemas/TI. Inventaría el repositorio, mide tamaño y complejidad, detecta riesgos de seguridad, escalabilidad y deuda técnica, y emite un informe accionable con prioridades. Úsala siempre que se pida revisar, auditar, evaluar, diagnosticar o auditar un proyecto, repositorio, arquitectura, stack o código; analizar calidad, seguridad, rendimiento o deuda técnica; o preparar documentación técnica de un sistema, aunque no se mencione la palabra "auditoría".
---

# Auditor Técnico de Proyectos

Una auditoría es un **barrido exhaustivo** seguido de un **informe priorizado**. El error clásico es opinar antes de medir: se lee el README, se intuye el resto y se escribe un veredicto. Esta skill invierte el orden — primero inventaría con evidencia, después juzga cada dimensión.

## Cuándo se activa

- Revisión, auditoría o diagnóstico de un proyecto, repositorio, arquitectura o stack.
- Análisis de calidad, seguridad, escalabilidad, rendimiento o deuda técnica.
- Preparación de documentación técnica (informe de estado, plan de mejora, ADR de hallazgos).

## Flujo

### 1. Inventaría con evidencia

Ejecuta el escáner sobre la raíz del proyecto:

```
python scripts/escanear_proyecto.py <ruta-del-proyecto> --json reporte_scan.json
```

El script es determinista y sin dependencias: cuenta archivos y líneas por lenguaje, lista manifiestos de dependencias, y marca señales objetivas de riesgo (`.env` versionado, secretos aparentes, TODOs, archivos pesados). No interpreta: entrega **hechos**.

Si no hay Python disponible, reconstruye el mismo inventario a mano con las herramientas de listado y búsqueda, y dilo en el informe.

**Criterio de término:** el inventario cubre todo el árbol (todos los lenguajes, manifiestos y señales de riesgo presentes). Sin inventario completo no se pasa al paso 2.

### 2. Evalúa cada dimensión

Recorre la [checklist de arquitectura](references/checklist-arquitectura.md) y puntúa **cada** dimensión contra la evidencia del inventario. La checklist es la barra de exhaustividad: ningún apartado queda sin veredicto.

Dimensiones: estructura y capas, dependencias, seguridad, escalabilidad, calidad y pruebas, observabilidad, documentación, mantenibilidad.

**Criterio de término:** cada dimensión tiene una nota y una justificación anclada a un hecho del inventario (archivo, conteo o hallazgo), no a una impresión.

### 3. Emite el informe

Usa la [plantilla de informe](assets/plantilla-reporte.md). Estructura obligatoria: resumen ejecutivo, tabla de hallazgos con severidad (Alta/Media/Baja) e impacto, y plan de mejora ordenado por esfuerzo/beneficio.

**Criterio de término:** el informe tiene un hallazgo accionable por riesgo detectado y una recomendación concreta (con comando o cambio de archivo) para cada hallazgo de severidad Alta.

## Principios

- **Evidencia sobre opinión.** Cada afirmación se ancla a un artefacto del inventario. Si algo no se pudo verificar, se declara como "no verificado", nunca se inventa.
- **Prioriza por impacto × esfuerzo**, no por orden de descubrimiento.
- **Separa hecho de interpretación** en todo el informe.
- Cuando falte contexto de negocio que cambie la severidad (p. ej. si es un prototipo o producción), pregunta una vez y ajusta.

## Referencias

- [checklist-arquitectura.md](references/checklist-arquitectura.md) — rúbrica por dimensión.
- [plantilla-reporte.md](assets/plantilla-reporte.md) — formato de salida.
- [escanear_proyecto.py](scripts/escanear_proyecto.py) — inventario determinista.
