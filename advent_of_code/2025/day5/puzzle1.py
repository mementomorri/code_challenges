"""
--- Day 5: Cafeteria ---

As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.

You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate.

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.

The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled. When you ask how it works, they give you a copy of their database (your puzzle input).

The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

    Ingredient ID 1 is spoiled because it does not fall into any range.
    Ingredient ID 5 is fresh because it falls into range 3-5.
    Ingredient ID 8 is spoiled.
    Ingredient ID 11 is fresh because it falls into range 10-14.
    Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
    Ingredient ID 32 is spoiled.

So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?
"""

FRESH_RANGES = []
INGREDIENTS = []
SECTION_FLAG = False


def process_ingredient(line: str) -> None:
    global INGREDIENTS
    INGREDIENTS.append(int(line))


def process_range(line: str) -> None:
    range_split = line.split("-")

    global FRESH_RANGES
    FRESH_RANGES.append((int(range_split[0]), int(range_split[1])))
    return


def process_line(line: str) -> None:
    global SECTION_FLAG

    if SECTION_FLAG:
        process_ingredient(line)
        return

    if line.strip() == "":
        SECTION_FLAG = True
        return

    process_range(line)
    return


def count_fresh_ingredients() -> int:
    fresh = 0

    for ingredient in INGREDIENTS:
        for current_range in FRESH_RANGES:
            if ingredient >= current_range[0] and ingredient <= current_range[1]:
                fresh += 1
                break

    return fresh


def process_id_ranges(input_path: str) -> int:
    try:
        f = open(input_path)
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            process_line(line)
    except FileNotFoundError:
        return 0
    finally:
        f.close()

    return count_fresh_ingredients()


if __name__ == "__main__":
    print(f"Total sum of fresh available ingredients ids are: {process_id_ranges('day5/input.txt')}")
    # print(f"Total sum of fresh available ingredients ids are: {process_id_ranges('day5/test_input.txt')}")
