from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from world.workshop_state import WorkshopState


KNOWN_MATERIALS = ("wood", "metal", "pigment")


class PuzzleType(str, Enum):
    GEARS = "gears"
    PIGMENTS = "pigments"
    ANATOMY = "anatomy"


@dataclass
class Contract:
    id: int
    name: str
    reward_money: float
    duration_days: int
    prestige: float
    materials_required: Dict[str, int]
    puzzle_type: PuzzleType
    puzzle_difficulty: int
    start_day: int
    patron: Optional[str] = None

    def __post_init__(self) -> None:
        if self.duration_days <= 0:
            raise ValueError("Contract duration must be positive.")
        if self.reward_money <= 0:
            raise ValueError("Contract reward must be positive.")
        if not (1 <= self.puzzle_difficulty <= 3):
            raise ValueError("Puzzle difficulty must be between 1 and 3.")
        if self.puzzle_type not in PuzzleType:
            raise ValueError("Invalid puzzle type.")
        if self.start_day < 1:
            raise ValueError("Start day must be positive.")

        unknown_materials = [
            material for material in self.materials_required if material not in KNOWN_MATERIALS
        ]
        if unknown_materials:
            raise ValueError(f"Unknown materials in contract: {', '.join(unknown_materials)}.")
        if any(amount <= 0 for amount in self.materials_required.values()):
            raise ValueError("Material requirements must be positive values.")

    def is_expired(self, current_day: int) -> bool:
        """Check whether the contract should expire based on the current day."""
        return current_day >= self.start_day + self.duration_days


class ContractsSystem:
    """Manages active contracts, generation, and expiration."""

    def __init__(self, max_active_contracts: int = 3) -> None:
        self.max_active_contracts = max_active_contracts
        self._next_id = 1

    def maybe_generate_daily_contracts(self, workshop_state: "WorkshopState") -> None:
        """Generate at most one new contract if there is capacity."""
        if len(workshop_state.active_contracts) >= self.max_active_contracts:
            return

        contract = self._build_contract_for_state(workshop_state)
        if contract:
            workshop_state.active_contracts.append(contract)

    def remove_expired_contracts(
        self, workshop_state: "WorkshopState", current_day: int
    ) -> None:
        """Remove contracts that have expired by the given day."""
        workshop_state.active_contracts = [
            contract
            for contract in workshop_state.active_contracts
            if not contract.is_expired(current_day)
        ]

    def _build_contract_for_state(self, workshop_state: "WorkshopState") -> Contract:
        current_day = workshop_state.day
        puzzle_type = self._pick_puzzle_type(current_day)
        difficulty = self._pick_difficulty(workshop_state.reputation, current_day)
        materials_required = self._materials_for_puzzle(puzzle_type, current_day)
        reward = self._reward_for_contract(difficulty, workshop_state.reputation)
        duration = self._duration_for_contract(difficulty)
        name = self._contract_name(puzzle_type)

        contract = Contract(
            id=self._next_id,
            name=name,
            reward_money=reward,
            duration_days=duration,
            prestige=0.1 * difficulty,
            materials_required=materials_required,
            puzzle_type=puzzle_type,
            puzzle_difficulty=difficulty,
            start_day=current_day,
        )
        self._next_id += 1
        return contract

    def _pick_puzzle_type(self, day: int) -> PuzzleType:
        rotation = list(PuzzleType)
        return rotation[(day - 1) % len(rotation)]

    def _pick_difficulty(self, reputation: float, day: int) -> int:
        base = 1 + (day % 3)
        bonus = 1 if reputation >= 5.0 and base < 3 else 0
        return min(3, base + bonus)

    def _materials_for_puzzle(self, puzzle_type: PuzzleType, day: int) -> Dict[str, int]:
        day_offset = (day % 3) + 1  # range 1-3
        if puzzle_type is PuzzleType.GEARS:
            return {"wood": 1 + (day % 2), "metal": day_offset}
        if puzzle_type is PuzzleType.PIGMENTS:
            return {"wood": 1, "pigment": day_offset}
        return {"pigment": 1 + (day % 2), "metal": 1}

    def _reward_for_contract(self, difficulty: int, reputation: float) -> float:
        base_reward = 120.0 + (difficulty * 60.0)
        reputation_bonus = max(0.0, reputation) * 15.0
        return base_reward + reputation_bonus

    def _duration_for_contract(self, difficulty: int) -> int:
        return max(2, 5 - difficulty)

    def _contract_name(self, puzzle_type: PuzzleType) -> str:
        titles = {
            PuzzleType.GEARS: "Workshop Mechanism",
            PuzzleType.PIGMENTS: "Portrait Commission",
            PuzzleType.ANATOMY: "Anatomical Study",
        }
        return f"{titles.get(puzzle_type, 'Contract')} #{self._next_id}"
