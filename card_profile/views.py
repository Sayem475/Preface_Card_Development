from django.shortcuts import render
from . import models

# Create your views here.
def view_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    print(data.name)
    return render(request, 'User/userProfile.html', 
                  {
                    'data': data
                  }
                  )

def edit_profile(request):
    return render(request, 'User/editProfile.html')