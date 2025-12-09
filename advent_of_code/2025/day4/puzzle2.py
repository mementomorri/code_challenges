"""
--- Part Two ---

Now, the Elves just need help accessing as much of the paper as they can.

Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?

Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.

Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?
"""

def is_valid_cell(x, y) -> bool:
    return True if ((x >= 0 and x < TOTAL_COLS) and (y >= 0 and y < TOTAL_ROWS)) else False

def format_shelf(lines: list[str]) -> list[list[int]]:
    result = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        line = line.replace("@", "1")
        line = line.replace(".", "0")

        result.append(list(map(int, line)))

    global TOTAL_ROWS
    global TOTAL_COLS
    TOTAL_ROWS = len(result)
    TOTAL_COLS = len(result[0])

    return result


def count_paper_rolls_to_be_retrieved(lines: list[str]) -> int:
    total_accessible = 0
    rows = format_shelf(lines)

    def helper(rows):
        result = 0
        for y, row in enumerate(rows):
            for x, col in enumerate(row):
                if not is_valid_cell(x, y):
                    break
                if col == 0:
                    continue

                sum_of_neighbours = 0
                for neighbour in NEIGHBOURS:
                    neighbour_y, neighbour_x = y + neighbour[1], x + neighbour[0]
                    if is_valid_cell(neighbour_x, neighbour_y):
                        sum_of_neighbours += rows[neighbour_y][neighbour_x]

                if sum_of_neighbours < 4:
                    rows[y][x] = 0
                    result+=1

        return result

    accessible = helper(rows)
    total_accessible += accessible
    while accessible > 0:
        accessible = helper(rows)
        total_accessible += accessible

    return total_accessible


def paper_rolls_that_can_be_accessed(input_file: str):
    accessable_paper_rolls = 0
    f = open(input_file)
    try:
        lines = f.readlines()
        accessable_paper_rolls = count_paper_rolls_to_be_retrieved(lines)
    finally:
        f.close()

    return accessable_paper_rolls


TOTAL_COLS = 0
TOTAL_ROWS = 0
NEIGHBOURS = (
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1),
)

if __name__ == '__main__':
    # print("Total accessable paper rolls is:", paper_rolls_that_can_be_accessed("day4/test_input.txt"))
    print("Total accessable paper rolls is:", paper_rolls_that_can_be_accessed("day4/input.txt"))
    # Total accessable paper rolls is: 9122
