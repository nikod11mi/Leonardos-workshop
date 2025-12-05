from __future__ import annotations

from world.workshop_state import WorkshopState


class TimeSystem:
    """Skeleton for advancing in-game time."""

    def __init__(self, workshop_state: WorkshopState) -> None:
        self.workshop_state = workshop_state

    def advance_day(self, days: int = 1) -> int:
        """Advance the in-game calendar by a number of days."""
        if days < 0:
            raise ValueError("Days to advance must be non-negative.")

        self.workshop_state.day += days
        return self.workshop_state.day
