# Generated by Django 3.2.19 on 2023-07-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_alter_profile_communities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studyplan',
            name='communities',
            field=models.ManyToManyField(blank=True, to='learning.Community'),
        ),
    ]
