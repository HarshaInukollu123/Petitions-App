from .serializers import PetitionSerializer
from .models import Petition
from rest_framework import viewsets

class PetitionModelViewSet(viewsets.ModelViewSet):
    queryset = Petition.objects.all()
    serializer_class = PetitionSerializer
