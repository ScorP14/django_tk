# Generated by Django 5.0.3 on 2024-03-18 05:33

import django.db.models.deletion
import substation.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
            },
            bases=(substation.models.AddColumQuerySetForModel, models.Model),
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('title', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип подстанции',
                'verbose_name_plural': 'Типы подстанций',
            },
            bases=(substation.models.AddColumQuerySetForModel, models.Model),
        ),
        migrations.CreateModel(
            name='Substation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='номер')),
                ('slug', models.SlugField(blank=True, verbose_name='url')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='substation.city')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='substation.view')),
            ],
            options={
                'verbose_name': 'Подстанция',
                'verbose_name_plural': 'Подстанции',
                'ordering': ['city', 'view', 'number'],
            },
            bases=(substation.models.AddColumQuerySetForModel, models.Model),
        ),
    ]