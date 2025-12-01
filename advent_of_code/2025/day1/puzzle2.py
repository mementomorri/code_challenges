"""
--- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?
"""

import csv
from time import perf_counter


def count_zero_clicks(csv_path: str) -> int:
    """Return the number of times the dial points at 0 during the whole sequence."""

    pos = 50  # starting position
    zero_hits = 0
    with open(csv_path, newline='') as file:
        instructions = csv.reader(file)
        for line in instructions:
            line = line[0].strip()
            if not line:
                continue

            direction = line[0]  # 'L' or 'R'
            steps = int(line[1:])  # distance value
            step_sign = -1 if direction == 'L' else 1

            # Walk through each click
            for _ in range(steps):
                pos = (pos + step_sign) % 100
                if pos == 0:
                    zero_hits += 1

    return zero_hits


def count_zeroes(csv_path: str) -> int:
    """Counts the amount of time the safe dial is set to 0."""
    zeroes_counter = 0
    dial_pointer = 50

    with open(csv_path, newline='') as file:
        input_csv = csv.reader(file)

        for line in input_csv:
            if not line:
                continue
            move = line[0].strip()
            if not move:
                continue

            direction = move[0]
            steps = int(move[1:])
            step_sign = -1 if direction == 'L' else 1

            for _ in range(steps):
                dial_pointer = (dial_pointer + step_sign) % 100
                if dial_pointer == 0:
                    zeroes_counter += 1
    return zeroes_counter


if __name__ == '__main__':
    start_time = perf_counter()

    result = count_zeroes("day1/input.csv")
    print(f"The password to the door is: {result}")
    # in my case in was 5782

    end_time = perf_counter()
    print(f"It took {end_time - start_time} seconds to run.")
    # It took 0.018145906000427203 seconds to run.
    # A lot slower than first puzzle, but still fast.
    #
    # Initial guess was to keep using remainder of devide,
    # like with divmod(). But optimal solution is a lot simpler.
    # Just add step with sign (+-) and count every
    # time we hit zero, a lot simpler, than with modulo and
    # complex conditions.
