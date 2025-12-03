"""
--- Part Two ---

The escalator doesn't move. The Elf explains that it probably needs more joltage to overcome the static friction of the system and hits the big red "joltage limit safety override" button. You lose count of the number of times she needs to confirm "yes, I'm sure" and decorate the lobby a bit while you wait.

Now, you need to make the largest joltage by turning on exactly twelve batteries within each bank.

The joltage output for the bank is still the number formed by the digits of the batteries you've turned on; the only difference is that now there will be 12 digits in each bank's joltage output instead of two.

Consider again the example from before:

987654321111111
811111111111119
234234234234278
818181911112111

Now, the joltages are much larger:

    In 987654321111111, the largest joltage can be found by turning on everything except some 1s at the end to produce 987654321111.
    In the digit sequence 811111111111119, the largest joltage can be found by turning on everything except some 1s, producing 811111111119.
    In 234234234234278, the largest joltage can be found by turning on everything except a 2 battery, a 3 battery, and another 2 battery near the start to produce 434234234278.
    In 818181911112111, the joltage 888911112111 is produced by turning on everything except some 1s near the front.

The total output joltage is now much larger: 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619.

What is the new total output joltage?
"""


def find_max_num(line: str) -> int:
    digits_list = list(line)
    digits_list = list(map(int, digits_list))
    while len(digits_list) > 12:
        current_min = min(digits_list)
        digits_list.remove(current_min)

    print("".join(map(str, digits_list)), "lenghth of digits_list:", len(digits_list))
    return int("".join(map(str, digits_list)))


def calculate_total_joltage(input_file: str):
    total_joltage = 0
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            if not line.strip():
                continue
            total_joltage += find_max_num(line.strip())
    return total_joltage


if __name__ == '__main__':
    print("Total output joltage is:", calculate_total_joltage("day3/input_test.txt"))
    # print("Total output joltage is:", calculate_total_joltage("day3/input.txt"))
