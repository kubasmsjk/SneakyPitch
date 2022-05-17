# Generated by Django 4.0.4 on 2022-05-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0031_player_number_of_goals'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='visiting_team',
            new_name='away_team',
        ),
        migrations.RemoveField(
            model_name='match',
            name='match_score',
        ),
        migrations.AddField(
            model_name='match',
            name='away_team_goals',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_goals',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]