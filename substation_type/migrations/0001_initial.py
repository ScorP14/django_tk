# Generated by Django 5.0.3 on 2024-04-29 04:39

import helper.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubstationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Тип подстанции',
                'verbose_name_plural': 'Типы подстанций',
            },
            bases=(helper.models.AddColumQuerySetForModel, models.Model),
        ),
    ]
