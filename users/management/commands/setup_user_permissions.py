from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    GROUPS = ["Basic", "Admin", "Master"]
    PERMISSIONS = {
        "Basic": ["deck", "deckcard"],
        "Admin": [
            "deck",
            "deckcard",
            "card",
            "collection",
            "expansion",
            "power",
            "heroclass",
            "hero",
            "keyword",
        ],
        "Master": [
            "deck",
            "deckcard",
            "card",
            "collection",
            "expansion",
            "power",
            "heroclass",
            "hero",
            "keyword",
            "user",
            "permission",
            "group",
        ],
    }

    def handle(self, *args, **kwargs):
        for v in self.GROUPS:
            group = Group.objects.create(name=v)
            for model in self.PERMISSIONS[v]:
                group.permissions.add(Permission.objects.get(codename="add_" + model))
                group.permissions.add(
                    Permission.objects.get(codename="change_" + model)
                )
                group.permissions.add(
                    Permission.objects.get(codename="delete_" + model)
                )
