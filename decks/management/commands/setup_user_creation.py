from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


class Command(BaseCommand):

    GROUPS = ["Basic", "Admin", "Master"]
    USERS = ["BasicUser", "AdminUser", "MasterUser"]

    def handle(self, *args, **kwargs):
        for index, user in enumerate(self.USERS):
            for number, groupy in enumerate(self.GROUPS):
                if index == number:
                    user = User.objects.create(username=user)
                    user.groups.set([Group.objects.get(name=groupy)])
