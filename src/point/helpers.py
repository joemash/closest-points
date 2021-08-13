import ast
import heapq
import math


def calculate_distance(x1, y1, x2, y2):
     """calculates the distance between two points to each other."""
     return math.sqrt((x1 - y1)**2 + (x2 - y2)**2)


def get_points_distances(points):
    """Returns the distance between points. the time complexity is O(N2)"""
    temp = []
    for x in points:
        for y in points:
            distance = calculate_distance(x[0], y[0], x[1], y[1])
            # if 0.0 its the distance of the point to itself
            if distance == 0.0:
                continue
            temp.append([distance, (x[0], x[1]), (y[0], y[1]) ])
    return temp


def calculate_closest_pair_of_points(points):
    distance_and_points = get_points_distances(points)
    
    # Transform list into a heap, in-place, in O(len(n)) time.
    heapq.heapify(distance_and_points)

    output = []
    i = 1
    while i <= 1:
        # Pop the smallest item off the heap, maintaining the heap invariant in O(log(n)) times
        _, x, y = heapq.heappop(distance_and_points)
        output.append((x, y))
        i += 1
    return output


def convert_string_to_a_list_of_tuples(str):
    return list(ast.literal_eval(str))
