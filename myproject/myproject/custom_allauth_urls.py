# custom_allauth_urls.py

from allauth.account import views as account_views
from django.urls import path,include
from allauth.socialaccount.providers.google import views as google_views
from allauth.socialaccount.providers.google import urls as google_urls
from allauth.socialaccount import views as socialaccount_views

urlpatterns = [
    #path('google/login/', google_views.oauth2_login, name='google_login'),
    path('logout/', account_views.logout, name='account_logout'),
    path('', include(google_urls)),
    path('social/cancelled/', socialaccount_views.login_cancelled, name='socialaccount_login_cancelled'),
    path('social/error/', socialaccount_views.login_error, name='socialaccount_login_error'),
    
    # Add other views you want to include
]
