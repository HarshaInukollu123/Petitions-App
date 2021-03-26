from django.urls import path,include
from rest_framework import routers
from .views import PetitionModelViewSet

router = routers.DefaultRouter()
router.register(r'petitions', PetitionModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
