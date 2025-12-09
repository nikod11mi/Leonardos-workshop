import pytest

from systems.economy_system import EconomySystem
from systems.materials_system import MaterialsSystem
from world.workshop_state import WorkshopState


def test_daily_upkeep_reduces_money() -> None:
    state = WorkshopState()
    economy = EconomySystem()

    starting_money = state.money
    economy.apply_daily_upkeep(state)

    assert state.money == starting_money - state.daily_upkeep


def test_inspiration_gain_increases_inspiration() -> None:
    state = WorkshopState()
    economy = EconomySystem()

    starting_inspiration = state.inspiration
    economy.apply_inspiration_gain(state)

    assert state.inspiration == starting_inspiration + state.inspiration_gain


def test_materials_purchase_and_remove() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    materials_system.purchase_material(state, "wood", 3, price_per_unit=2.0)
    assert state.materials["wood"] == 3
    assert state.money == 150.0 - 6.0

    materials_system.remove_material(state, "wood", 2)
    assert state.materials["wood"] == 1


def test_remove_more_material_than_available_raises() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    with pytest.raises(ValueError):
        materials_system.remove_material(state, "wood", 1)


def test_purchasing_materials_updates_counts_and_money() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    materials_system.purchase_material(state, "metal", 5, price_per_unit=1.5)

    assert state.materials["metal"] == 5
    assert state.money == 150.0 - 7.5


def test_purchase_material_with_negative_price_raises() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    with pytest.raises(ValueError):
        materials_system.purchase_material(state, "wood", 1, price_per_unit=-0.1)


def test_purchase_material_with_non_positive_amount_raises() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    with pytest.raises(ValueError):
        materials_system.purchase_material(state, "wood", 0, price_per_unit=1.0)


def test_purchase_unknown_material_raises() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    with pytest.raises(ValueError):
        materials_system.purchase_material(state, "stone", 1, price_per_unit=1.0)


def test_remove_material_with_non_positive_amount_raises() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    with pytest.raises(ValueError):
        materials_system.remove_material(state, "wood", 0)


def test_remove_unknown_material_raises() -> None:
    state = WorkshopState()
    materials_system = MaterialsSystem()

    with pytest.raises(ValueError):
        materials_system.remove_material(state, "stone", 1)
