from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Point
from .serializers import PointSerializer
from .helpers import (
    calculate_closest_pair_of_points,
    convert_string_to_a_list_of_tuples,
)


class PointViewSet(ModelViewSet):
    """Point viewset."""

    queryset = Point.objects.all()
    serializer_class = PointSerializer

    @action(detail=False, methods=["post"])
    def compute_closest_points(self, request, pk=None):
        """
        Endpoint to compute a closests points.

        It expects the following payload:
        {
            "submission": "(2,3), (1,1), (5, 4)"
        }

        When successful it returns the closest 2 points
        and HTTP status code HTTP_201_CREATED
        """
        request_data = request.data
        print(request_data)
        points_create_ser = PointSerializer(
            data=request_data, context={"request": request}
        )
        points_create_ser.is_valid(raise_exception=True)
        point_ser_data = points_create_ser.validated_data
        submitted_points = point_ser_data.get("submission")
        # persist the submitted points in the database
        points_create_ser.save()
        # compute the closest points
        points = convert_string_to_a_list_of_tuples(submitted_points)
        data = calculate_closest_pair_of_points(points)
        # response_payload = {"closest_points": data}
        return Response(data=data, status=status.HTTP_201_CREATED)
