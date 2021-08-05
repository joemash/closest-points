import uuid

from django.db import models
from django.utils import timezone

from .helpers import (
    calculate_closest_pair_of_points,
    convert_string_to_a_list_of_tuples,
)


class AbstractBase(models.Model):
    """Base class for models"""

    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    created_by = models.UUIDField(null=True, blank=True)
    updated = models.DateTimeField(default=timezone.now)
    updated_by = models.UUIDField(null=True, blank=True)


class Point(AbstractBase):
    """Points stores point submissions."""

    submission = models.CharField(max_length=250)

    def get_result(self):
        """computes the result from the stored submission."""
        points = convert_string_to_a_list_of_tuples(self.submission)
        return calculate_closest_pair_of_points(points)
