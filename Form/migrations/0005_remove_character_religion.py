# Generated by Django 4.2.6 on 2023-10-10 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0004_alter_character_sexuals_orientations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='religion',
        ),
    ]