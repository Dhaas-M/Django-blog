from django.contrib import admin
from django.urls import path
from . import views
import articles

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('create/', views.article_create, name='create'),
    path('populate/', views.populate, name='populate'),
    path('<slug:slug>/', views.article_details, name='details')
]