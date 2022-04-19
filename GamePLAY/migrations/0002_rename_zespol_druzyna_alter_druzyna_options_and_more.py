# Generated by Django 4.0.3 on 2022-04-19 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GamePLAY', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Zespol',
            new_name='Druzyna',
        ),
        migrations.AlterModelOptions(
            name='druzyna',
            options={'verbose_name': 'Druzyna', 'verbose_name_plural': 'Druzyny'},
        ),
        migrations.AlterModelOptions(
            name='zawodnik',
            options={'verbose_name': 'Zawodnik', 'verbose_name_plural': 'Zawodnicy'},
        ),
        migrations.AddField(
            model_name='zawodnik',
            name='druzyna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GamePLAY.druzyna'),
        ),
    ]