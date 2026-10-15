# Brief para la Infografía (generar en ChatGPT)

> Este entregable **no lo genero yo** (la consigna exige que se cree en ChatGPT). Aquí dejo el brief y el prompt listos para pegar en ChatGPT con generación de imágenes.

## Instrucciones de uso

1. Abre ChatGPT (con generación de imágenes habilitada).
2. Pega el **prompt** de abajo.
3. Ajusta textos si lo deseas y exporta en PNG alta resolución.
4. Guarda el resultado en `docs/infografia.png`.

## Especificación visual

- **Formato:** vertical (1080 × 1920) o A3.
- **Paleta:** azul profundo (`#0B1E3B`), turquesa (`#12B5A5`), ámbar (`#F2A63B`) sobre fondo claro (`#F7F9FC`).
- **Estilo:** infografía conceptual plana, íconos lineales, tipografía sans-serif, jerarquía clara.
- **Título:** `SKILLS INTEGRADOS A GEMINI`
- **Subtítulo:** `Automatizando el criterio del ingeniero de sistemas`

## Contenido (bloques)

1. **¿Qué es una Skill?** Paquete de conocimiento procedimental (instrucciones + buenas prácticas + recursos) en formato estándar `SKILL.md`.
2. **Anatomía:** diagrama `SKILL.md` + `scripts/` + `references/` + `assets/`.
3. **Ciclo de vida:** Descubrimiento → Activación → Ejecución.
4. **Dónde viven en Gemini:** `.agents/skills/` (workspace) y `~/.gemini/config/skills/` (global).
5. **Caso de uso TI:** Skill `auditor-tecnico-proyectos` → inventario → rúbrica → informe priorizado.
6. **Beneficios:** estandarización, trazabilidad, reutilización, consistencia.

## Prompt para ChatGPT

```
Crea una infografía conceptual vertical de alta resolución titulada
"SKILLS INTEGRADOS A GEMINI" con el subtítulo "Automatizando el criterio del
ingeniero de sistemas". Estilo plano, profesional, tecnológico.

Seis bloques con íconos:
1. "¿Qué es una Skill?" con icono de rompecabezas; texto: conocimiento
   procedimental reutilizable (instrucciones + buenas prácticas + recursos)
   en formato estándar SKILL.md.
2. "Anatomía" con diagrama de carpeta: SKILL.md, scripts/, references/, assets/.
3. "Ciclo de vida" como flecha circular: Descubrimiento → Activación → Ejecución.
4. "Dónde viven en Gemini": rutas .agents/skills/ (workspace) y
   ~/.gemini/config/skills/ (global).
5. "Caso de uso en TI": flujo auditor-tecnico-proyectos → Inventario → Rúbrica
   → Informe priorizado.
6. "Beneficios": estandarización, trazabilidad, reutilización, consistencia,
   con iconos de check.

Paleta: azul profundo #0B1E3B, turquesa #12B5A5, ámbar #F2A63B, fondo #F7F9FC.
Tipografía sans-serif, mucho aire, jerarquía clara. Sin texto ilegible.
```

## Estado del entregable

- [ ] Generado en ChatGPT
- [ ] Exportado como PNG
- [ ] Guardado en `docs/infografia.png`
