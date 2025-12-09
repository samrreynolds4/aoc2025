#! /usr/bin/env python3

import math
from collections import namedtuple
from typing import NamedTuple, Self

from file import get_file_data

# Pos = namedtuple("Pos", "x y z circuit")


class Pos:
    def __init__(self, x: int, y: int, z: int, circuit: str):
        self.x = x
        self.y = y
        self.z = z
        self.circuit = circuit

    def __hash__(self) -> int:
        return self.x * 3 + self.y * 5 + self.z * 7

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"


class Edge:
    def __init__(self, d: float, p1: Pos, p2: Pos):
        self.d = d
        self.p1 = p1
        self.p2 = p2

    def __hash__(self) -> int:
        return self.p1.__hash__() + self.p2.__hash__()

    def __repr__(self) -> str:
        return f"{self.p1}-[{self.d}]-{self.p2}"

    def __eq__(self, edge) -> bool:
        return (self.p1 == edge.p1 and self.p2 == edge.p2) or (
            self.p1 == edge.p2 and self.p2 == edge.p1
        )


def get_distance(p1: Pos, p2: Pos, mem: dict[Pos, dict[Pos, float]]) -> float:
    p_mem: dict = dict()
    if p1 in mem:
        p_mem = mem.setdefault(p1, dict())
    if p2 in mem:
        p_mem = mem.setdefault(p2, dict())

    return p_mem.setdefault(
        p2,
        math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2),
    )


def get_closest(p1: Pos, p_list: list[Pos], mem: dict[Pos, dict[Pos, float]]) -> Pos:
    min_dist: float = get_distance(p1, p_list[0], mem)
    min_pos: Pos = p_list[0]
    for i in range(1, len(p_list)):
        p_i = p_list[i]
        d = get_distance(p1, p_i, mem)
        if d < min_dist:
            if not p_i.circuit == p1.circuit:
                min_dist = d
                min_pos = p_i
    min_pos.circuit = p1.circuit
    return min_pos


# get a list of edges and sort them by distance
def get_edges(p_list: list[Pos], mem: dict) -> set[Edge]:
    edges = set()

    for p_x in range(len(p_list)):
        for p_y in range(len(p_list)):
            if p_x == p_y:
                continue
            p1 = p_list[p_x]
            p2 = p_list[p_y]
            e = Edge(d=get_distance(p1, p2, mem), p1=p1, p2=p2)
            if e not in edges:
                edges.add(e)
    return edges


def main():
    # p1 = Pos(12, 21, 3, "1")
    # p2 = Pos(12, 21, 3, "1")
    # print(p1 == p2)
    # s = set()
    # s.add(p1)
    # print(p1 in s)
    # e1 = Edge(0, p1, p2)
    # e2 = Edge(0, p2, p1)
    # print(e1 == e2)
    # s.add(e1)
    # print(e1 in s)
    data = get_file_data()
    lines = data.strip().split("\n")
    positions = set()
    mem = dict()
    for l_i, line in enumerate(lines):
        coors = line.split(",")
        positions.add(
            Pos(x=int(coors[0]), y=int(coors[1]), z=int(coors[2]), circuit=str(l_i))
        )
    print(positions)
    edges = get_edges(list(positions), mem)
    sorted_edges = sorted(list(edges), key=lambda a: a.d)
    groupings: dict[str, set[Pos]] = {p.circuit: set([p]) for p in positions}
    connections = 10
    i = 0
    # for e in sorted_edges:
    #     print(e)
    print(len(sorted_edges))
    while connections > 0:
        # print(sorted_edges[i])
        p1 = sorted_edges[i].p1
        p2 = sorted_edges[i].p2
        i += 1
        # print(i)

        if p2.circuit == p1.circuit:
            continue
        # p2.circuit = p1.circuit
        # if p2.circuit in groupings and p2 in groupings[p2.circuit]:
        # print(f"{p2.circuit} already in {groupings.keys()}")
        # continue

        connections -= 1
        # p2.circuit = p1.circuit
        if p2.circuit in groupings:
            groupings[p1.circuit].remove(p1)
            if len(groupings[p1.circuit]) == 0:
                del groupings[p1.circuit]
            p1.circuit = p2.circuit
            groupings[p2.circuit].add(p1)
            print(f"{p1} and {p2}")
        elif p1.circuit in groupings:
            groupings[p2.circuit].remove(p2)
            if len(groupings[p2.circuit]) == 0:
                del groupings[p2.circuit]
            p2.circuit = p1.circuit
            groupings[p1.circuit].add(p2)
            print(f"{p1} and {p2}")
        else:
            p2.circuit = p1.circuit
            groupings[p1.circuit] = set([p1, p2])
            print(f"new grouping: {p1.circuit}: {p1}, {p2}")

    # print(groupings)

    for key, val in groupings.items():
        print(f"{key}: {len(val)}")


if __name__ == "__main__":
    main()
