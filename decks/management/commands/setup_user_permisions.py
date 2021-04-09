from django.core.management import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import AbstractUser

unauthorized_permissions = (
    "Can view card",
    "Can view collection",
    "Can view key word",
    "Can view power",
    "Can view hero class",
    "Can view hero",
    "Can view expansion",
    "Can view deck",
)

user_permissions = unauthorized_permissions + (
    # "Can view card",
    # "Can view collection",
    # "Can view key word",
    # "Can view power",
    # "Can view hero class",
    # "Can view hero",
    # "Can view expansion",
    # "Can view deck",
    "Can view deck card",
    "Can add deck",
    "Can change deck",
    "Can delete deck",
    "Can add deck card",
    "Can change deck card",
    "Can delete deck card",
)

superuser_permissions = user_permissions + (
    "Can add log entry",
    "Can change log entry",
    "Can delete log entry",
    "Can view log entry",
    "Can add permission",
    "Can change permission",
    "Can delete permission",
    "Can view permission",
    "Can add group",
    "Can change group",
    "Can delete group",
    "Can view group",
    "Can add user",
    "Can change user",
    "Can delete user",
    "Can view user",
    "Can add content type",
    "Can change content type",
    "Can delete content type",
    "Can view content type",
    "Can add session",
    "Can change session",
    "Can delete session",
    "Can view session",
    "Can add card",
    "Can change card",
    "Can delete card",
    # "Can view card",
    "Can add collection",
    "Can change collection",
    "Can delete collection",
    # "Can view collection",
    "Can add key word",
    "Can change key word",
    "Can delete key word",
    # "Can view key word",
    "Can add power",
    "Can change power",
    "Can delete power",
    # "Can view power",
    "Can add hero class",
    "Can change hero class",
    "Can delete hero class",
    # "Can view hero class",
    "Can add hero",
    "Can change hero",
    "Can delete hero",
    # "Can view hero",
    "Can add expansion",
    "Can change expansion",
    "Can delete expansion",
    # "Can view expansion",
    # "Can add deck",
    # "Can change deck",
    # "Can delete deck",
    # "Can view deck",
    # "Can add deck card",
    # "Can change deck card",
    # "Can delete deck card",
    # "Can view deck card",
)

# basic_group, created = Group.objects.get_or_create(name="BasicUser")


# doctor_group.permissions.set([permission_list])
# doctor_group.permissions.add(permission, permission, ...)
# doctor_group.permissions.remove(permission, permission, ...)
# doctor_group.permissions.clear()

# doctor_group.user_set.add(user)
#             OR
# user.groups.add(doctor_group)


# class Command(BaseCommand):
#     def handle(self, *args, **kwargs):
#         group = Group.obejcts.create()
#         group.set_permissions(
