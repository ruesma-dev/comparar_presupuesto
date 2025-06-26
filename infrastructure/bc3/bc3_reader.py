# infrastructure/bc3/bc3_reader.py
"""
Lector de registros FIEBDC-3 (~C|, ~T|, ~D|, …).

BC3Register          – named-tuple con (tag, fields, raw)
iter_registers(path) – iterador que devuelve un BC3Register por línea útil
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterator, List, NamedTuple

ENCODING = "latin-1"


class BC3Register(NamedTuple):
    tag: str           # e.g. '~C', '~T', '~D', …
    fields: List[str]  # lista de campos sin separador final
    raw: str           # línea completa original (sin \n)


def iter_registers(path: Path) -> Iterator[BC3Register]:
    """
    Recorre *path* línea a línea y devuelve únicamente registros válidos.
    Ignora vacías y comentarios (/* … */).

    Ejemplo de uso:
        for reg in iter_registers(Path('presupuesto.bc3')):
            print(reg.tag, reg.fields)
    """
    with path.open(encoding=ENCODING, errors="ignore") as fh:
        for line in fh:
            if not line or line.startswith("/*"):
                continue                       # comentario
            if not line.startswith("~"):
                continue                       # no es registro FIEBDC
            if "|" not in line:
                continue                       # registro mal formado
            tag = line[:2]                     # '~C', '~T', …
            _, rest = line.split("|", 1)
            fields = rest.rstrip("\n").split("|")
            yield BC3Register(tag, fields, line.rstrip("\n"))


# para que el import «from … import iter_registers» sea explícito
__all__ = ["BC3Register", "iter_registers"]
