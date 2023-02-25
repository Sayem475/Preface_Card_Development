from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import *
# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'Auth/login.html')
        
class Register(View):
    def get(self, request):
        return render(request, 'Auth/register.html')

class Home(View):
    def get(self, request):
        return render(request, 'Pages/home.html')

class ProductDetails(View):
    def get(self, request):
        return render(request, 'Pages/productDetail.html')

class Shop(View):
    def get(self, request):
        return render(request, 'Pages/shop.html')

class Cart(View):
    def get(self, request):
        return render(request, 'Pages/cart.html')

class Checkout(View):
    def get(self, request):
        return render(request, 'Pages/checkout.html')

class Blog(View):
    def get(self, request):
        return render(request, 'Blog/blog.html')

class BlogDetail(View):
    def get(self, request):
        return render(request, 'Blog/blogDetails.html')

class About(View):
    def get(self, request):
        return render(request, 'Others/about.html')

class Contact(View):
    def get(self, request):
        return render(request, 'Others/contact.html')

class Mission(View):
    def get(self, request):
        return render(request, 'Others/mission.html')

class Terms(View):
    def get(self, request):
        return render(request, 'Others/terms.html')

class UserProfile(View):
    def get(self, request):
        return render(request, 'User/userProfile.html')

class EditProfile(View):
    def get(self, request):
        return render(request, 'User/editProfile.html')

class UserLoginCard(View):
    def get(self, request):
        return render(request, 'User/userlogin.html')

class CardOnBoard(View):
    def get(self, request):
        return render(request, 'Pages/cardonboard.html')


class ConfirmCard(View):
    def get(self, request):
        return render(request, 'Pages/confirmcard.html')

