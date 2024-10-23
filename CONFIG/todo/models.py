from typing import Any
from django.db import models


class Task(models.Model):
    title = models.CharField(
        max_length=255, null=True, blank=False
    )
    description = models.TextField(
        null=True, blank=True
    )
    is_completed = models.BooleanField(
        default=False
    )
    due_date = models.DateField(
        null=False, blank=False,
    )
    created_date = models.DateField(
        auto_created=True
    )

    def __str__(self):
        return self.title
