"""
--- Day 1: Secret Entrance ---

The Elves have good news and bad news.

The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.

The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!

To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

Collect stars by solving puzzles. Two puzzles will be made available on each day; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

"Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

The safe has a dial with only an arrow on it; around the dial are the numbers 0 through 99 in order. As you turn the dial, it makes a small click noise as it reaches each number.

The attached document (your puzzle input) contains a sequence of rotations, one per line, which tell you how to open the safe. A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

So, if the dial were pointing at 11, a rotation of R8 would cause the dial to point at 19. After that, a rotation of L19 would cause it to point at 0.

Because the dial is a circle, turning the dial left from 0 one click makes it point at 99. Similarly, turning the dial right from 99 one click makes it point at 0.

So, if the dial were pointing at 5, a rotation of L10 would cause it to point at 95. After that, a rotation of R5 could cause it to point at 0.

The dial starts by pointing at 50.

You could follow the instructions, but your recent required official North Pole secret entrance security training seminar taught you that the safe is actually a decoy. The actual password is the number of times the dial is left pointing at 0 after any rotation in the sequence.

For example, suppose the attached document contained the following rotations:

L68
L30
R48
L5
R60
L55
L1
L99
R14
L82

Following these rotations would cause the dial to move as follows:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32.

Because the dial points at 0 a total of three times during this process, the password in this example is 3.

Analyze the rotations in your attached document. What's the actual password to open the door?

"""

import csv
from time import perf_counter


def count_zeroes(csv_path: str) -> int:
    """Counts the amount of time the safe dial is set to 0.

    My initial thought was to use a modulo 99, but since 0
    is a number on the dial itself, the corret modulo was 100.

    That is another reminder: read examples very carefully and
    slowly, don't rush to the solution.
    """
    zoeroes_counter = 0
    dial_pointer = 50

    with open(csv_path, newline='') as file:
        input_csv = csv.reader(file)

        for line in input_csv:
            # print(f"Dial: {dial_pointer}, next move: {line[0]}")
            move = line[0]
            if not move:
                continue

            direction = move[0]
            step = int(move[1:])

            if direction == 'L':
                dial_pointer -= step
            elif direction == 'R':
                dial_pointer += step

            dial_pointer %= 100

            if dial_pointer == 0:
                # print("Found zero!")
                zoeroes_counter += 1

    return zoeroes_counter


if __name__ == '__main__':
    start_time = perf_counter()

    result = count_zeroes("day1/input.csv")
    print(f"The password to the door is: {result}")
    # in my case in was 962

    end_time = perf_counter()
    print(f"It took {end_time - start_time} seconds to run.")
    # It took 0.0013086670005577616 seconds to run.
