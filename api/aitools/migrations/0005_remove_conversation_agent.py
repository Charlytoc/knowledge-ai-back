# Generated by Django 4.2 on 2023-06-14 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aitools', '0004_alter_engine_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='agent',
        ),
    ]
