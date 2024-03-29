# Generated by Django 2.0.13 on 2019-10-09 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0022_auto_20191009_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area_medica',
            name='nivel_nutricion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nino.Nivel_Nutricion'),
        ),
        migrations.AlterField(
            model_name='nino',
            name='motivo_ingreso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='nino.Motivo_Ingreso'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='fecha_publicacion',
            field=models.DateField(),
        ),
    ]
