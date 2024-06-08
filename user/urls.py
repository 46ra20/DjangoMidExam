from django.urls import path
from .views import UserRegistration,UserLogin,UserLogout,UserProfile,ResetYourPassword

urlpatterns = [
    path('registration/',UserRegistration,name='useregistration'),
    path('login/',UserLogin,name='userlogin'),
    path('logout/',UserLogout,name='logout'),
    path('userprofile/',UserProfile,name='profile'),
    path('resetpassword/',ResetYourPassword.as_view(),name='resetpassword'),
]
