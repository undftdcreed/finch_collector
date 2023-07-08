from django.urls import path
from . import views

urlpatterns = [

    path('', views.Home.as_view(), name ="home"),
    path('about/', views.About.as_view(), name="about"),
    path('gamelist/', views.GameList.as_view(), name = "game_list"),
    path('gamelist/new', views.GameCreate.as_view(), name = "game_create"),
    path('gamelist/<int:pk>/', views.GameDetail.as_view(), name="game_detail"),
    path('gamelist/<int:pk>/update', views.GameUpdate.as_view(), name="game_update"),
    path('gamelist/<int:pk>/delete', views.GameDelete.as_view(), name="game_delete"),
    path('accounts/signup', views.Signup.as_view(), name="signup"),

    
]