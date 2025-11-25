from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol, runtime_checkable

PlayerMark = Literal["X", "O"]


@dataclass(frozen=True)
class Move:
    row: int
    col: int


@runtime_checkable
class Player(Protocol):
    @property
    def name(self) -> str:
        ...

    def choose_move(self, board: "Board", mark: PlayerMark) -> Move:
        """
        Decide on the next move for the given board and mark.

        """
        ...
