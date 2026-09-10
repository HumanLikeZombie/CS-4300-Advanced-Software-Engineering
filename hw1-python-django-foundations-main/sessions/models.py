from django.core.exceptions import ValidationError
from django.db import models


class StudySession(models.Model):
    """A single study session. HW1 Part 3 asks students to add a subject field."""

    topic = models.CharField(max_length=150)
    subject = models.CharField(max_length=200, default="")
    duration_minutes = models.IntegerField()
    completed_on = models.DateField(auto_now_add=True)

    def clean(self):
        """HW1 Part 4: add validation so negative duration is rejected."""
        # (HW1 Part 4): add validation for negative duration.
        super().clean()
        if self.duration_minutes is not None and self.duration_minutes < 0:
            raise ValidationError(
                {"duration_minutes": "Duration cannot be a negative value."}
            )

    def __str__(self):
        return f"{self.topic} ({self.duration_minutes} min)"
