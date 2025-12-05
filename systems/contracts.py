from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from world.workshop_state import WorkshopRoom


class PatronTier(str, Enum):
    COMMONER = "Commoner"
    CLERGY = "Clergy"
    NOBILITY = "Nobility"
    RULER = "Ruler"


@dataclass
class Patron:
    name: str
    tier: PatronTier
    reputation: float = 0.0
    notes: str = ""

    def adjust_reputation(self, amount: float) -> float:
        """Adjust the relationship value with Leonardo."""
        self.reputation += amount
        return self.reputation


@dataclass
class Contract:
    name: str
    duration_days: int
    reward_money: float
    prestige: float
    required_room: WorkshopRoom
    patron: Optional[Patron] = None
    description: str = ""
    days_remaining: int = field(init=False)

    def __post_init__(self) -> None:
        self.days_remaining = self.duration_days

    def progress(self, days: int = 1) -> int:
        """Advance the contract timeline."""
        if days < 0:
            raise ValueError("Days must be non-negative.")

        self.days_remaining = max(0, self.days_remaining - days)
        return self.days_remaining
