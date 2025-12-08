#! /usr/bin/env python3

from collections import deque
from typing import Deque, Self

from file import get_file_data


def beam_down(x, y, grid: list[list[str]]) -> tuple[tuple[int, int], bool]:
    down_y = y + 1
    if x < 0 or x >= len(grid[y]):
        return (-1, -1), False
    # print(down_y, x, len(grid))
    while down_y < len(grid) and not grid[down_y][x] == "^":
        grid[down_y][x] = "|"
        down_y += 1
        # print(down_y, len(grid))

    if down_y < len(grid) and grid[down_y][x] == "^":
        return (x, down_y), True

    # grid[down_y][x] = "|"
    return (-1, -1), False


def split(x, y, grid: list[list[str]], mem: dict[tuple[int, int], int]) -> int:
    if (x, y) in mem:
        return mem[(x, y)]

    split_y = y + 1
    split_left = x - 1
    split_right = x + 1
    splits = 0
    # if split_y >= len(grid):
    # return 1
    if split_left >= 0:
        grid[split_y][split_left] = "|"
        (left_pos, found) = beam_down(split_left, split_y, grid)
        if found:
            splits += split(*left_pos, grid, mem)
            # splits += mem[left_pos]
        else:
            splits += 1
    if split_right < len(grid[split_y]):
        grid[split_y][split_right] = "|"
        (right_pos, found) = beam_down(split_right, split_y, grid)
        if found:
            splits += split(*right_pos, grid, mem)
            # splits += mem[right_pos]
        else:
            splits += 1
    mem[(x, y)] = splits

    return splits


def get(x, y, grid: list[str]) -> str:
    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[y]):
        return ""
    return grid[y][x]


def print_grid(grid: list[list[str]]):
    for line in grid:
        print("".join(line))


grid_type = list[list[str]]


class Node:
    def __init__(self, x: int, y: int):
        self.left: Self | None = None
        self.right: Self | None = None
        self.x: int = x
        self.y: int = y

    def __repr__(self):
        return f"{self.x},{self.y}"


def main():
    data = get_file_data()
    grid: list[list[str]] = [list(line) for line in data.strip().split("\n")]
    splits = 0

    # stack: Deque[tuple[grid_type, int, int]] = deque()

    # cur = root
    stack: Deque[Node] = deque()
    start_pos = (-1, -1)
    for x in range(len(grid[0])):
        if grid[0][x] == "S":
            start_pos, found = beam_down(x, 0, grid)
    print(split(*start_pos, grid, dict()))

    # stack.append((0, 0))
    # ans = 1
    # while len(stack) > 0:
    #     # print(stack)
    #     cur = stack.popleft()
    #     # print(cur)
    #     if cur.x < 0 or cur.y < 0:
    #         continue
    #     # if s_x < 0 or s_y < 0 or s_y >= len(grid) or s_x >= len(grid[s_y]):
    #     # continue

    #     ans += 1
    #     # print(stack)
    #     if cur.x - 1 > 0:
    #         left_node = Node(*beam_down(cur.x - 1, cur.y, grid))
    #         cur.left = left_node
    #         stack.append(left_node)
    #     if cur.x + 1 < len(grid[cur.y]):
    #         right_node = Node(*beam_down(cur.x + 1, cur.y, grid))
    #         cur.right = right_node
    #         stack.append(right_node)
    # print(ans)
    # print_grid(grid)
    # print(splits)


if __name__ == "__main__":
    main()
