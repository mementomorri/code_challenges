"""
--- Part Two ---

The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.

So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh. An ingredient ID is still considered fresh if it is in any range.

Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18

The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example, the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.

Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?
"""



def count_fresh_ingredients(fresh_ranges: list[list[int]]) -> int:
    merged_ranges = [fresh_ranges[0]]
    last_merged_end = fresh_ranges[0][1]

    for curr_range in fresh_ranges:
        if curr_range[0] <= last_merged_end:
            if last_merged_end < curr_range[1]:
                merged_ranges[-1][1] = curr_range[1]
        else:
            merged_ranges.append(curr_range)

        last_merged_end = max(curr_range[1], last_merged_end)

    total_avail_ingredients = 0
    for r in merged_ranges:
        total_avail_ingredients += (r[1] + 1) - r[0]

    return total_avail_ingredients


def process_id_ranges(input_path: str) -> int:
    fresh_ranges = []

    try:
        f = open(input_path)
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                break

            range_split = line.split("-")
            fresh_ranges.append([int(range_split[0]), int(range_split[1])])

    except FileNotFoundError:
        return 0

    finally:
        f.close()

    fresh_ranges.sort(key=lambda r: r[0])

    return count_fresh_ingredients(fresh_ranges)


if __name__ == "__main__":
    print(f"Total sum of fresh available ingredients ids are: {process_id_ranges('day5/input.txt')}")
    # print(f"Total sum of fresh available ingredients ids are: {process_id_ranges('day5/test_input.txt')}")
    # Don't use brute force!
    # Total sum of fresh available ingredients ids are: 343143696885053
