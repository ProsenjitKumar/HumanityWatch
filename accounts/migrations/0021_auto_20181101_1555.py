# Generated by Django 2.1.2 on 2018-11-01 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20181101_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_donation_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
