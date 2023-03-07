from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_login, name='login'),
    path('logout', views.profile_logout, name='logout')
]