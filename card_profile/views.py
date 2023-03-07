from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    return render(request, 'User/userProfile.html', 
      {
        'data': data,
        'auth': request.user.is_authenticated
      }
    )

@login_required(login_url='login')
def edit_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    if data.user == request.user:
      if request.method == 'POST':
          data.name = request.POST['name']
          data.designation = request.POST['designation']
          data.about = request.POST['about']
          data.phone_number = request.POST['phone_number']
          data.email = request.POST['email']
          data.address = request.POST['address']

          data.save()

      return render(request, 'User/editProfile.html', 
        {
          'data': data
        }
      )
    else:
        return HttpResponse(404)