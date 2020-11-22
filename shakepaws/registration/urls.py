from django.urls import path
from .views import SignUpView, ProfileUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('perfil-padrino/', ProfileUpdate.as_view() , name = "perfil-padrino"),
]
