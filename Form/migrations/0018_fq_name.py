# Generated by Django 4.2.7 on 2023-11-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0017_alter_fq_confort_alter_fq_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fq',
            name='name',
            field=models.CharField(default='None', max_length=50),
        ),
    ]