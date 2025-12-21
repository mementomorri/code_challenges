from collections import namedtuple


# Represent a point in 2D space
Point = namedtuple('Point', 'x y')


class Segment:
    # Represent a line segment in 2D space
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start.x},{self.start.y} : {self.end.x},{self.end.y}]"

    def start_segment(self):
        return self.start

    def end_segment(self):
        return self.end


def make_segment(start: Point, end: Point) -> Segment:
    # Constructor for line segment
    return Segment(start, end)


def midpoint_segment(s: Segment) -> Point:
    # Calculate the midpoint of a line segment
    return Point((s.end.x + s.start.x) // 2, (s.end.y + s.start.y) // 2)


if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(10, 3)
    segmant1 = make_segment(p1, p2)
    print(segmant1)
    print(midpoint_segment(segmant1))

    p3 = Point(4, 1)
    p4 = Point(8, 2)
    s2 = make_segment(p3, p4)
    print(s2)
    print(midpoint_segment(s2))
