import pytest
from django.core.exceptions import ValidationError

from sessions.models import StudySession


@pytest.mark.django_db
def test_session_stores_topic_and_duration():
    session = StudySession.objects.create(topic="Mutation Testing", duration_minutes=60)
    saved = StudySession.objects.get(pk=session.pk)
    assert saved.topic == "Mutation Testing"
    assert saved.duration_minutes == 60


# HW1 Part 4:
# Add a test showing that StudySession correctly stores the new "subject"
# information that you add in Part 3.
@pytest.mark.django_db
def test_study_session_creation_with_subject():
    """Verify that a study session correctly stores subject information."""
    session = StudySession.objects.create(
        topic="Gamma Radiation",
        subject="Physics",
        duration_minutes=75,
    )
    assert session.topic == "Gamma Radiation"
    assert session.subject == "Physics"
    


# HW1 Part 4:
# Add a test showing that a negative duration is rejected.
# Beginner hint:
# - construct a StudySession with a negative duration
# - call full_clean()
# - pytest.raises(ValidationError) may be useful
@pytest.mark.django_db
def test_study_session_rejects_negative_duration():
    """Verify that a study session cannot be saved with a negative duration."""
    session = StudySession(
        topic="Invalid Session",
        subject="Testing",
        duration_minutes=-15,
    )
    with pytest.raises(ValidationError):
        session.full_clean()