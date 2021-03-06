# Generated by Django 3.1.4 on 2021-01-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0007_auto_20210119_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='race',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
