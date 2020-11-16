from django.contrib import admin
from .models import Animal, Sponsor#, Animal_sponsor

# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Sponsor)
admin.site.register(Animal, AnimalAdmin)
#admin.site.register(Animal_sponsor)