# Generated by Django 3.1.4 on 2021-01-12 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20210111_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(max_length=150, null=True),
        ),
    ]