from django.shortcuts import render

# Create your views here.
def profile_login(request):
    return render(request, 'Auth/userlogin.html')