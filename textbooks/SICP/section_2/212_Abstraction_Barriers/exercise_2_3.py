from collections import namedtuple


# Represent a point in 2D space
Point = namedtuple('Point', 'x y')


class Rectangle:
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def __str__(self):
        return f"[{self.p1}, {self.p2}, {self.p3}, {self.p4}]"


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


def perimeter(start: Point, end: Point) -> int:
    return 2 * abs(end.x - start.x) + 2 * abs(end.y - start.y)


def area(start: Point, end: Point) -> int:
    return abs(start.x - end.x) * abs(start.y - end.y)


if __name__ == "__main__":
    p1 = Point(1, 1)
    p2 = Point(10, 3)
    segmant1 = make_segment(p1, p2)
    print("First segment:", segmant1)
    print("Midpoint:", midpoint_segment(segmant1))

    p3 = Point(4, 1)
    p4 = Point(8, 2)
    segmant2 = make_segment(p3, p4)
    print("First segment:", segmant2)
    print("Midpoint:", midpoint_segment(segmant2))

    print("Perimeter of first segment:", perimeter(segmant1.start, segmant1.end))
    print("Area of first segment:", area(segmant1.start, segmant1.end))

    rect = Rectangle(Point(1, 1), Point(11, 1), Point(1, 11), Point(11, 11))

    print("Rectangle:", rect)

    print("Perimeter of the rectangle:", perimeter(rect.p1, rect.p4))
    print("Area of the rectangle:", area(rect.p1, rect.p4))
