import sys
import ast


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "[x={},y={}]".format(self.x, self.y)


def calculate_distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


def calculate_closest_pair_of_points(point_tuples):
    points = [Point(x, y) for (x, y) in point_tuples]
    minimum_distance, minimum_distance_points = sys.maxsize, None
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            dist = calculate_distance(points[i], points[j])
            if dist < minimum_distance:
                minimum_distance = dist
                minimum_distance_points = (
                    (points[i].x, points[i].y),
                    (points[j].x, points[j].y),
                )

    return minimum_distance_points


def convert_string_to_a_list_of_tuples(str):
    return list(ast.literal_eval(str))
