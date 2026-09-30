from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('dashboard')
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html') # Django ka default login use karenge