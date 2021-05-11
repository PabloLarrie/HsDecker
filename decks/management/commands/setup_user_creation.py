from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class Command(BaseCommand):

    GROUPS = ["Basic", "Admin", "Master"]
    USERS = ["BasicUser", "AdminUser", "MasterUser"]

    def handle(self, *args, **kwargs):
        for index, user in enumerate(self.USERS):
            user = User.objects.create(username=user)
            user.groups.set([Group.objects.get(name=self.GROUPS[index])])
