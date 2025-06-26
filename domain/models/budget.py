# domain/models/budget.py
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Breakdown:
    code: str
    description: str
    unit: str | None
    quantity: float
    price: float
    btype: str  # Mano de obra, Material, Maquinaria…


@dataclass
class Item:
    code: str
    description: str
    unit: str | None
    quantity: float
    price: float
    breakdowns: List[Breakdown] = field(default_factory=list)


@dataclass
class SubChapter:
    code: str
    description: str
    items: List[Item] = field(default_factory=list)


@dataclass
class Chapter:
    code: str
    description: str
    subchapters: List[SubChapter] = field(default_factory=list)


@dataclass
class Budget:
    code: str
    description: str
    chapters: List[Chapter] = field(default_factory=list)
