"""
--- Day 4: Printing Department ---

You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).

Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.

"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.

The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.

For example:

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

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.

In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

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

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
"""

def is_valid_cell(x, y) -> bool:
    return True if x >= 0 and x < TOTAL_COLS and y >= 0 and y < TOTAL_ROWS else False

def format_shelf(lines: list[str]) -> list[list[int]]:
    result = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        line = line.replace("@", "1")
        line = line.replace(".", "0")

        result.append(list(map(int, line)))

    return result


def count_paper_rolls_to_be_retrieved(lines: list[str]) -> int:
    accessible = 0
    rows = format_shelf(lines)

    for x, row in enumerate(rows):
        for y, col in enumerate(row):
            if not is_valid_cell(x, y):
                break
            if col == 0:
                continue

            sum_of_neighbours = 0
            for neighbour in NEIGHBOURS:
                neighbour_x, neighbour_y = x + neighbour[0], y + neighbour[1]
                print(neighbour_x, neighbour_y)
                if is_valid_cell(neighbour_x, neighbour_y):
                    sum_of_neighbours += rows[neighbour_x][neighbour_y]

            if sum_of_neighbours < 4:
                accessible+=1

    return 1


def paper_rolls_that_can_be_accessed(input_file: str):
    accessable_paper_rolls = 0
    f = open(input_file)
    try:
        lines = f.readlines()
        global TOTAL_ROWS
        global TOTAL_COLS
        TOTAL_ROWS = len(lines) - 1
        TOTAL_COLS = len(lines[0]) - 1
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
    print("Total accessable paper rolls is:", paper_rolls_that_can_be_accessed("day4/test_input.txt"))
    # print("Total accessable paper rolls is:", paper_rolls_that_can_be_accessed("day4/input.txt"))
