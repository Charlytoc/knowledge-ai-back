# Generated by Django 3.2.19 on 2023-07-08 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_topic_objective'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='objectives',
            new_name='objective',
        ),
    ]