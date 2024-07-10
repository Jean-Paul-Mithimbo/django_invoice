from django.shortcuts import render

# Create your views here.

def home(request,*arg,**kwargs):
    return render(request,'base.html')