"""shakepaws URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from shelter import views as shelter_views
from django.conf import settings
from animalProfile import views as animalProfile_views
from sponsorProfile import views as sponsorProfile_views
#from registration import views as registration_views

urlpatterns = [
    path('', core_views.index, name = "inicio"),
    path('informacion/', core_views.information, name = "informacion"),
    path('apadrinar/', shelter_views.sponsoring , name = "apadrinar"),
    path('perfil-animal/<int:animal_id>/', animalProfile_views.profile , name = "perfil-animal"),
    
    path('validation/<int:animal_id>/<sponsor_id>/', animalProfile_views.validation , name = "validation"),
    
    #path('perfil-padrino/<int:id>/', sponsorProfile_views.profile , name = "perfil-padrino"),
    path('perfil-animal/', animalProfile_views.profile , name = "perfil-animal"),
    path('admin/', admin.site.urls, name = "administrador"),
    
    #Path de autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)