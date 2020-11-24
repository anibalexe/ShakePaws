from django.contrib import admin
from .models import Profile, Profile_animal

# Register your models here.
class Profile_animalInLine(admin.TabularInline):
    model = Profile_animal
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [Profile_animalInLine,]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile_animal)