<<<<<<< HEAD
<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-04-26 20:27
=======
# Generated by Django 4.0.4 on 2022-05-04 15:56
>>>>>>> kwachu
=======
# Generated by Django 4.0.4 on 2022-05-04 20:11
>>>>>>> marcin

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0020_rename_statisticofplayer_playerstatistic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='league',
            name='team1',
        ),
        migrations.RemoveField(
            model_name='league',
            name='team2',
        ),
        migrations.RemoveField(
            model_name='league',
            name='team3',
        ),
        migrations.RemoveField(
            model_name='league',
            name='team4',
        ),
        migrations.RemoveField(
            model_name='league',
            name='team5',
        ),
        migrations.RemoveField(
            model_name='league',
            name='team6',
        ),
        migrations.RemoveField(
            model_name='league',
            name='team7',
        ),
        migrations.RemoveField(
            model_name='league',
            name='team8',
        ),
        migrations.AddField(
            model_name='team',
            name='league_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='GamePLAY.league'),
        ),
        migrations.AlterField(
            model_name='league',
            name='league_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
