# Generated by Django 5.1.2 on 2024-11-16 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPromoConcert', '0002_reseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseña',
            name='calificacion',
            field=models.IntegerField(default=0),
        ),
    ]
