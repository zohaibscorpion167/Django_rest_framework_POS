# Generated by Django 3.1.5 on 2021-01-13 07:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('POS_APP', '0005_remove_stock_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date_added',
            field=models.DateField(default=datetime.date(2021, 1, 13)),
        ),
    ]
