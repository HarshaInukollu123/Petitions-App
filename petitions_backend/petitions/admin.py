from django.contrib import admin
from .models import Petition
# Register your models here.
@admin.register(Petition)
class PetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
