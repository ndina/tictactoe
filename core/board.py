from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional, Tuple, List

from .types import PlayerMark, Move


class InvalidMoveError(ValueError):
    """Raised when a move is invalid for the current board state."""


Grid = Tuple[Tuple[Optional[PlayerMark], ...], ...]


@dataclass(frozen=True)
class Board:
    """
    Immutable representation of a Tic-Tac-Toe board.

    - Board is immutable: operations return a new instance.
    - Size is configurable, default 3x3 (classic Tic-Tac-Toe).
    """

    size: int
    _grid: Grid

    @classmethod
    def empty(cls, size: int = 3) -> "Board":
        if size < 1:
            raise ValueError("Board size must be >= 1")
        grid: Grid = tuple(tuple(None for _ in range(size)) for _ in range(size))
        return cls(size=size, _grid=grid)

    def cell(self, row: int, col: int) -> Optional[PlayerMark]:
        self._validate_coords(row, col)
        return self._grid[row][col]

    def available_moves(self) -> List[Move]:
        return [
            Move(r, c)
            for r in range(self.size)
            for c in range(self.size)
            if self._grid[r][c] is None
        ]

    def apply_move(self, move: Move, mark: PlayerMark) -> "Board":
        self._validate_coords(move.row, move.col)
        if self._grid[move.row][move.col] is not None:
            raise InvalidMoveError(f"Cell ({move.row}, {move.col}) is already occupied")

        new_rows: List[List[Optional[PlayerMark]]] = [
            list(row) for row in self._grid
        ]
        new_rows[move.row][move.col] = mark
        new_grid: Grid = tuple(tuple(row) for row in new_rows)
        return Board(size=self.size, _grid=new_grid)

    def is_full(self) -> bool:
        return all(cell is not None for row in self._grid for cell in row)

    def winner(self) -> Optional[PlayerMark]:
        for line in self._winning_lines():
            first = line[0]
            if first is not None and all(cell == first for cell in line):
                return first
        return None

    def is_terminal(self) -> bool:
        return self.winner() is not None or self.is_full()

    def _winning_lines(self) -> Iterable[Tuple[Optional[PlayerMark], ...]]:
        for r in range(self.size):
            yield self._grid[r]

        for c in range(self.size):
            yield tuple(self._grid[r][c] for r in range(self.size))

        yield tuple(self._grid[i][i] for i in range(self.size))

        yield tuple(self._grid[i][self.size - 1 - i] for i in range(self.size))

    def _validate_coords(self, row: int, col: int) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise InvalidMoveError(
                f"Coordinates ({row}, {col}) out of bounds for board size {self.size}"
            )

    def __str__(self) -> str:
        def render(cell: Optional[PlayerMark]) -> str:
            return cell if cell is not None else " "

        rows = [
            " | ".join(render(self._grid[r][c]) for c in range(self.size))
            for r in range(self.size)
        ]
        sep = "\n" + "-" * (self.size * 4 - 3) + "\n"
        return sep.join(rows)
