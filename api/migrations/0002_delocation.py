# Generated by Django 5.1.3 on 2024-11-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='delocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('images', models.TextField(default='', max_length=1000000000000000000000000)),
                ('is_accident', models.BooleanField()),
                ('is_fire', models.BooleanField()),
            ],
        ),
    ]
