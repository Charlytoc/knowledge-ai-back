# Generated by Django 3.2.19 on 2023-07-08 17:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0016_auto_20230708_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 7, 17, 55, 41, 85533, tzinfo=utc)),
        ),
    ]
