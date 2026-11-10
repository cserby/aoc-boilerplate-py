import sys
from math import prod

from aoc.utils import lines, read_input


def parse(text: str) -> list[int]:
    return [int(line) for line in lines(text)]


def part1(text: str) -> int:
    return sum(parse(text))


def part2(text: str) -> int:
    return prod(parse(text))


if __name__ == "__main__":
    text = read_input(sys.argv[1] if len(sys.argv) > 1 else "day0.example.txt")
    print(f"part1: {part1(text)}")
    print(f"part2: {part2(text)}")
