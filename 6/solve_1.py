#! /usr/bin/env python3

from file import get_file_data


def op(n1: int, n2: int, oper: str) -> int:
    # print(f"{n1} {oper} {n2}")
    match oper:
        case "*":
            return n1 * n2
        case "+":
            return n1 + n2
        case _:
            print("unrecognized op " + oper)
            return -1


def main():
    data = get_file_data()
    print(data)
    n_dict: dict[int, list[int]] = dict()

    lines = data.strip().split("\n")
    total = 0
    # print(lines)
    for line in lines:
        ans = 0
        # print(f"{line}: {line.split()}")
        for col, n in enumerate(line.split()):
            # print(f"{col}: {n}")
            n_list = n_dict.setdefault(col, list())
            if n in "+*":
                for i in range(len(n_list) - 1):
                    ans = op(n_list[i], n_list[i + 1], n)
                    n_list[i + 1] = ans
                total += ans
            else:
                n_list.append(int(n.strip()))
                # print(n_dict)
    print(total)


if __name__ == "__main__":
    main()
