from aoc.day0 import part1, part2
from aoc.utils import read_input

EXAMPLE = read_input("day0.example.txt")


def test_part1_example() -> None:
    assert part1(EXAMPLE) == 10


def test_part2_example() -> None:
    assert part2(EXAMPLE) == 24
