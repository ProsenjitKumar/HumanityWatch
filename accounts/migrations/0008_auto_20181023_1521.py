# Generated by Django 2.1.2 on 2018-10-23 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20181023_1520'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='level',
            new_name='blood',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='level',
            new_name='blood',
        ),
    ]
