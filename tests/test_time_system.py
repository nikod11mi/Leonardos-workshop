from systems.time_system import TimeSystem
from world.workshop_state import WorkshopState


def test_time_system_advances_days_and_resets_counter() -> None:
    workshop_state = WorkshopState()
    time_system = TimeSystem(ticks_per_day=10)

    for _ in range(10):
        time_system.tick(workshop_state)

    assert workshop_state.day == 2
    assert time_system.tick_counter == 0

    for _ in range(10):
        time_system.tick(workshop_state)

    assert workshop_state.day == 3
    assert time_system.tick_counter == 0
