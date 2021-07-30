from rest_framework import serializers

from .models import Point


class PointSerializer(serializers.ModelSerializer):
    """Main point serializer."""

    result = serializers.ReadOnlyField(source="point.compute_submission_result")

    class Meta:
        """Serialization options."""

        model = Point
        fields = "__all__"
