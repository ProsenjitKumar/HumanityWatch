# Generated by Django 2.1.2 on 2018-10-27 18:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20181025_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaluser',
            name='last_donation_date',
            field=models.DateField(blank=True, default=datetime.datetime(2018, 10, 27, 18, 31, 50, 392679, tzinfo=utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_donation_date',
            field=models.DateField(auto_now=True),
        ),
    ]
