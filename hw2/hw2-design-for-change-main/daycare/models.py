from django.db import models


class Dragon(models.Model):
    name = models.CharField(max_length=50, default="Puff")
    hunger = models.IntegerField(default=5)
    energy = models.IntegerField(default=5)
    mood = models.CharField(max_length=20, default="content")

    def feed(self):
        # This works, but the care rules have become tangled together.
        if self.hunger >= 8:
            self.hunger -= 3
            self.energy += 1
            self.mood = "relieved"
        elif self.hunger >= 5:
            self.hunger -= 2
            self.mood = "happy"
        else:
            self.hunger -= 1
            self.mood = "sleepy"

        if self.hunger < 0:
            self.hunger = 0
        if self.energy > 10:
            self.energy = 10

    def status_message(self):
        if self.hunger >= 8:
            return f"{self.name} is very hungry!"
        if self.hunger >= 6:
            return f"{self.name} could use a snack."
        if self.energy <= 2:
            return f"{self.name} is exhausted."
        if self.mood == "happy":
            return f"{self.name} is happy."
        if self.mood == "relieved":
            return f"{self.name} looks relieved."
        if self.mood == "sleepy":
            return f"{self.name} is sleepy."
        return f"{self.name} is doing fine."

    def needs_attention(self):
        return self.hunger >= 8 or self.energy <= 2 or self.mood == "sleepy"

    def __str__(self):
        return self.name
