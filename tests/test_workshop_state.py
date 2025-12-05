from world.workshop_state import WorkshopState


def test_workshop_state_defaults() -> None:
    state = WorkshopState()

    assert state.money > 0
    assert state.reputation >= 0
    assert state.inspiration > 0
    assert state.active_contracts == []
