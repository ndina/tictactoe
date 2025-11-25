from __future__ import annotations

from dataclasses import dataclass

from core.board import Board
from core.types import Move, PlayerMark


@dataclass
class HumanCLIPlayer:
    name: str = "You"

    def choose_move(self, board: Board, mark: PlayerMark) -> Move:
        while True:
            self._print_board(board, mark)
            raw = input(
                f"{self.name} ({mark}), choose a cell "
                "(1-9 or 'row col' with 1-based indices): "
            ).strip()
            try:
                move = self._parse_input(raw, board)
                if board.cell(move.row, move.col) is not None:
                    print("That cell is already occupied. Try again.\n")
                    continue
                return move
            except ValueError as e:
                print(f"Invalid input: {e}\n")

    def _parse_input(self, raw: str, board: Board) -> Move:
        if not raw:
            raise ValueError("Input cannot be empty")

        if raw.isdigit() and len(raw) == 1 and board.size == 3:
            idx = int(raw) - 1
            if idx < 0 or idx >= 9:
                raise ValueError("Number must be between 1 and 9")
            row, col = divmod(idx, 3)
            return Move(row=row, col=col)

        parts = raw.split()
        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            raise ValueError("Expected a single digit (1-9) or 'row col'")

        row = int(parts[0]) - 1
        col = int(parts[1]) - 1

        if not (0 <= row < board.size and 0 <= col < board.size):
            raise ValueError(f"Row/col must be between 1 and {board.size}")
        return Move(row=row, col=col)

    def _print_board(self, board: Board, mark: PlayerMark) -> None:
        print("\nCurrent board:")
        print(board)

        if board.size == 3:
            print("\nCell numbers:")
            cells = [str(i) for i in range(1, 10)]
            rows = [" | ".join(cells[r * 3 : (r + 1) * 3]) for r in range(3)]
            print("\n" + "-" * 11)
            print("\n".join(rows))
        print()
