from tictactoe.core.board import Board, InvalidMoveError
from tictactoe.core.types import Move


def test_apply_move_and_read_cell():
    board = Board.empty()
    move = Move(row=1, col=1)
    new_board = board.apply_move(move, "X")

    assert board.cell(1, 1) is None 
    assert new_board.cell(1, 1) == "X"


def test_row_winner_detected():
    grid = (
        ("X", "X", "X"),
        (None, None, None),
        (None, None, None),
    )
    board = Board(size=3, _grid=grid)
    assert board.winner() == "X"


def test_column_winner_detected():
    grid = (
        ("O", None, None),
        ("O", None, None),
        ("O", None, None),
    )
    board = Board(size=3, _grid=grid)
    assert board.winner() == "O"


def test_diagonal_winner_detected():
    grid = (
        ("X", None, None),
        (None, "X", None),
        (None, None, "X"),
    )
    board = Board(size=3, _grid=grid)
    assert board.winner() == "X"


def test_invalid_move_raises():
    board = Board.empty()
    first = board.apply_move(Move(0, 0), "X")
    try:
        first.apply_move(Move(0, 0), "O")
        assert False, "Expected InvalidMoveError"
    except InvalidMoveError:
        pass
