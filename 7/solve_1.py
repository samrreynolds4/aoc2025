#! /usr/bin/env python3

from collections import deque

from file import get_file_data


def beam_down(x, y, grid: list[list[str]]) -> int:
    down_y = y + 1
    if down_y >= len(grid) or x < 0 or x >= len(grid[down_y]):
        return 0
    if grid[down_y][x] == "^":
        split(x, y, grid)
        return 1

    grid[down_y][x] = "|"
    return 0


def split(x, y, grid: list[list[str]]):
    split_y = y + 1
    split_x1 = x - 1
    split_x2 = x + 1

    if split_y >= len(grid):
        return
    if split_x1 >= 0:
        grid[split_y][split_x1] = "|"
    if split_x2 < len(grid[split_y]):
        grid[split_y][split_x2] = "|"


def get(x, y, grid: list[str]) -> str:
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return ""
    return grid[y][x]


def print_grid(grid: list[list[str]]):
    for line in grid:
        print("".join(line))


def main():
    data = get_file_data()
    grid = [list(line) for line in data.split("\n")]
    splits = 1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S" or grid[y][x] == "|":
                splits += beam_down(x, y, grid)

    print_grid(grid)
    print(splits)


if __name__ == "__main__":
    main()
