from rest_framework import serializers

from .models import Point


class PointSerializer(serializers.ModelSerializer):
    """Main point serializer."""

    result = serializers.ReadOnlyField(source="point.get_result")

    class Meta:
        """Serialization point options."""

        model = Point
        exclude = (
            'created_by', 'updated_by', 'active',"updated", "created", "id"
        )
