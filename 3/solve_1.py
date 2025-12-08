#! /usr/bin/env python3

import sys


def main():
    print("aaa")
    print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python solve_1.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, "r") as f:
        banks = f.read().strip().split()
    total_ans = 0
    for bank in banks:
        spots_left = 11
        starting = 0
        ans = 0
        while spots_left >= 0:
            largest_n = (-1, 0)
            # print(f"starting:{starting}, spots_left:{spots_left}")
            for i, n in enumerate(bank[starting : len(bank) - spots_left]):
                # print(i, n)
                if int(n) > largest_n[0]:
                    largest_n = (int(n), i)
            ans += largest_n[0] * (10 ** (spots_left))
            spots_left -= 1
            starting += largest_n[1] + 1
            # print(largest_n)
        print(ans)
        total_ans += ans
    print(total_ans)


main()
