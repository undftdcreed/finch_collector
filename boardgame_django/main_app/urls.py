from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"), 
    path('games/', views.GameList.as_view(), name="game_list"),
]