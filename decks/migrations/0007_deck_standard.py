# Generated by Django 3.1.6 on 2021-02-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0006_auto_20210209_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='standard',
            field=models.BooleanField(default=False),
        ),
    ]
