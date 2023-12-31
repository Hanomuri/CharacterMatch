# Generated by Django 4.2.7 on 2023-11-22 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0015_alter_fq_neurodivergence_alter_fq_sexuality'),
    ]

    operations = [
        migrations.AddField(
            model_name='fq',
            name='confort',
            field=models.IntegerField(choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], default=0, verbose_name='Confort'),
        ),
        migrations.AddField(
            model_name='fq',
            name='country',
            field=models.CharField(choices=[['Reino Unido', 'Reino Unido'], ['Estados Unidos', 'Estados Unidos'], ['Argentina', 'Argentina'], ['Chile', 'Chile'], ['Australia', 'Australia'], ['Libano', 'Libano'], ['Sudáfrica', 'Sudáfrica'], ['Canadá', 'Canadá'], ['Italia', 'Italia'], ['Tanzania', 'Tanzania'], ['España', 'España'], ['Republica Dominicana', 'Republica Dominicana'], ['Puerto Rico', 'Puerto Rico'], ['otro', 'otro']], default='None', max_length=30, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='fq',
            name='disability',
            field=models.CharField(choices=[['SININFORMACION', 'SININFORMACION']], default='None', max_length=50, verbose_name='Discapacidad'),
        ),
        migrations.AddField(
            model_name='fq',
            name='ethnicity',
            field=models.CharField(choices=[['Blanca', 'Blanca'], ['Mestiza', 'Mestiza'], ['Afroamericana', 'Afroamericana'], ['Asiática', 'Asiática']], default='None', max_length=50, verbose_name='Etnia'),
        ),
        migrations.AddField(
            model_name='fq',
            name='identity',
            field=models.CharField(choices=[['Masculino', 'Masculino'], ['Femenino', 'Femenino'], ['Queer', 'Queer'], ['No binarie', 'No binarie'], ['Sin etiquetas', 'Sin etiquetas']], default='None', max_length=50, verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='fq',
            name='mbti',
            field=models.CharField(choices=[['ESTJ', 'ESTJ'], ['ISTJ', 'ISTJ'], ['ISFJ', 'ISFJ'], ['ESFJ', 'ESFJ'], ['INTP', 'INTP'], ['ENTP', 'ENTP'], ['INTJ', 'INTJ'], ['ENTJ', 'ENTJ'], ['ESFP', 'ESFP'], ['ISFP', 'ISFP'], ['ESTP', 'ESTP'], ['ISTP', 'ISTP'], ['ENFJ', 'ENFJ'], ['INFJ', 'INFJ'], ['INFP', 'INFP'], ['ENFP', 'ENFP']], default='None', max_length=10, verbose_name='Mbti'),
        ),
        migrations.AddField(
            model_name='fq',
            name='trans',
            field=models.CharField(choices=[['Yes', 'Yes'], ['No', 'No']], default='None', max_length=4, verbose_name='Trans'),
        ),
        migrations.AlterField(
            model_name='fq',
            name='neurodivergence',
            field=models.CharField(choices=[['Trastorno limite de personalidad', 'Trastorno limite de personalidad'], ['Autismo', 'Autismo'], ['TDAH', 'TDAH'], ['Dislexia', 'Dislexia'], ['Sindrome de Tourette', 'Sindrome de Tourette'], ['Otra', 'Otra']], default='None', max_length=50, verbose_name='neurodivergencia'),
        ),
        migrations.AlterField(
            model_name='fq',
            name='sexuality',
            field=models.CharField(choices=[('Gay', 'Gay'), ('Bisexual', 'Bisexual'), ('Lesbiana', 'Lesbiana'), ('Asexual', 'Asexual'), ('Arromantico', 'Arromantico'), ('Pansexual', 'Pansexual'), ('Sin etiqueta', 'Sin etiqueta'), ('Otra', 'Otra')], default='None', max_length=50, verbose_name='sexualidad'),
        ),
    ]
