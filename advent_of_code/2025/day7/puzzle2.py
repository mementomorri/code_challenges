"""
--- Part Two ---

With your analysis of the manifold complete, you begin fixing the teleporter. However, as you open the side of the teleporter to replace the broken manifold, you are surprised to discover that it isn't a classical tachyon manifold - it's a quantum tachyon manifold.

With a quantum tachyon manifold, only a single tachyon particle is sent through the manifold. A tachyon particle takes both the left and right path of each splitter encountered.

Since this is impossible, the manual recommends the many-worlds interpretation of quantum tachyon splitting: each time a particle reaches a splitter, it's actually time itself which splits. In one timeline, the particle went left, and in the other timeline, the particle went right.

To fix the manifold, what you really need to know is the number of timelines active after a single particle completes all of its possible journeys through the manifold.

In the above example, there are many timelines. For instance, there's the timeline where the particle always went left:

.......S.......
.......|.......
......|^.......
......|........
.....|^.^......
.....|.........
....|^.^.^.....
....|..........
...|^.^...^....
...|...........
..|^.^...^.^...
..|............
.|^...^.....^..
.|.............
|^.^.^.^.^...^.
|..............

Or, there's the timeline where the particle alternated going left and right at each splitter:

.......S.......
.......|.......
......|^.......
......|........
......^|^......
.......|.......
.....^|^.^.....
......|........
....^.^|..^....
.......|.......
...^.^.|.^.^...
.......|.......
..^...^|....^..
.......|.......
.^.^.^|^.^...^.
......|........

Or, there's the timeline where the particle ends up at the same point as the alternating timeline, but takes a totally different path to get there:

.......S.......
.......|.......
......|^.......
......|........
.....|^.^......
.....|.........
....|^.^.^.....
....|..........
....^|^...^....
.....|.........
...^.^|..^.^...
......|........
..^..|^.....^..
.....|.........
.^.^.^|^.^...^.
......|........

In this example, in total, the particle ends up on 40 different timelines.

Apply the many-worlds interpretation of quantum tachyon splitting to your manifold diagram. In total, how many different timelines would a single tachyon particle end up on?
"""

#!/usr/bin/env python3
from functools import cache
import sys

SPLITTER = '^'
SPACE = '.'
ENTER = 'S'


def read_grid(path):
    with open(path, encoding='utf-8') as f:
        raw = [line.rstrip("\n") for line in f.readlines()]
    width = max(len(r) for r in raw)
    grid = [list(r.ljust(width, ' ')) for r in raw]
    return grid


def find_start(grid):
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == ENTER:
                return x, y
    raise ValueError("No start 'S' found")


def in_bounds(x, y, W, H):
    return 0 <= x < W and 0 <= y < H


def make_successor_fn(grid):
    H = len(grid)
    W = len(grid[0]) if H > 0 else 0

    def successors(node):
        x, y = node
        ny = y + 1
        if ny >= H:
            return []
        ch = grid[ny][x]
        if ch == SPLITTER:
            succs = []
            for nx in (x - 1, x + 1):
                if in_bounds(nx, ny, W, H):
                    succs.append((nx, ny))
            return succs
        if ch != ' ':
            return [(x, ny)]
        return []

    return successors


def count_timelines(grid):
    sx, sy = find_start(grid)
    successors = make_successor_fn(grid)

    @cache
    def dp(node):
        succs = successors(node)
        if not succs:
            return 1
        total = 0
        for s in succs:
            total += dp(s)
        return total

    return dp((sx, sy))


def main(path):
    grid = read_grid(path)
    total = count_timelines(grid)
    print("Tachyon beam will split:", total, "times")
    # Tachyon beam will split: 48989920237096 times


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 puzzle2.py <input-file>")
        sys.exit(1)
    main(sys.argv[1])
