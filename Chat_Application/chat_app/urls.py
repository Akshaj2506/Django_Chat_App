from django.urls import path, include
from chat_app import views

urlpatterns = [
   path("", views.login_form, name =""),
   path("login", views.login_form, name ="login"),
   path("signup", views.signup, name ="signup"),
   path("logout", views.logout_view, name ="logout"),
   path("chat", views.chat, name ="chat"),
   path('messages/<int:user_id>/', views.get_messages, name='get_messages')
]