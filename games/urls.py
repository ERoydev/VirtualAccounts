from django.urls import path
from . import views


urlpatterns = [
    path('twitch/user/<str:username>/', views.get_twitch_user_view, name='twitch_user'),
]