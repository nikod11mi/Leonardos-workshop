import pytest

from systems.contracts import Contract, ContractsSystem, PuzzleType
from world.workshop_state import WorkshopState


def test_contract_generation_reaches_capacity() -> None:
    state = WorkshopState()
    contracts_system = ContractsSystem(max_active_contracts=2)

    for _ in range(5):
        contracts_system.maybe_generate_daily_contracts(state)
        state.day += 1

    assert len(state.active_contracts) == 2


def test_generated_contracts_have_valid_fields() -> None:
    state = WorkshopState()
    contracts_system = ContractsSystem()

    for _ in range(3):
        contracts_system.maybe_generate_daily_contracts(state)
        state.day += 1

    allowed_materials = {"wood", "metal", "pigment"}
    allowed_types = {puzzle.value for puzzle in PuzzleType}

    assert state.active_contracts
    for contract in state.active_contracts:
        assert isinstance(contract, Contract)
        assert contract.reward_money > 0
        assert contract.duration_days > 0
        assert set(contract.materials_required).issubset(allowed_materials)
        assert all(amount > 0 for amount in contract.materials_required.values())
        assert contract.puzzle_type.value in allowed_types
        assert 1 <= contract.puzzle_difficulty <= 3


def test_remove_expired_contracts() -> None:
    state = WorkshopState()
    contracts_system = ContractsSystem(max_active_contracts=1)

    contracts_system.maybe_generate_daily_contracts(state)
    assert len(state.active_contracts) == 1
    contract = state.active_contracts[0]

    # Advance time to the day the contract should expire.
    state.day = contract.start_day + contract.duration_days
    contracts_system.remove_expired_contracts(state, state.day)

    assert not state.active_contracts
