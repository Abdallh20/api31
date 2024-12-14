# Generated by Django 5.1.3 on 2024-12-14 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_delocation"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="servo_angle",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="location",
            name="target_angle",
            field=models.FloatField(default=0),
        ),
    ]