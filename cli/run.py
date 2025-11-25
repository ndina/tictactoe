from __future__ import annotations

from app.engine import GameEngine, GameStatus
from core.ai import MinimaxAI
from cli.human_player import HumanCLIPlayer
from core.types import PlayerMark


def _ask_human_mark() -> PlayerMark:
    while True:
        choice = input("Do you want to be X and go first? [Y/n]: ").strip().lower()
        if choice in ("", "y", "yes"):
            return "X"
        if choice in ("n", "no"):
            return "O"
        print("Please answer 'y' or 'n'.")


def main() -> None:
    print("=== Tic-Tac-Toe test game ===")

    human_mark: PlayerMark = _ask_human_mark()
    ai_mark: PlayerMark = "O" if human_mark == "X" else "X"

    human = HumanCLIPlayer(name="You")
    ai = MinimaxAI(ai_mark=ai_mark, name="Computer")

    players = {
        human_mark: human,
        ai_mark: ai,
    }

    starting_mark = human_mark
    engine = GameEngine(players=players, board_size=3, starting_mark=starting_mark)

    while True:
        result = engine.step()
        state = engine.state

        if result.status == GameStatus.ONGOING:
            continue

        from core.board import Board 
        board: Board = state.board
        print("\nFinal board:")
        print(board)

        if result.status == GameStatus.DRAW:
            print("\nIt's a draw!")
        elif result.status == GameStatus.WIN:
            if result.winner == human_mark:
                print("\nYou win! 🎉")
            else:
                print("\nComputer wins. Better luck next time!")

        break


if __name__ == "__main__":
    main()
