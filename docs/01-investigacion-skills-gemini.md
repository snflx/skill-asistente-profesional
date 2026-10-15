# Investigación: Desarrollo y uso de Skills integrados a Gemini

**Actividad de Seguimiento — Investigación y desarrollo de Skills**
**Ámbito profesional:** Ingeniería de Sistemas / TI
**Autor:** Juan

## 1. ¿Qué es una Skill?

Una **Skill** es un paquete de conocimiento procedimental que extiende lo que un agente de IA puede hacer. No es código ejecutado por el modelo, sino **instrucciones reutilizables** que el agente lee y sigue cuando la tarea encaja. Cada Skill aporta tres cosas:

- **Instrucciones:** protocolos explícitos de cómo abordar una tarea concreta.
- **Buenas prácticas:** convenciones, checklists y estándares.
- **Recursos:** scripts y esquemas auxiliares que el agente puede ejecutar o consultar.

El formato es un estándar abierto: una carpeta con un archivo `SKILL.md` (frontmatter YAML + cuerpo en Markdown) y, opcionalmente, subcarpetas `scripts/`, `references/` y `assets/`.

> El estándar nació en el ecosistema de agentes (Anthropic) y fue adoptado como **estándar abierto** por Google Antigravity y el runtime del agente Antigravity de la Gemini API, además de por Claude Code, Cursor, Codex, OpenCode y otros.

## 2. Skills en el ecosistema Gemini

### 2.1 Dónde viven

Google Antigravity (app, IDE y CLI) carga Skills desde dos ubicaciones:

| Ubicación | Alcance |
|-----------|---------|
| `<raíz-del-workspace>/.agents/skills/<skill>/` | Específica del proyecto; se versiona con el código. |
| `~/.gemini/config/skills/<skill>/` | Global; disponible en todos los workspaces. |

Existe compatibilidad retroactiva con `.agent/skills/`, pero el directorio por defecto es `.agents/skills/`.

### 2.2 Cómo se usan (divulgación progresiva)

1. **Descubrimiento:** al iniciar la conversación el agente ve la lista de Skills (nombre + descripción).
2. **Activación:** si la descripción encaja con la tarea, el agente lee el `SKILL.md` completo.
3. **Ejecución:** el agente sigue las instrucciones mientras trabaja.

La invocación puede ser **autónoma** (el agente decide por contexto) o **manual** (comando `/<nombre-skill>`).

### 2.3 Skills en el Agente Antigravity (Gemini API)

El agente gestionado `antigravity-preview-09-2026` ejecuta en un sandbox Linux de Google y acepta **agentes personalizados** que montan `AGENTS.md` y `SKILL.md`:

```python
from google import genai

client = genai.Client()
interaction = client.interactions.create(
    agent="antigravity-preview-09-2026",
    input="Analiza el proyecto y genera un informe técnico.",
    system_instruction="Eres un auditor de sistemas.",
    files=[
        {"type": "inline",
         "target": ".agents/skills/auditor-tecnico-proyectos/SKILL.md",
         "content": "<contenido del SKILL.md>"},
    ],
)
print(interaction.output_text)
```

El runtime escanea `.agents/` y auto-registra las Skills encontradas.

## 3. Anatomía de una Skill

```
my-skill/
├── SKILL.md       # Requerido: instrucciones y metadatos
├── scripts/       # Opcional: código ejecutable (determinista)
├── references/    # Opcional: documentos consultados bajo demanda
└── assets/        # Opcional: plantillas y esquemas de salida
```

El frontmatter define el nombre y, sobre todo, la **descripción**: es el mecanismo de disparo. Debe declarar *qué hace* y *cuándo usarla*.

## 4. Ecosistema e instalación (skills.sh)

El ecosistema abierto se distribuye vía **skills.sh** con el CLI `skills`:

```bash
npx skills add <owner>/<repo>             # instalar
npx skills add <owner>/<repo> --list      # ver skills disponibles
npx skills add <owner>/<repo> -a opencode # instalar para un agente
```

Skills relevantes para esta actividad y para el ejercicio de Ingeniería de Sistemas:

| Skill | Repositorio | Para qué |
|-------|-------------|----------|
| `skill-creator` | anthropics/skills | Diseñar y optimizar Skills. |
| `writing-for-agents` | mattpocock/skills | Redactar documentos para agentes (SKILL.md, AGENTS.md). |
| `research` | mattpocock/skills | Investigar contra fuentes primarias. |
| `code-review` | mattpocock/skills | Revisar cambios de código. |
| `frontend-design` | anthropics/skills | Diseño de la landing page. |

## 5. Valor para el ejercicio profesional (Ingeniería de Sistemas / TI)

Las Skills convierten conocimiento tácito del ingeniero (checklists, criterios de revisión, plantillas de auditoría) en **procedimiento ejecutable y versionable** por el agente:

- **Estandarización:** todos los informes salen con la misma estructura y rigor.
- **Trazabilidad:** la Skill vive en el repositorio y evoluciona con control de versiones.
- **Reutilización:** un equipo comparte la misma forma de trabajar con la IA.
- **Consistencia:** reduce la varianza entre ejecuciones del agente.

## 6. Conclusiones

1. Las Skills son el mecanismo estándar para inyectar procedimiento experto en agentes Gemini/Antigravity.
2. El costo de adopción es bajo (una carpeta con `SKILL.md`) y el beneficio es alto (consistencia y trazabilidad).
3. Para TI, el mayor valor está en las tareas repetitivas y de criterio: auditorías, revisiones de arquitectura, documentación y despliegues.

## 7. Fuentes

- Google Antigravity Docs — *Agent skills*: https://antigravity.google/docs/skills
- Gemini API Docs — *Antigravity agent*: https://ai.google.dev/gemini-api/docs/antigravity-agent
- Gemini API Docs — *Building managed agents*: https://ai.google.dev/gemini-api/docs/custom-agents
- skill.sh — *The Open Agent Skills Ecosystem*: https://www.skills.sh/
- google-gemini/gemini-skills: https://github.com/google-gemini/gemini-skills
