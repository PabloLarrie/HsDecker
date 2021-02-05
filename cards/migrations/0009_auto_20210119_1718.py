# Generated by Django 3.1.4 on 2021-01-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_auto_20210119_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='decks',
        ),
        migrations.RemoveField(
            model_name='card',
            name='keywords',
        ),
        migrations.AlterField(
            model_name='card',
            name='heroes',
            field=models.ManyToManyField(null=True, related_name='cards', to='cards.HeroClass'),
        ),
    ]
