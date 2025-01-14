from django.urls import path, include
from chat_app import views

urlpatterns = [
   path("", views.login, name ="login"),
   path("chat", views.chat, name ="chat")
]