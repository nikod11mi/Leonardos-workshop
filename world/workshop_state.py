from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from systems.contracts import Contract


class WorkshopRoom(str, Enum):
    PAINTING_STUDIO = "Painting Studio"
    LABORATORY = "Laboratory"
    MECHANICAL_WORKSHOP = "Mechanical Workshop"
    LIBRARY = "Library"


@dataclass
class WorkshopState:
    """Tracks the high-level workshop status."""

    day: int = 1
    money: float = 150.0
    reputation: float = 0.0
    inspiration: float = 5.0
    materials: Dict[str, int] = field(
        default_factory=lambda: {"wood": 0, "metal": 0, "pigment": 0}
    )
    daily_upkeep: float = 1.0
    inspiration_gain: float = 0.1
    active_contracts: List["Contract"] = field(default_factory=list)
    rooms: List[WorkshopRoom] = field(
        default_factory=lambda: [
            WorkshopRoom.PAINTING_STUDIO,
            WorkshopRoom.LABORATORY,
            WorkshopRoom.MECHANICAL_WORKSHOP,
            WorkshopRoom.LIBRARY,
        ]
    )
