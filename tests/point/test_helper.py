from src.point.helpers import calculate_closest_pair_of_points


def test_compute_closest_points():
    assert calculate_closest_pair_of_points(
        [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
    ) == ((1, 1), (-1, -1))
