# Checklist de Arquitectura

Rúbrica para puntuar cada dimensión de un proyecto de software. Puntúa de 1 (crítico) a 5 (sólido) y ancla cada nota a un hecho del inventario `reporte_scan.json` o a un archivo concreto.

## 1. Estructura y capas

- ¿Hay separación clara de capas (presentación / lógica / datos)?
- ¿La organización de carpetas corresponde a dominios o features, no a tipos de archivo sueltos?
- ¿Existen puntos de entrada definidos y el acoplamiento entre módulos es bajo?

## 2. Dependencias

- ¿Los manifiestos están presentes y bloqueados (`package-lock.json`, `poetry.lock`)?
- ¿Hay dependencias abandonadas, duplicadas o con versiones fijadas por rangos peligrosos?
- ¿El número de dependencias es proporcional al tamaño del proyecto?

## 3. Seguridad

- ¿Se versiona `.env` o hay credenciales en el código? (señal `env_versionado`, `posibles_secretos`).
- ¿Se validan y escapan las entradas externas?
- ¿Están configurados autenticación, autorización y manejo de secretos?

## 4. Escalabilidad y rendimiento

- ¿El diseño soporta concurrencia y crecimiento horizontal?
- ¿Hay consultas N+1, bucles costosos o falta de índices evidentes?
- ¿Se cachea lo que corresponde y se evitan cargas sincrónicas bloqueantes?

## 5. Calidad y pruebas

- ¿Existen pruebas automatizadas y qué proporción del código cubren?
- ¿Hay análisis estático (linters) y convenciones de estilo aplicadas?
- ¿El código está libre de duplicación severa y funciones excesivamente largas?

## 6. Observabilidad

- ¿Hay registro (logging) estructurado, métricas y trazas?
- ¿Se manejan errores con contexto en lugar de silenciarlos?
- ¿Existe monitoreo de salud (health checks) y alertas?

## 7. Documentación

- ¿README, guía de instalación y documentación de API están presentes y vigentes?
- ¿Hay decisiones arquitectónicas registradas (ADR)?
- ¿El código tiene comentarios donde el *porqué* no es obvio?

## 8. Mantenibilidad y deuda técnica

- ¿Cuántos `TODO`/`FIXME` hay y cuántos son riesgos reales? (señal `pendientes`).
- ¿Los archivos pesados versionados inflan el repositorio? (señal `archivos_pesados`).
- ¿La complejidad del código permite que un nuevo desarrollador contribuya en días, no semanas?

## Escala de severidad

| Severidad | Criterio |
|-----------|----------|
| Alta      | Compromete seguridad, disponibilidad o datos; bloquea producción. |
| Media     | Degrada mantenibilidad o rendimiento; abordable en el corto plazo. |
| Baja      | Mejora de calidad o estilo; sin impacto inmediato. |
