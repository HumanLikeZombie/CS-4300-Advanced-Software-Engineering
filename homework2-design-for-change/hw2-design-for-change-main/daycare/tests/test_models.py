import pytest

from daycare.models import Dragon


@pytest.mark.django_db
def test_feed_reduces_moderate_hunger():
    puff = Dragon.objects.create(hunger=6, energy=5, mood="content")

    puff.feed()

    assert puff.hunger == 4
    assert puff.mood == "happy"


@pytest.mark.django_db
def test_feed_reduces_severe_hunger_more_aggressively():
    puff = Dragon.objects.create(hunger=9, energy=5, mood="content")

    puff.feed()

    assert puff.hunger == 6
    assert puff.energy == 6
    assert puff.mood == "relieved"


@pytest.mark.django_db
def test_feed_never_makes_hunger_negative():
    puff = Dragon.objects.create(hunger=0, energy=5, mood="content")

    puff.feed()

    assert puff.hunger == 0


@pytest.mark.django_db
def test_status_message_for_very_hungry_dragon():
    puff = Dragon.objects.create(name="Puff", hunger=8, energy=5, mood="content")

    assert puff.status_message() == "Puff is very hungry!"
