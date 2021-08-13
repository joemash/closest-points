from django.urls import reverse


def test_compute_points(logged_in_client, token):
    """Test compute points with valid data."""
    payload = {
        "submission": "(2,3), (1,1), (5, 4)",
    }
    url = reverse("point-compute-closest-points")
    headers = {"Authorization": "JWT " + token}
    response = logged_in_client.post(url, payload, headers=headers)
    assert response.data.get("submission") == '(2,3), (1,1), (5, 4)'
    assert response.data.get("result") == [((1, 1), (2, 3))]
