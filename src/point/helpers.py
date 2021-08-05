import ast
import heapq
import math


def compute_distance_between_points(x, y):
    """
    Calculate the distance between two points from origin (0,0).
    """
    return math.sqrt((x ** 2 + y ** 2))


def calculate_closest_pair_of_points(points, k=1):
    """
    Given a list of points and the number of points to return
    compute distance to the closest point to the origin.

    We transform the items into a heap this ensures
    we keep a min heap of size len(points).

    Runtime:

    Popping an item from a heap of size len(points) takes O(log(N)) time.

    And we do this for each item points.

    So runtime is O(k * log(N)) where k is the number of pair points to return.

    Space: O(k) for our heap.
    """
    # compute the distances of the points from the origin
    temp = []
    for x, y in points:
        distance = compute_distance_between_points(x, y)
        temp.append([distance, x, y])
    # Transform list into a heap, in-place, in O(len(n)) time.
    heapq.heapify(temp)

    output = []
    i = 1
    while i <= k:
        # Pop the smallest item off the heap, maintaining the heap invariant in O(log(n)) times
        _, x, y = heapq.heappop(temp)
        output.append((x, y))
        i += 1
    return output


def convert_string_to_a_list_of_tuples(str):
    return list(ast.literal_eval(str))
