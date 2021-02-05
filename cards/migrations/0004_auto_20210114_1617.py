# Generated by Django 3.1.4 on 2021-01-14 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20210112_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroclass',
            name='description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='heroclass',
            name='power',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cards.power'),
        ),
    ]