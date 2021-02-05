# Generated by Django 3.1.5 on 2021-01-25 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0002_auto_20210125_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckcard',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(1)]),
        ),
    ]
