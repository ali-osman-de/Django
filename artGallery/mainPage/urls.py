from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage),
    path('/', views.mainPage),
    path('home',views.mainPage),
]
