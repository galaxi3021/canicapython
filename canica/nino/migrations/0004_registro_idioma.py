# Generated by Django 2.2 on 2019-10-08 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0003_motivo_ingreso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Idioma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('estado', models.BooleanField(null=True)),
            ],
            options={
                'verbose_name': 'Registro_Idioma',
                'verbose_name_plural': 'Registro_Idiomas',
            },
        ),
    ]
