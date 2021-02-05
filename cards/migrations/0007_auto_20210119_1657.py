# Generated by Django 3.1.4 on 2021-01-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0001_initial'),
        ('cards', '0006_auto_20210119_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('minion', 'Minion'), ('spell', 'Spell'), ('weapon', 'Weapon'), ('hero', 'Hero')], default='minion', max_length=6),
        ),
        migrations.AlterField(
            model_name='card',
            name='decks',
            field=models.ManyToManyField(blank=True, through='decks.DeckCard', to='decks.Deck'),
        ),
        migrations.AlterField(
            model_name='card',
            name='keywords',
            field=models.ManyToManyField(blank=True, related_name='cards', to='cards.KeyWord'),
        ),
        migrations.AlterField(
            model_name='card',
            name='quality',
            field=models.CharField(choices=[('free', 'Free'), ('common', 'Common'), ('rare', 'Rare'), ('epic', 'Epic'), ('legendary', 'Legendary')], default='common', max_length=12),
        ),
    ]