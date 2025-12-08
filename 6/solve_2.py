#! /usr/bin/env python3

from file import get_file_data


def op(n1: int, n2: int, oper: str) -> int:
    print(f"{n1} {oper} {n2}")
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
    # print(data)
    n_dict: dict[int, list[int]] = dict()

    lines = data.split("\n")
    print(lines)
    total = 0
    new_lines = []
    # skip_space = True
    max_len = 0
    # iterate through each list and obtain the n_digit and add to digit
    n_digit = 0
    new_lines = []
    new_line = []
    ops = []
    n_str = ""
    while n_digit < len(lines[0]):
        n_str = ""
        for r_i, row in enumerate(lines):
            if n_digit >= len(row):
                continue
            if row[n_digit] in "*+":
                ops.append(row[n_digit])
            else:
                n_str += row[n_digit].strip()
        if n_str == "":
            new_lines.append(new_line)
            new_line = []
            n_digit += 1
        else:
            new_line.append(int(n_str))
            n_digit += 1
    new_lines.append(new_line)
    print(new_lines)
    print(ops)
    total_ans = 0
    for r_i, row in enumerate(new_lines):
        ans = row[0]
        for n in range(1, len(row)):
            ans = op(ans, row[n], ops[r_i])
        total_ans += ans
    print(total_ans)
    # for line in lines:
    #     new_line = []
    #     entry = ""
    #     for c_i, ch in enumerate(line):
    #         if entry.strip() == "":
    #             entry += ch
    #         elif not ch == " ":
    #             if c_i > 0 and line[c_i - 1].strip() == "":
    #                 new_line.append(entry)
    #                 entry = ""
    #             entry += ch
    #         elif c_i < len(line) - 1:
    #             if line[c_i + 1].strip() == "":
    #                 entry += ch
    #     if not entry.strip() == "":
    #         new_line.append(entry)
    #     new_lines.append(new_line)
    # print(new_lines)

    # # row = 0
    # col = 0
    # # new_mat = []
    # # ops = []
    # col_mat = []
    # n_digit = 0
    # # specifies which element to grab within the row
    # while col < len(new_lines[0]):
    #     col_row = []
    #     # row = 0
    #     n_str = ""
    #     added_digit = True
    #     # col is the element inside the row
    #     # row is the list of elements inside the matrix
    #     # n_digit is the digit inside the element
    #     # 3 loops
    #     # 1. outer loop: specifies which element inside the row to access
    #     # 2. inner loop: will loop through the rows
    #     # 3.

    #     # specifies whether or not a digit was added in the last loop through the rows
    #     while added_digit:
    #         added_digit = False
    #         for row in new_lines:
    #             if n_digit >= len(row[col]) or (
    #                 row[col][n_digit].strip() == "" or row[col][n_digit] in "*+"
    #             ):
    #                 continue
    #             # there is a digit to be added
    #             added_digit = True

    #             n_str += row[col][n_digit].strip()
    #         if n_str == "":
    #             continue
    #         col_row.append(int(n_str))
    #         n_str = ""
    #         n_digit += 1
    #     col_mat.append(col_row)
    #     col += 1
    #     n_digit = 0

    #     # col += 1
    #     # col_mat.append(new_row)
    # print(col_mat)
    # n_digit = 0
    # r_i = 0
    # col_row = []
    # col_mat = []
    # print(new_mat)
    # while r_i < len(new_mat):
    #     row = new_mat[r_i]
    #     col_n_str = ""

    #     for i, n in enumerate(row):
    #         if n_digit < len(n):
    #             col_n_str = col_n_str + n[n_digit]

    #         # print(col_n)

    #     if col_n_str == "":
    #         r_i += 1
    #         n_digit = 0
    #         col_mat.append(col_row)
    #         col_row = []
    #     else:
    #         n_digit += 1
    #         print(col_n_str)
    #         col_row.append(int(col_n_str))
    # print(col_mat)
    # total = 0
    # for i_op, oper in enumerate(ops):
    #     ans = col_mat[i_op][0]
    #     for i_n in range(1, len(col_mat[i_op])):
    #         ans = op(ans, col_mat[i_op][i_n], oper)
    #     print(ans)
    #     total += ans
    # # for line in lines:
    # # print([list(n) for n in line.split()])
    # print(total)


if __name__ == "__main__":
    main()
