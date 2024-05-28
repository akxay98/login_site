from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    if request.method=='POST':
        if request.POST.get('submit')=='SIGN UP':
            username = request.POST['uname']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            password = request.POST['pwd']
            cpwd = request.POST['cpwd']

            if(password==cpwd):
                my_user = User.objects.create_user(username, email, password)
                my_user.first_name = fname
                my_user.last_name = lname
                my_user.save()
                messages.success(request, 'Your Account has been successfully created. Please Signin')
                return redirect('index')
            else:
                messages.error(request, 'Passwords doesnt match. Please Sign up Again')
        if request.POST.get('submit')=='SIGN IN':
            username = request.POST['unamel']
            password = request.POST['pwdl']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                fname = user.first_name
                return render(request, 'LoginApp/home.html', {'fname':fname})
            
            else:
                messages.error(request, 'Invalid credentials. Please Try Again')
                return redirect('index')
    return render(request, 'LoginApp/index.html')

def logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('index')
