# Generated by Django 3.2.19 on 2023-07-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0015_studyplan_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
