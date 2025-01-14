from django.urls import path, include
from chat_app import views

urlpatterns = [
   path("login", views.login_form, name ="login"),
   path("signup", views.signup, name ="signup"),
   path("chat", views.chat, name ="chat")
]