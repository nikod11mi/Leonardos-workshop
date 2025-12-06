from __future__ import annotations

from world.workshop_state import WorkshopState


class MaterialsSystem:
    """Backend-only utilities for managing workshop materials."""

    def purchase_material(
        self,
        workshop_state: WorkshopState,
        material_name: str,
        amount: int,
        price_per_unit: float,
    ) -> int:
        if amount <= 0:
            raise ValueError("Amount to purchase must be positive.")
        if price_per_unit < 0:
            raise ValueError("Price per unit cannot be negative.")
        self._validate_material_exists(workshop_state, material_name)

        total_cost = amount * price_per_unit
        if workshop_state.money < total_cost:
            raise ValueError("Not enough money to purchase materials.")

        workshop_state.money -= total_cost
        workshop_state.materials[material_name] += amount
        return workshop_state.materials[material_name]

    def remove_material(
        self, workshop_state: WorkshopState, material_name: str, amount: int
    ) -> int:
        if amount <= 0:
            raise ValueError("Amount to remove must be positive.")
        self._validate_material_exists(workshop_state, material_name)

        current_amount = workshop_state.materials.get(material_name, 0)
        if current_amount < amount:
            raise ValueError("Not enough material available to remove.")

        workshop_state.materials[material_name] = current_amount - amount
        return workshop_state.materials[material_name]

    def _validate_material_exists(
        self, workshop_state: WorkshopState, material_name: str
    ) -> None:
        if material_name not in workshop_state.materials:
            raise ValueError(f"Material '{material_name}' is not tracked.")
