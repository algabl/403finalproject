# Generated by Django 4.1.2 on 2022-12-11 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('duckdatabase', '0006_alter_duck_beak_color_alter_duck_body_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='duck',
            name='duck_age',
        ),
    ]