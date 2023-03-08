from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    social = models.SocialLinksIntems.objects.filter(card_user=data)
    return render(request, 'User/userProfile.html', 
      {
        'links': social,
        'data': data,
        'auth': request.user.is_authenticated
      }
    )

@login_required(login_url='login')
def edit_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    social = models.SocialLinksIntems.objects.filter(card_user=data)
    if data.user == request.user:
      if request.method == 'POST':
          data.name = request.POST['name']
          data.designation = request.POST['designation']
          data.about = request.POST['about']
          data.phone_number = request.POST['phone_number']
          data.email = request.POST['email']
          data.address = request.POST['address']
          data.save()

          social.delete()
          for i in range(len(request.POST.getlist('sname'))):
                model = models.SocialLinksIntems()
                model.card_user = data
                model.social_name = request.POST.getlist('sname')[i]
                model.social_link = request.POST.getlist('slink')[i]
                model.save()

      return render(request, 'User/editProfile.html', 
        {
          'data': data,
          'links': social
        }
      )
    else:
        return HttpResponse(404)
  
def profile_onboard_log(request):
<<<<<<< HEAD
    return render(request, 'Onboard/onBoard.html')
=======
    return render(request, 'Onboard/onBoardLog.html')
>>>>>>> 6b44c6ad4d412b33feea4d62da8d6e7a3e487af1

def profile_onboard(request, id):
    return render(request, 'Onboard/onBoard.html')