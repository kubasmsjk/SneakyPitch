# Generated by Django 4.0.3 on 2022-04-19 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0009_alter_player_nazwisko'),
    ]

    operations = [
        migrations.CreateModel(
            name='Druzyna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=20, null=True)),
                ('stadion', models.CharField(max_length=20, null=True)),
                ('Trener', models.CharField(max_length=30, null=True)),
                ('data_zalozenia', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Drużyna',
                'verbose_name_plural': 'Drużyny',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='druzyna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GamePLAY.druzyna'),
        ),
    ]