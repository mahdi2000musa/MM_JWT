# Generated by Django 4.2 on 2024-07-19 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm_jwt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtoken',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 19, 12, 32, 57, 675273, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='customtoken',
            name='value',
            field=models.CharField(default='', max_length=255),
        ),
    ]
