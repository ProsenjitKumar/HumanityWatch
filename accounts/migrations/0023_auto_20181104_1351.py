# Generated by Django 2.1.3 on 2018-11-04 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20181104_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_donation_date',
            field=models.DateField(blank=True, null=True, unique=True),
        ),
    ]
