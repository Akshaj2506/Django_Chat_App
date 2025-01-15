from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserSignupForm, UserLoginForm
from django.contrib.auth import authenticate, login
from .models import ChatMessage
from django.db.models import Q
from django.http import JsonResponse

def chat(request):
   users = User.objects.exclude(id=request.user.id)
   return render(request, 'chat_app/chat.html', {'users': users})
def get_messages(request, user_id):
    try:
        other_user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User does not exist."}, status=404)

    messages = ChatMessage.objects.filter(
        (Q(sender=request.user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=request.user))
    ).order_by('timestamp')

    messages_data = [{'sender': msg.sender.username, 'message': msg.message, 'timestamp': msg.timestamp} for msg in messages]
    return JsonResponse(messages_data, safe=False)

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
                return redirect('chat')
            else:
                form.add_error(None, 'Invalid username or password')
   else:
      form = UserLoginForm()
   
   return render(request, 'chat_app/login.html', {'form': form})