# interface_adapters/controllers/bc3_to_csv_controller.py
"""
Orquesta el flujo completo con el parser de nodos (build_tree_service).

Pasos:
    1) build_tree()   – lee los registros ~C|, ~T|, ~D|, ~M|...
    2) export_to_csv – aplana el árbol Node y genera todas las columnas
"""

from pathlib import Path

from application.services.build_tree_service import build_tree
from application.services.export_csv_service import export_to_csv


def run(bc3_file: Path, csv_file: Path) -> None:
    if not bc3_file.exists():
        raise FileNotFoundError(bc3_file)

    # 1) construir árbol completo (capítulo, partida, descompuesto, mediciones…)
    roots = build_tree(bc3_file)

    # 2) exportar a CSV con todas las columnas (tipo, codigo, desc*, unidad, precio,
    #    cantidad_pres, importe_pres, hijos, mediciones)
    export_to_csv(roots, csv_file)
    print(f"CSV generado → {csv_file.resolve()}")
