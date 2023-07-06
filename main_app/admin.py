from django.contrib import admin
from .models import Cephalopod, Species, Animal

# Register your models here.
admin.site.register(Cephalopod)
admin.site.register(Species)
admin.site.register(Animal)