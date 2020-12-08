from django.urls import path
from . import views
from .views import Profile_animalCreate


urlpatterns =[
    path('perfil-animal/<int:animal_id>/', views.profile , name = "perfil-animal"),
    path('validation/<int:animal_id>/<sponsor_id>/', Profile_animalCreate.as_view() , name = "validation"),
    #path('perfil-padrino/<int:id>/', sponsorProfile_views.profile , name = "perfil-padrino"),
    #path('perfil-animal/', views.profile , name = "perfil-animal"),

]