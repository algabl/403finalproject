# Generated by Django 4.1.2 on 2022-12-03 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('duckdatabase', '0002_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duck',
            name='owner_first_name',
        ),
        migrations.RemoveField(
            model_name='duck',
            name='owner_last_name',
        ),
        migrations.AddField(
            model_name='duck',
            name='Owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='duckdatabase.owner'),
        ),
    ]