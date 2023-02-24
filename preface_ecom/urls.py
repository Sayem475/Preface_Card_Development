
from django.urls import path, include
from . import views
from django.views import View
from .views import *

urlpatterns = [
    path('/login', Login.as_view(), name='login'),
    path('/register', Register.as_view(), name='register'),
    path('', Home.as_view(), name='home'),
    path('/shop', Shop.as_view(), name='shop'),
    path('/productDetail', ProductDetails.as_view(), name='productDetail'),
    path('/blog', Blog.as_view(), name='blog'),
    path('/blogDetails', BlogDetail.as_view(), name='blogDetails'),
    path('/about', About.as_view(), name='about'),
    path('/contact', Contact.as_view(), name='contact'),
    path('/cart', Cart.as_view(), name='cart'),
    path('/checkout', Checkout.as_view(), name='checkout'),
    path('/mission', Mission.as_view(), name='mission'),
    path('/terms', Terms.as_view(), name='terms'),
    path('/userProfile', UserProfile.as_view(), name='userProfile'),
    path('/editProfile', EditProfile.as_view(), name='editProfile'),
    path('/userlogin', UserLoginCard.as_view(), name='userlogin'),
]
