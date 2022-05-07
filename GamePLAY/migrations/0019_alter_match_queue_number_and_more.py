# Generated by Django 4.0.4 on 2022-04-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0018_rename_statistic_statisticofplayer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='queue_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='player',
            name='number_of_goals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statisticofplayer',
            name='number_of_assists',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statisticofplayer',
            name='number_of_fouls',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statisticofplayer',
            name='number_of_goals',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='statisticofplayer',
            name='number_of_passes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]