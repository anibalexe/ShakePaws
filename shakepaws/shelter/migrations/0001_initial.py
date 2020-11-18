# Generated by Django 3.1.3 on 2020-11-18 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificación')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('lifestage', models.CharField(max_length=50, verbose_name='Etapa de vida')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('image', models.ImageField(upload_to='Animales', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animales',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('sponsor_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Identificación')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('cost', models.IntegerField(verbose_name='Costo')),
            ],
            options={
                'verbose_name': 'Apadrinamiento',
                'verbose_name_plural': 'Apadrinamientos',
            },
        ),
        migrations.CreateModel(
            name='Animal_sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.animal')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelter.sponsor')),
            ],
        ),
    ]
