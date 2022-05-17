# Generated by Django 4.0.4 on 2022-05-15 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0032_rename_visiting_team_match_away_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='GamePLAY.team'),
        ),
    ]