from django.urls import path
from .views import SignUpView, ProfileUpdate, panel, notification, sponsors

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('perfil-padrino/', ProfileUpdate.as_view() , name = "perfil-padrino"),
    path('panel/', panel, name="panel"),
    path('notificaciones/', notification, name="notificaciones"),
    path('apadrinamientos/', sponsors, name="apadrinamientos"),
]
