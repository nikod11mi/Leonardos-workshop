from __future__ import annotations

from world.workshop_state import WorkshopState


class TimeSystem:
    """Simple time tracker that converts frame ticks into in-game days."""

    def __init__(self, ticks_per_day: int = 300) -> None:
        if ticks_per_day <= 0:
            raise ValueError("ticks_per_day must be a positive integer.")
        self.ticks_per_day: int = ticks_per_day
        self._tick_counter: int = 0

    @property
    def tick_counter(self) -> int:
        """Current progress toward the next in-game day."""
        return self._tick_counter

    def tick(self, workshop_state: WorkshopState) -> None:
        """Advance the internal counter and progress the workshop's day."""
        self._tick_counter += 1
        if self._tick_counter >= self.ticks_per_day:
            workshop_state.day += 1
            self._tick_counter = 0
