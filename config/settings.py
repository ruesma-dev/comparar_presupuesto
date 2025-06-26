# config/settings.py
"""
Parámetros globales del microservicio.

Puedes modificar aquí las rutas por defecto de entrada y salida para no
tener que pasarlas por línea de comandos cada vez.
"""
from pathlib import Path

# ──────────────────────────────────────────────────────────────
# Rutas por defecto
# ──────────────────────────────────────────────────────────────
BC3_DEFAULT_PATH: Path = Path(r"C:\Users\pgris\PycharmProjects\comparar_presupuesto\input\presupuesto_1.bc3")
CSV_DEFAULT_PATH: Path = Path(r"C:\Users\pgris\PycharmProjects\comparar_presupuesto\output\presupuesto_tree.csv")

# ──────────────────────────────────────────────────────────────
# Ajustes de CSV
# ──────────────────────────────────────────────────────────────
CSV_SEP: str = ";"
CSV_ENCODING: str = "utf-8"
