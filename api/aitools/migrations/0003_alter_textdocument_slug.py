# Generated by Django 4.2 on 2023-06-11 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aitools', '0002_textdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textdocument',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
