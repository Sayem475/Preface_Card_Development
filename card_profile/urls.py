from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_profile, name='view_profile'),
    path('edit', views.edit_profile, name='editProfile')
]