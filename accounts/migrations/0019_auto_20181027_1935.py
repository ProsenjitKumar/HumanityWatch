# Generated by Django 2.1.2 on 2018-10-27 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20181027_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='last_donation_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_donation_date',
            field=models.DateField(),
        ),
    ]
