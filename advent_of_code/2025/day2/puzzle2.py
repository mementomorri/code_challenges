"""
--- Part Two ---

The clerk quickly discovers that there are still invalid IDs in the ranges in your list. Maybe the young Elf was doing other silly patterns as well?

Now, an ID is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs.

From the same example as before:

    11-22 still has two invalid IDs, 11 and 22.
    95-115 now has two invalid IDs, 99 and 111.
    998-1012 now has two invalid IDs, 999 and 1010.
    1188511880-1188511890 still has one invalid ID, 1188511885.
    222220-222224 still has one invalid ID, 222222.
    1698522-1698528 still contains no invalid IDs.
    446443-446449 still has one invalid ID, 446446.
    38593856-38593862 still has one invalid ID, 38593859.
    565653-565659 now has one invalid ID, 565656.
    824824821-824824827 now has one invalid ID, 824824824.
    2121212118-2121212124 now has one invalid ID, 2121212121.

Adding up all the invalid IDs in this example produces 4174379265.

What do you get if you add up all of the invalid IDs using these new rules?
"""

import csv


def count_invalid_ids(csv_path: str):
    invalid_ids_counter = 0
    invalid_ids = []

    with open(csv_path, newline='') as file:
        csv_reader = csv.reader(file)
        all_lines = list(csv_reader)

        for line in all_lines:
            left, right = line[0].split('-')
            left, right = int(left), int(right)

            for n in range(left, right + 1):
                s = str(n)
                length = len(s)
                for i in range(1, length // 2 + 1):
                    if length % i == 0:
                        pattern = s[:i]
                        repetitions = length // i

                        if pattern * repetitions == s:
                            invalid_ids_counter += n
                            invalid_ids.append(n)
                            break  # very important

    return invalid_ids_counter, invalid_ids


if __name__ == '__main__':
    answer, invalid_ids = count_invalid_ids("day2/input.csv")
    print(f"List of incorrect ids: {invalid_ids}\n\nPassword is: {answer}")
    # Correct answer: 43872163557
    #
    # Remember previous note?
    # Seems like I've tried to solve second
    # puzzle before solving first one.
