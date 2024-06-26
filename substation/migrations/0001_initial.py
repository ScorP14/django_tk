# Generated by Django 5.0.3 on 2024-04-29 04:39

import django.db.models.deletion
import helper.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_initial'),
        ('substation_type', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Substation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='номер')),
                ('slug', models.SlugField(blank=True, verbose_name='url')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='city.city')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='substation_type.substationtype')),
            ],
            options={
                'verbose_name': 'Подстанция',
                'verbose_name_plural': 'Подстанции',
                'ordering': ['city', 'view', 'number'],
            },
            bases=(helper.models.AddColumQuerySetForModel, models.Model),
        ),
    ]
