# main.py
"""
Punto de entrada del microservicio **BC3 → CSV**.

Ejemplos
────────
# Usando las rutas por defecto definidas en config/settings.py
python main.py

# Indicando rutas en la línea de comandos
python main.py datos/obra.bc3 salidas/obra.csv
"""
from pathlib import Path
import argparse
import sys

# ─── configuración por defecto ──────────────────────────────────────────────
try:
    from config import settings  # tus constantes centralizadas
    _BC3_DEFAULT = settings.BC3_DEFAULT_PATH
    _CSV_DEFAULT = settings.CSV_DEFAULT_PATH
except (ModuleNotFoundError, AttributeError):
    # si no existe config/settings.py se caen a valores genéricos
    _BC3_DEFAULT = Path("input/presupuesto.bc3")
    _CSV_DEFAULT = Path("output/presupuesto_tree.csv")

# ─── lógica del microservicio ───────────────────────────────────────────────
from interface_adapters.controllers.bc3_to_csv_controller import run as run_pipeline


def _args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="bc3-to-csv",
        description="Convierte un fichero BC3 (FIEBDC-3) en un CSV jerárquico",
    )
    parser.add_argument(
        "bc3_file",
        nargs="?",
        default=_BC3_DEFAULT,
        type=Path,
        help=f"BC3 de entrada (defecto: {_BC3_DEFAULT})",
    )
    parser.add_argument(
        "csv_file",
        nargs="?",
        default=_CSV_DEFAULT,
        type=Path,
        help=f"CSV de salida (defecto: {_CSV_DEFAULT})",
    )
    return parser.parse_args()


def main() -> None:
    args = _args()

    try:
        run_pipeline(args.bc3_file, args.csv_file)
    except FileNotFoundError as exc:
        print(f"[ERROR] No se encontró el fichero: {exc.filename}", file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(f"[ERROR] {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":  # ejecución directa
    main()
