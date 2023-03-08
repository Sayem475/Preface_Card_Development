from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def profile_login(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['name'], password=request.POST['pass'])
        if user is not None:
            login(request, user)
            return redirect('viewProfile', user.id)
        print(user)
    return render(request, 'Auth/userlogin.html')

def profile_logout(request):
    logout(request)
    return redirect('login')
