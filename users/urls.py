from rest_framework import routers
from django.urls import path, include
from users import views

app_name = "users"

router = routers.SimpleRouter()

# router.register(r"users", views.UserViewSet, basename="users")
router.register(r"profiles", views.ProfileViewSet, basename="profiles")

urlpatterns = [
    path('', include(router.urls)),
]
