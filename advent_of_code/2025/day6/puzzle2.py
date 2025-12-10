"""
--- Part Two ---

The big cephalopods come back to check on how things are going. When they see that your grand total doesn't match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.

Cephalopod math is written right-to-left in columns. Each number is given in its own column, with the most significant digit at the top and the least significant digit at the bottom. (Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +

Reading the problems right-to-left one column at a time, the problems are now quite different:

    The rightmost problem is 4 + 431 + 623 = 1058
    The second problem from the right is 175 * 581 * 32 = 3253600
    The third problem from the right is 8 + 248 + 369 = 625
    Finally, the leftmost problem is 356 * 24 * 1 = 8544

Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again. What is the grand total found by adding together all of the answers to the individual problems?
"""

from functools import reduce
from collections import defaultdict


def apply_op(nums: list[int], op: str) -> int:
    if op == "+":
        return sum(nums)

    if op == "*":
        return reduce(lambda x, y: x * y, nums)

    return 0


def count_grand_total(rows: list[list[int]], ops: list[str]) -> int:
    return sum(apply_op(row, op) for row, op in zip(rows, ops))


def parse_rows(nums: dict[int, list[str]], len_ops: int) -> list[list[int]]:
    rows = [[] for _ in range(len_ops)]
    current_row = 0
    buffer = ""

    for row in nums.values():
        # An empty line separates rows.
        if "".join(row).strip() == "":
            current_row += 1
            continue

        for char in row:
            if char.isdigit():
                buffer += char
            else:
                if buffer:
                    rows[current_row].append(int(buffer))
                    buffer = ""

        # Flush any trailing number at the end of the line.
        if buffer:
            rows[current_row].append(int(buffer))
            buffer = ""

    return rows


def collect_line(line: str, nums: dict[int, list[str]]) -> None:
    for i, char in enumerate(line):
        nums[i].append(char)


def process_input(input_path: str) -> int:
    ops: list[str] = []
    nums: defaultdict[int, list[str]] = defaultdict(list)

    try:
        with open(input_path, encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines):
            line = line.strip("\n")
            if not line:
                continue

            if i == len(lines) - 1:
                ops = line.split()
            else:
                collect_line(line, nums)

    except FileNotFoundError:
        return 0

    if not ops:
        return 0

    rows = parse_rows(nums, len(ops))
    grand_total = count_grand_total(rows, ops)
    return grand_total


if __name__ == "__main__":
    # print(f"The grand total: {process_input('day6/test_input.txt')}")
    print(f"The grand total: {process_input('day6/input.txt')}")
    # The grand total: 7669802156452
