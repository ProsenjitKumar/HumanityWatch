# Generated by Django 2.1.2 on 2018-10-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20181023_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='blood',
            field=models.CharField(choices=[('a_positive', 'A+'), ('a_negative', 'A-'), ('b_positive', 'B+'), ('b_negative', 'B-'), ('ab_positive', 'AB+'), ('ab_negative', 'AB-'), ('o_positive', 'O+'), ('o_negative', 'O-')], max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='blood',
            field=models.CharField(choices=[('a_positive', 'A+'), ('a_negative', 'A-'), ('b_positive', 'B+'), ('b_negative', 'B-'), ('ab_positive', 'AB+'), ('ab_negative', 'AB-'), ('o_positive', 'O+'), ('o_negative', 'O-')], max_length=20),
        ),
    ]
