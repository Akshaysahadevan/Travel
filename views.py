from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(req):
    if req.method=='POST':
        user_name=req.POST['username']
        first_name=req.POST['first_name']
        last_name=req.POST['last_name']
        email_id=req.POST['email']
        passw=req.POST['password']
        cpass=req.POST['cpassword']
        if passw==cpass:
            if User.objects.filter(username=user_name).exists():
                messages.info(req,"name already taken")
                return redirect('register')
            elif User.objects.filter(email=email_id).exists():
                messages.info(req,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email_id,password=passw)
                user.save();
                return redirect('userlogin')

        else:
            messages.info(req,"password not matching")
            return redirect('register')
        return redirect('indexpg')
    return render(req,'loginpage.html')

def userlogin(req):
    if req.method =='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(req,user)
            return redirect('indexpg')
        else:
            messages.info(req,"invalid user")
            return redirect('userlogin')
    return render(req,"userlogpage.html")


def logout(req):
    auth.logout(req)
    return redirect('indexpg')
