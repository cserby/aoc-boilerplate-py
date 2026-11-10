from pathlib import Path

INPUTS = Path(__file__).parents[2] / "inputs"


def read_input(name: str) -> str:
    return (INPUTS / name).read_text().strip()


def lines(text: str) -> list[str]:
    return text.splitlines()
