from rest_framework import routers
from django.urls import path, include
from decks import views

app_name = "decks"

router = routers.SimpleRouter()

router.register(r"decks", views.DeckViewSet, basename="decks")

urlpatterns = [
    path('', include(router.urls)),
]
