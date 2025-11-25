from tictactoe.core.ai import MinimaxAI
from tictactoe.core.board import Board
from tictactoe.core.types import Move


def test_ai_takes_winning_move():
    grid = (
        ("X", "X", None),
        ("O", "O", None),
        (None, None, None),
    )
    board = Board(size=3, _grid=grid)
    ai = MinimaxAI(ai_mark="X")

    move = ai.choose_move(board, "X")
    assert move == Move(row=0, col=2)


def test_ai_blocks_immediate_loss():
    grid = (
        ("X", "X", None),
        (None, "O", None),
        (None, None, None),
    )
    board = Board(size=3, _grid=grid)
    ai = MinimaxAI(ai_mark="O")

    move = ai.choose_move(board, "O")
    assert move == Move(row=0, col=2)
