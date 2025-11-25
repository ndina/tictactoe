from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional

from core.board import Board
from core.types import PlayerMark, Move, Player


class GameStatus(Enum):
    ONGOING = "ongoing"
    DRAW = "draw"
    WIN = "win"


@dataclass(frozen=True)
class GameResult:
    status: GameStatus
    winner: Optional[PlayerMark] = None


@dataclass(frozen=True)
class GameState:
    board: Board
    current_mark: PlayerMark


class GameEngine:
    def __init__(
        self,
        players: Dict[PlayerMark, Player],
        board_size: int = 3,
        starting_mark: PlayerMark = "X",
    ) -> None:
        if set(players.keys()) != {"X", "O"}:
            raise ValueError("Players dict must have exactly 'X' and 'O' keys")

        if starting_mark not in ("X", "O"):
            raise ValueError("starting_mark must be 'X' or 'O'")

        self._players = players
        self._state = GameState(board=Board.empty(size=board_size), current_mark=starting_mark)

    @property
    def state(self) -> GameState:
        return self._state

    def step(self) -> GameResult:
        """
        Perform a single turn: ask the current player for a move,
        apply it to the board, update state, and return the new game result.
        """
        player = self._players[self._state.current_mark]
        move: Move = player.choose_move(self._state.board, self._state.current_mark)

        new_board = self._state.board.apply_move(move, self._state.current_mark)
        winner = new_board.winner()
        if winner is not None:
            self._state = GameState(board=new_board, current_mark=self._state.current_mark)
            return GameResult(status=GameStatus.WIN, winner=winner)

        if new_board.is_full():
            self._state = GameState(board=new_board, current_mark=self._state.current_mark)
            return GameResult(status=GameStatus.DRAW)

        next_mark: PlayerMark = "O" if self._state.current_mark == "X" else "X"
        self._state = GameState(board=new_board, current_mark=next_mark)
        return GameResult(status=GameStatus.ONGOING)
