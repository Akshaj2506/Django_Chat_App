from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def chat(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat_app/chat.html', {'users': users})

def login(request):
   return render(request, "chat_app/login.html")