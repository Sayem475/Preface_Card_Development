from django.shortcuts import render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    social = models.SocialLinksIntems.objects.filter(card_user=data)
    skill = models.SkillsIntems.objects.filter(card_user=data)
    return render(request, 'User/userProfile.html', 
      {
        'links': social,
        'data': data,
        'auth': request.user.is_authenticated,
        'skills': skill
      }
    )

@login_required(login_url='login')
def edit_profile(request, id):
    data = models.CardUser.objects.get(id=id)
    social = models.SocialLinksIntems.objects.filter(card_user=data)
    skill = models.SkillsIntems.objects.filter(card_user=data)
    professional = models.ProfessionalItems.objects.filter(card_user=data)
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
          
          skill.delete()
          for i in range(len(request.POST.getlist('skl_name'))):
              model = models.SkillsIntems()
              model.card_user = data
              model.skill = request.POST.getlist('skl_name')[i]
              model.save()
          
          professional.delete()
          for i in range(len(request.POST.getlist('prof_company'))):
              model = models.ProfessionalItems()
              model.card_user = data
              model.designation = request.POST.getlist('prof_designation')[i]
              model.company_name = request.POST.getlist('prof_company')[i]
              model.work_from = request.POST.getlist('prof_from_date')[i]
              model.work_to = request.POST.getlist('prof_to_date')[i]
              model.location = request.POST.getlist('prof_location')[i]
              model.save()

      return render(request, 'User/editProfile.html', 
        {
          'data': data,
          'links': social,
          'skills': skill,
          'professions': professional
        }
      )
    else:
        return HttpResponse(404)
  
def profile_onboard_log(request):
    return render(request, 'Onboard/onBoardLog.html')

def profile_onboard(request, id):
    return render(request, 'Onboard/onBoard.html')