# Generated by Django 4.0.4 on 2022-06-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0004_playerstatistic_match'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='number_of_goals_diffrence',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teamstatistic',
            name='number_of_goals_diffrence',
            field=models.IntegerField(default=0),
        ),
    ]