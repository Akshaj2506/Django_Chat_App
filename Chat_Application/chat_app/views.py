from django.shortcuts import render

# Create your views here.
def chat(request):
   return render(request, "chat_app/index.html")

def login(request):
   return render(request, "chat_app/login.html")