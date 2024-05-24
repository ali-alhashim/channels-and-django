from django.shortcuts import render, redirect
from django.views import View
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import MessageChat
from django.db.models import Q
# Create your views here.

class Main(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, 'chat/main.html',{})
    

class Login(View):
    def get(self, request):
        return render(request, 'chat/login.html',{})
    
    def post(self, request):
        data = request.POST.dict()
        username = data.get("username")
        password = data.get("password")
        print("login with username:", username)
        user = authenticate(requesrt = request, username = username, password = password)
        if user ==None:
            print("user not authenticate")
            return render(request, 'chat/login.html',{"message":"user not authenticate"})
        else:
            print("user is authenticate")
            login(request, user)
            return redirect('home')


    


class Register(View):
    def get(self, request):
        return render(request, 'chat/register.html',{})
    def post(self, request):
        data = request.POST.dict()
        first_name = data.get("first_name")
        last_name  = data.get("last_name")
        username   = data.get("username")
        email      = data.get("email")
        password   = data.get("password")

        print(first_name, last_name, username, email, password)

        new_user = User()
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.username = username
        new_user.email = email
        new_user.set_password(password)

        try:
            new_user.save()
        except Exception as e:
            return render(request, 'chat/register.html',{"message":e})

        user = authenticate(requesrt = request, username = username, password = password)
        if user ==None:
            print("user not authenticate")
            return render(request, 'chat/register.html',{"message":"user not authenticate"})
        else:
            print("user is authenticate")
            login(request, user)
            return redirect('home')
            

        
    
class Chat_person(View):
    def get(self, request, user_name,you):
        to_user = User.objects.get(username = user_name)
        old_messages = MessageChat.objects.filter(Q(from_who = request.user, to_who = to_user) | Q(from_who = to_user, to_who = request.user)).order_by("date", "time")
        return render(request, 'chat/chat_person.html',{"user_name":user_name, "old_messages":old_messages})
    

class Logout(View):
    def get(self, request):
        # run operation
        logout(request)
        return redirect('login')
    


class Home(View):
    def get(self, request):
        if request.user.is_authenticated:
            users = User.objects.all()
            return render(request, 'chat/home.html',{"users":users})
        else:
            return redirect("main")

        