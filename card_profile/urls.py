from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.view_profile, name='view_profile'),
    path('edit/<int:id>', views.edit_profile, name='editProfile')
]