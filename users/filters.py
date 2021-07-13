from rest_framework_filters import FilterSet, filters

from users.models import Profile


class ProfilesFilter(FilterSet):

    class Meta:
        model = Profile
        fields = [
            "username",
        ]