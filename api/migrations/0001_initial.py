# Generated by Django 5.1.3 on 2024-11-06 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('images', models.CharField(default='', max_length=10000)),
                ('is_accident', models.BooleanField()),
                ('is_fire', models.BooleanField()),
            ],
        ),
    ]
