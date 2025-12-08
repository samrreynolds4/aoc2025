#! /usr/bin/env python3

from collections import deque
from typing import Deque, Self

from file import get_file_data


def beam_down(x, y, grid: list[list[str]]) -> tuple[int, int]:
    down_y = y + 1
    if x < 0 or x >= len(grid[y]):
        return (-1, -1)
    # print(down_y, x, len(grid))
    while down_y < len(grid) and not grid[down_y][x] == "^":
        grid[down_y][x] = "|"
        down_y += 1
        # print(down_y, len(grid))

    if down_y < len(grid) and grid[down_y][x] == "^":
        return (x, down_y)

    # grid[down_y][x] = "|"
    return (-1, -1)


def split(x, y, grid: list[list[str]], right: bool):
    split_y = y + 1
    split_left = x - 1
    split_right = x + 1

    if split_y >= len(grid):
        return
    if not right and split_left >= 0:
        grid[split_y][split_left] = "|"
    if right and split_right < len(grid[split_y]):
        grid[split_y][split_right] = "|"


def get(x, y, grid: list[str]) -> str:
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return ""
    return grid[y][x]


def print_grid(grid: list[list[str]]):
    for line in grid:
        print("".join(line))


grid_type = list[list[str]]


class Node:
    def __init__(self, x: int, y: int)
        self.left: Self|None = None
        self.right: Self|None = None
        self.x: int = x
        self.y: int = y


def main():
    data = get_file_data()
    grid: list[list[str]] = [list(line) for line in data.strip().split("\n")]
    splits = 1

    # stack: Deque[tuple[grid_type, int, int]] = deque()
    root: Node
    stack: Deque[] = deque()

    for x in range(len(grid[0])):
        if grid[0][x] == "S":
            root = Node(*beam_down(x, 0, grid))
            stack.append(root)
    # stack.append((0, 0))
    ans = 1
    while len(stack) > 0:
        cur = stack.pop()
        # if s_x < 0 or s_y < 0 or s_y >= len(grid) or s_x >= len(grid[s_y]):
            # continue

        ans += 1
        print(stack)
        if s_x - 1 > 0:
            cur.node
            stack.append(beam_down(s_x - 1, s_y, grid))
        if s_x + 1 < len(grid[s_y]):
            stack.append(beam_down(s_x + 1, s_y, grid))
    print(ans)
    print_grid(grid)
    print(splits)


if __name__ == "__main__":
    main()
