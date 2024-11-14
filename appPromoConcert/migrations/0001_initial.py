# Generated by Django 5.1.2 on 2024-11-14 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('ubicacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PromotorMusical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('pais_origen', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interprete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
                ('pais_origen', models.CharField(max_length=100)),
                ('festivales', models.ManyToManyField(related_name='interpretes', to='appPromoConcert.festival')),
            ],
        ),
        migrations.AddField(
            model_name='festival',
            name='promotor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='festivales', to='appPromoConcert.promotormusical'),
        ),
    ]