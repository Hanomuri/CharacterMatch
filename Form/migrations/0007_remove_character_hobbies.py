# Generated by Django 4.2.6 on 2023-10-12 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0006_alter_character_motto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='hobbies',
        ),
    ]
