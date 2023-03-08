from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.view_profile, name='viewProfile'),
    path('edit/<int:id>', views.edit_profile, name='editProfile'),
    path('admin/onboard', views.profile_onboard_log, name='onboardLog'),
    path('admin/onboard/<int:id>', views.profile_onboard, name='onBoard')
]