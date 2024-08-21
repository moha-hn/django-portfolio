from django.shortcuts import render,redirect
from .forms import *
from django.template.loader import render_to_string
from django.conf import settings


from django.core.mail import send_mail

# Create your views here.
def accueilfr(request):
    return render(request,"fr/indexfr.html") 



def projectfr(request):
    return render(request,"fr/projectsfr.html") 

def resumefr(request):
    return render(request,"fr/resumefr.html") 

def contactfr(request):
    if request.method=='POST':
        form=ContactFormfr(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactfr')
    else:
        form = ContactFormfr()
        return render(request, 'fr/contactfr.html',{'form':form})


'''anglais'''
def accueileng(request):
    return render(request,"eng/indexeng.html") 


def contacteng(request):
    if request.method=='POST':
        form=ContactFormeng(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacteng')
    else:
        form = ContactFormeng()
        return render(request, 'eng/contacteng.html',{'form':form})

def projecteng(request):
    return render(request,"eng/projectseng.html") 

def resumeeng(request):
    return render(request,"eng/resumeeng.html") 