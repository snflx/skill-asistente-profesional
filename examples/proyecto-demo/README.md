# Proyecto Demo — Prueba integrada de la Skill

Proyecto ficticio con riesgos intencionales para probar de extremo a extremo la Skill `auditor-tecnico-proyectos`.

## Contenido

- `src/app.py`, `src/db.py`, `src/index.js` — código con un secreto embebido y pendientes.
- `requirements.txt` — manifiesto de dependencias.
- `reporte_scan.json` — inventario generado por el escáner.
- `informe-auditoria.md` — informe final producido por la Skill.

## Reproducir la prueba

El archivo `.env` **no se versiona** (lo excluye `.gitignore`). Para reproducir el hallazgo de credenciales, créalo localmente:

```bash
printf "API_KEY=abc123def456\nDB_PASSWORD=super-secreto-123\n" > .env
```

Luego ejecuta el flujo de la Skill:

```bash
python ../../.agents/skills/auditor-tecnico-proyectos/scripts/escanear_proyecto.py . --json reporte_scan.json
```

El escáner debe reportar `env_versionado: [".env"]`, `posibles_secretos: ["src\\db.py"]` y `pendientes: 2`.
