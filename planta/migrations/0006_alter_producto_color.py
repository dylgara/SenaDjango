# Generated by Django 4.0.6 on 2022-08-02 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0005_alter_producto_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='color',
            field=models.CharField(choices=[('r', 'ROJO'), ('v', 'VERDE'), ('a', 'AZUL')], default='r', max_length=100),
        ),
    ]
