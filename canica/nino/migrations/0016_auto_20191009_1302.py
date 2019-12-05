# Generated by Django 2.0.13 on 2019-10-09 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nino', '0015_auto_20191009_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='motivo_ingreso',
            options={'verbose_name': 'Motivo de Ingreso', 'verbose_name_plural': 'Motivo_Ingresos'},
        ),
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
    ]