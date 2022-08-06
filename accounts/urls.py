from django.urls import  path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup__, name='signup'),
    path('', views.login__, name='login'),
    path('logout/', views.logout__, name='logout'),
]