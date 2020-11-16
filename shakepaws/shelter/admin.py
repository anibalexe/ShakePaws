from django.contrib import admin
from .models import Animal, Sponsor 
#, Animal_sponsor

# Register your models here.
admin.site.register(Animal)
admin.site.register(Sponsor)
#admin.site.register(Animal_sponsor)