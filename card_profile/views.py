from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    return render(request, 'User/userProfile.html', 
      {
        'data': data
      }
    )

@login_required(login_url='login')
def edit_profile(request, id):
    return render(request, 'User/editProfile.html')