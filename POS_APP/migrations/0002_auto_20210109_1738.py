# Generated by Django 3.1.5 on 2021-01-09 12:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='order_date',
            field=models.DateField(default=datetime.date(2021, 1, 9)),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='order_time',
            field=models.TimeField(default=datetime.datetime(2021, 1, 9, 17, 38, 37, 4694)),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date_added',
            field=models.DateField(default=datetime.date(2021, 1, 9)),
        ),
    ]