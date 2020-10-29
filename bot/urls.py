from django.urls import path
from . import views

urlpatterns = [
    path('', views.update, name="bot"),
    path('channel/exists/', views.channel_exists),
]
