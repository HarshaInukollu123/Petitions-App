from rest_framework import serializers
from .models import Petition

class PetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petition
        fields = ('title','image','description')
