from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Point
from .serializers import PointSerializer

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

        When successful it returns the result of the closest point
        and HTTP status code HTTP_201_CREATED
        
        {'result': [(1, 1), (2,3)], 'submission': '(2,3), (1,1), (5, 4)'}

        """
        points_create_ser = PointSerializer(
            data=request.data, context={"request": request}
        )
        points_create_ser.is_valid(raise_exception=True)
        point_ser_data = points_create_ser.validated_data
        submitted_points = point_ser_data.get("submission")
        point = points_create_ser.save()
        serializer = self.get_serializer(point)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
