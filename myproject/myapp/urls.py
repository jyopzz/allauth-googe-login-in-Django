from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/signup/',views.signup,name='signup')
]
