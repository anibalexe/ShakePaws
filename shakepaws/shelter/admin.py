from django.contrib import admin
from .models import Animal, Sponsor, Animal_sponsor

# Register your models here.
class Animal_sponsorInLine(admin.TabularInline):
    model = Animal_sponsor
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    inlines = [Animal_sponsorInLine,]
    readonly_fields = ('created', 'updated')

admin.site.register(Sponsor)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Animal_sponsor)