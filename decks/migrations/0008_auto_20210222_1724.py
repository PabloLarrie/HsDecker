# Generated by Django 3.1.6 on 2021-02-22 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0012_remove_card_decks'),
        ('decks', '0007_deck_standard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='cards',
        ),
        migrations.AlterField(
            model_name='deck',
            name='standard',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='deckcard',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deck_cards', to='cards.card'),
        ),
        migrations.AlterField(
            model_name='deckcard',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deck_cards', to='decks.deck'),
        ),
    ]