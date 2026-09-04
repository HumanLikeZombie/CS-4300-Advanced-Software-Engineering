# Generated for HW2 starter code.
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dragon",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(default="Puff", max_length=50)),
                ("hunger", models.IntegerField(default=5)),
                ("energy", models.IntegerField(default=5)),
                ("mood", models.CharField(default="content", max_length=20)),
            ],
        ),
    ]
