#!/usr/bin/env python3
"""Escáner de inventario para la skill auditor-tecnico-proyectos.

Cuenta archivos y líneas por lenguaje, detecta manifiestos de dependencias y
marca señales objetivas de riesgo. No interpreta: entrega hechos en JSON.

Uso:
    python escanear_proyecto.py <ruta> [--json reporte_scan.json]
"""

import argparse
import json
import os
import re
import sys

LENGUAJES = {
    ".py": "Python", ".js": "JavaScript", ".mjs": "JavaScript", ".cjs": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".jsx": "JavaScript",
    ".java": "Java", ".kt": "Kotlin", ".go": "Go", ".rs": "Rust",
    ".cs": "C#", ".php": "PHP", ".rb": "Ruby", ".c": "C", ".h": "C",
    ".cpp": "C++", ".cc": "C++", ".hpp": "C++", ".swift": "Swift",
    ".sql": "SQL", ".html": "HTML", ".css": "CSS", ".scss": "CSS",
    ".sh": "Shell", ".ps1": "PowerShell", ".yml": "YAML", ".yaml": "YAML",
    ".json": "JSON", ".md": "Markdown",
}

MANIFIESTOS = [
    "package.json", "requirements.txt", "pyproject.toml", "Pipfile",
    "pom.xml", "build.gradle", "go.mod", "Cargo.toml", "composer.json",
    "Gemfile", "*.csproj", "environment.yml", "poetry.lock", "package-lock.json",
]

IGNORAR_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv", "env",
    "dist", "build", ".next", "target", ".idea", ".vscode", ".mypy_cache",
    ".pytest_cache", "coverage", ".agents", "workspace",
}

SECRETOS = re.compile(
    r"(?i)(api[_-]?key|secret|password|passwd|token|private[_-]?key)\s*[:=]\s*"
    r"['\"][^'\"]{8,}['\"]"
)

EXT_PESADOS = {".zip", ".rar", ".7z", ".iso", ".exe", ".dll", ".mp4", ".mov", ".dmg"}
LIMITE_ARCHIVO_PESADO = 5 * 1024 * 1024


def escanear(raiz):
    archivos_por_lenguaje = {}
    lineas_por_lenguaje = {}
    manifiestos = []
    senales = {
        "env_versionado": [],
        "posibles_secretos": [],
        "pendientes": 0,
        "archivos_pesados": [],
    }
    total_archivos = 0
    total_lineas = 0

    for dirpath, dirnames, filenames in os.walk(raiz):
        dirnames[:] = [d for d in dirnames if d not in IGNORAR_DIRS]
        for nombre in filenames:
            ruta = os.path.join(dirpath, nombre)
            rel = os.path.relpath(ruta, raiz)
            total_archivos += 1
            ext = os.path.splitext(nombre)[1].lower()

            if nombre.startswith(".env") or nombre == "env":
                senales["env_versionado"].append(rel)

            try:
                tam = os.path.getsize(ruta)
            except OSError:
                tam = 0
            if tam > LIMITE_ARCHIVO_PESADO or ext in EXT_PESADOS:
                senales["archivos_pesados"].append({"ruta": rel, "bytes": tam})

            if nombre in MANIFIESTOS or (nombre.endswith(".csproj")):
                manifiestos.append(rel)

            lenguaje = LENGUAJES.get(ext)
            if not lenguaje:
                continue
            archivos_por_lenguaje[lenguaje] = archivos_por_lenguaje.get(lenguaje, 0) + 1

            try:
                with open(ruta, "r", encoding="utf-8", errors="ignore") as fh:
                    contenido = fh.read()
            except OSError:
                continue

            n_lineas = contenido.count("\n") + 1
            total_lineas += n_lineas
            lineas_por_lenguaje[lenguaje] = lineas_por_lenguaje.get(lenguaje, 0) + n_lineas
            senales["pendientes"] += len(re.findall(r"\b(TODO|FIXME|HACK|XXX)\b", contenido))
            if SECRETOS.search(contenido):
                senales["posibles_secretos"].append(rel)

    return {
        "raiz": os.path.abspath(raiz),
        "total_archivos": total_archivos,
        "total_lineas_codigo": total_lineas,
        "archivos_por_lenguaje": dict(sorted(archivos_por_lenguaje.items(), key=lambda x: -x[1])),
        "lineas_por_lenguaje": dict(sorted(lineas_por_lenguaje.items(), key=lambda x: -x[1])),
        "manifiestos": sorted(manifiestos),
        "senales_riesgo": senales,
    }


def main():
    parser = argparse.ArgumentParser(description="Inventario técnico de un proyecto.")
    parser.add_argument("ruta", help="Ruta raíz del proyecto a escanear.")
    parser.add_argument("--json", dest="salida", default=None,
                        help="Archivo donde escribir el JSON (por defecto: stdout).")
    args = parser.parse_args()

    if not os.path.isdir(args.ruta):
        print(f"Error: '{args.ruta}' no es un directorio.", file=sys.stderr)
        return 1

    resultado = escanear(args.ruta)
    texto = json.dumps(resultado, ensure_ascii=False, indent=2)

    if args.salida:
        with open(args.salida, "w", encoding="utf-8") as fh:
            fh.write(texto)
        print(f"Inventario escrito en {args.salida}")
    else:
        print(texto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
