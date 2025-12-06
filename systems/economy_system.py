from __future__ import annotations

from world.workshop_state import WorkshopState


class EconomySystem:
    """Handles daily financial and inspiration adjustments."""

    def apply_daily_upkeep(self, workshop_state: WorkshopState) -> float:
        workshop_state.money -= workshop_state.daily_upkeep
        return workshop_state.money

    def apply_inspiration_gain(self, workshop_state: WorkshopState) -> float:
        workshop_state.inspiration += workshop_state.inspiration_gain
        return workshop_state.inspiration
