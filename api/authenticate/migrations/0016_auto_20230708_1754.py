# Generated by Django 3.2.19 on 2023-07-08 17:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0015_alter_token_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providercredentials',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2023, 9, 6)),
        ),
        migrations.AlterField(
            model_name='token',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 7, 17, 53, 59, 173952, tzinfo=utc)),
        ),
    ]
