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


def do_math(nums: list[int], op: str) -> int:
    if nums:
        if op == "+":
            return sum(nums)

        if op == "*":
            return reduce(lambda x, y: x * y, nums)

    return 0


def count_grand_total(nums: list[list[int]], ops: list[str]) -> int:
    grand_total = 0
    prev_op = ""

    for i, op in enumerate(ops):
        if op == "+" or op == "*":
            prev_op = op

        grand_total += do_math(nums[i], prev_op)
        print(f"i={i}, op={op}, prev_op={prev_op}, grand_total={grand_total}, nums[i]={nums[i]}")

    return grand_total


def process_rows(nums: dict[int, list[str]]) -> list[list[int]]:
    result = []
    num = ""

    for k, v in nums.items():
        result.append([])
        for i, n in enumerate(v):
            if n.isdigit():
                num += n
            else:
                if num:
                    result[k].append(int(num))
                    num = ""

        if num:
            result[k].append(int(num))
            num = ""
    return result


def processed_line(line: str, nums: dict[int, list[str]]) -> None:
    for i, n in enumerate(line):
        nums[i].append(n)


def process_input(input_path: str) -> int:
    ops = []
    nums = defaultdict(list)

    try:
        f = open(input_path)
        lines = f.readlines()
        for i, line in enumerate(lines):
            if not line:
                break

            if i == len(lines) - 1:
                ops = line
            else:
                processed_line(line, nums)

    except FileNotFoundError:
        return 0

    finally:
        f.close()
    print(f"before process rows: {nums}")
    cols = process_rows(nums)
    print(f"after process rows: {cols}")
    return count_grand_total(cols, ops)


if __name__ == "__main__":
    print(f"The grand total: {process_input('day6/test_input.txt')}")
    # print(f"The grand total: {process_input('day6/input.txt')}")
