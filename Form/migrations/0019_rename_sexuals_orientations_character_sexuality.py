# Generated by Django 4.2.7 on 2023-11-24 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0018_fq_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='sexuals_orientations',
            new_name='sexuality',
        ),
    ]
