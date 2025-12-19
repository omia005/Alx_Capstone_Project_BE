from django.urls import path
from . import views


urlpatterns = [
  path('', views.register_view, name = 'signup' ),
  path('login/', views.login_view, name = 'login' ),
]