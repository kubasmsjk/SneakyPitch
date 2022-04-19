# Generated by Django 4.0.3 on 2022-04-19 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0002_rename_zespol_druzyna_alter_druzyna_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zawodnik',
            name='druzyna',
        ),
        migrations.AddField(
            model_name='druzyna',
            name='stadion',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='druzyna',
            name='zawodnik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GamePLAY.zawodnik'),
        ),
        migrations.AddField(
            model_name='zawodnik',
            name='narodowosc',
            field=models.TextField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='zawodnik',
            name='imie',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='zawodnik',
            name='nazwisko',
            field=models.TextField(max_length=30),
        ),
    ]