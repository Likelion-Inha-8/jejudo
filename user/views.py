from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.


def home(req):
    if req.user is not None:
        user = req.user
    else:
        user = None
    print('hello')
    return render(req, 'home2.html', {'user': user})


def signin(req):
    return render(req, 'signin.html')


def signup(req):
    return render(req, 'signup.html')


def signout(req):
    logout(req)
    return redirect('home')


def proc(request):
    if(request.method == 'POST'):
        if (request.POST['proc'] == 'signin'):
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
        elif (request.POST['proc'] == 'signup'):
            username = request.POST["username"]
            password = request.POST["password"]
            user = User.objects.create_user(username, "", password)
            user.save()
            login(request, user)
    return redirect('home')
