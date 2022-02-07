from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Incorrect Username or Password")
            return redirect("login")
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
                #print("user name taken")
            else:
                user = User.objects.create_user(first_name = first_name, last_name = last_name, username = username, password = password)
                user.save()
                #print("User created")
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            #print("password not matching")
            return redirect('register')
        
        return redirect('/')
    else:
        #print("not created")
        return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")


