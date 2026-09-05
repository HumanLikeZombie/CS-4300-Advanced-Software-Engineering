from django import forms
from .models import StudySession


class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        # HW1 Part 3: after adding subject to StudySession, add it here too.
        fields = ["topic", "subject", "duration_minutes"]
