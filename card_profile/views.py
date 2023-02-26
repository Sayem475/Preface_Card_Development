from django.shortcuts import render

# Create your views here.
def view_profile(request):
    return render(request, 'User/userProfile.html')

def edit_profile(request):
    return render(request, 'User/editProfile.html')