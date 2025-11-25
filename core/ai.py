from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .board import Board
from .types import PlayerMark, Move


@dataclass
class MinimaxAI:
    """
    Unbeatable AI based on minimax with alpha-beta pruning.
    """

    ai_mark: PlayerMark
    name: str = "Computer"
    max_depth: Optional[int] = None

    def choose_move(self, board: Board, mark: PlayerMark) -> Move:
        if mark != self.ai_mark:
            raise ValueError(f"MinimaxAI is configured for mark {self.ai_mark}, got {mark}")

        best_score = float("-inf")
        best_move: Optional[Move] = None

        for move in board.available_moves():
            new_board = board.apply_move(move, self.ai_mark)
            score = self._minimax(
                new_board,
                current_mark=self._opponent_mark(self.ai_mark),
                is_maximizing=False,
                alpha=float("-inf"),
                beta=float("inf"),
                depth=1,
            )
            if score > best_score:
                best_score = score
                best_move = move

        if best_move is None:
            raise RuntimeError("AI could not find a valid move")
        return best_move

    def _minimax(
        self,
        board: Board,
        current_mark: PlayerMark,
        is_maximizing: bool,
        alpha: float,
        beta: float,
        depth: int,
    ) -> float:
        if board.is_terminal() or (
            self.max_depth is not None and depth >= self.max_depth
        ):
            return self._evaluate(board)

        if is_maximizing:
            value = float("-inf")
            for move in board.available_moves():
                child = board.apply_move(move, current_mark)
                score = self._minimax(
                    child,
                    current_mark=self._opponent_mark(current_mark),
                    is_maximizing=False,
                    alpha=alpha,
                    beta=beta,
                    depth=depth + 1,
                )
                value = max(value, score)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return value
        else:
            value = float("inf")
            for move in board.available_moves():
                child = board.apply_move(move, current_mark)
                score = self._minimax(
                    child,
                    current_mark=self._opponent_mark(current_mark),
                    is_maximizing=True,
                    alpha=alpha,
                    beta=beta,
                    depth=depth + 1,
                )
                value = min(value, score)
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return value

    def _evaluate(self, board: Board) -> float:
        winner = board.winner()
        if winner is None:
            return 0.0
        if winner == self.ai_mark:
            return 1.0
        return -1.0

    @staticmethod
    def _opponent_mark(mark: PlayerMark) -> PlayerMark:
        return "O" if mark == "X" else "X"
