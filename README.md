# Tic-Tac-Toe (Python 3.9+)

A clean, extensible, and fully testable implementation of Tic-Tac-Toe written in
Python. The project follows a modular architecture with:

- `core/`: game types, board logic, and AI (Minimax)
- `app/`: game engine and state management
- `cli/`: command-line interface for human players
- `tests/`: pytest unit tests
- `play.py`: single entry point to run the game

---

##  Requirements

- Python **3.9 or newer** (3.10/3.11 recommended)
- `pytest` (optional, for running tests)

---

##  Running the Game

From the project root:

```bash
python play.py
```

---

##  Running Tests

Make sure your `PYTHONPATH` includes the project root:

### Windows CMD

```bash
set PYTHONPATH=.
pytest
```

### PowerShell

```powershell
$env:PYTHONPATH="."
pytest
```

---

##  Project Structure

```
tictactoe/
├── app/
│   ├── __init__.py
│   ├── engine.py
│
├── core/
│   ├── __init__.py
│   ├── board.py
│   ├── ai.py
│   ├── types.py
│
├── cli/
│   ├── __init__.py
│   ├── run.py
│   ├── human_player.py
│
├── tests/
│   ├── __init__.py
│   ├── test_ai.py
│   ├── test_board.py
│
├── play.py
├── README.md
└── .gitignore
```

---

##  Notes

- `MinimaxAI` uses alpha-beta pruning.
- `Move` objects are immutable (`@dataclass(frozen=True)`).
- Engine uses `Protocol` for clean architecture.
