from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth import authenticate, login

# Create your views here.
def chat(request):
   users = User.objects.exclude(id=request.user.id)
   return render(request, 'chat_app/chat.html', {'users': users})


def signup(request):
   if request.method == 'POST':
      form = UserSignupForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('chat')
   else:
      form = UserSignupForm()
   return render(request, 'chat_app/signup.html', {'form': form})

def login_form(request):
   if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chat')  # Replace 'chat' with your desired redirect URL
            else:
                form.add_error(None, 'Invalid username or password')
   else:
      form = UserLoginForm()
   
   return render(request, 'chat_app/login.html', {'form': form})