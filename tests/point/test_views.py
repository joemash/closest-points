import json

from django.urls import reverse


def test_compute_points(logged_in_client, token):
    """Test compute points with valid data."""
    payload = {
        "submission": "(2,3), (1,1), (5, 4)",
    }
    url = reverse("point-compute-closest-points")
    headers = {"Authorization": "JWT " + token}
    response = logged_in_client.post(url, payload, headers=headers)
    returned_payload = json.loads(response.content)
    assert returned_payload == [[2, 3], [1, 1]]

    # get the submitted points from the API
    url = reverse("point-list")
    headers = {"Authorization": "JWT " + token}
    response = logged_in_client.get(url, payload, headers=headers)
    returned_payload = json.loads(response.content)
    assert returned_payload.get("results")[0]["submission"] == "(2,3), (1,1), (5, 4)"
    assert returned_payload.get("results")[0]["result"] == [[2, 3], [1, 1]]
