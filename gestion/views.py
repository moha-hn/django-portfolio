from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from myapp.models import *
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(username=username,password=password)
            if  user is not None :
                    login(request, user)
                    return redirect('admin')
    return render(request,'login/login.html',context={'form':AuthenticationForm()})

@login_required
def admin(request):
    con=contact.objects.all()
    context={
        "contact":con,
    }
    return render(request,"admin/admin.html",context)


def logout_view(request):
    logout(request)
    return redirect("login")

