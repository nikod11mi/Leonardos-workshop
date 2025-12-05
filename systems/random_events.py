from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class RandomEvent:
    """Placeholder for random workshop events."""

    name: str
    description: str


class RandomEventSystem:
    """Skeleton system for producing random events."""

    def __init__(self) -> None:
        self._event_pool: List[RandomEvent] = [
            RandomEvent("Plague in the city", "Production slows as illness spreads."),
            RandomEvent("Flooded streets", "Deliveries are delayed by high waters."),
            RandomEvent("Eager students visit", "Inspiration rises after teaching."),
            RandomEvent("War on the horizon", "Patrons hesitate to spend."),
        ]

    def possible_events(self) -> List[RandomEvent]:
        """Return currently available random events (placeholder)."""
        return list(self._event_pool)
