from rest_framework import routers
from django.urls import path, include
from cards import views

app_name = "cards"

router = routers.SimpleRouter()

router.register(r"cards", views.CardViewSet, basename="cards")

urlpatterns = [
    path('', include(router.urls)),
]
