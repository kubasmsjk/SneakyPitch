# Generated by Django 4.0.4 on 2022-06-11 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0003_alter_playerstatistic_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerstatistic',
            name='match',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='GamePLAY.match'),
        ),
    ]
