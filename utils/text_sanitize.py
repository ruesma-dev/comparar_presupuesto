# utils/text_sanitize.py
r"""
Normaliza texto de BC3

• Elimina caracteres de sustitución y controles
• Quita acentos/diéresis
• Conserva separadores del formato (~ | \)
"""
from __future__ import annotations

import string
import unicodedata

_ALLOWED: set[str] = set(string.printable) | {"|", "~", "\\"}


def _strip_accents(txt: str) -> str:
    nfkd = unicodedata.normalize("NFKD", txt)
    return "".join(ch for ch in nfkd if not unicodedata.combining(ch))


def clean_text(text: str) -> str:
    text = _strip_accents(text)
    return "".join(
        ch
        for ch in text
        if ch in _ALLOWED or ch.isalnum() or ch.isspace()
    )
