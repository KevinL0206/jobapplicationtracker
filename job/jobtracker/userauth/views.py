from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, "register.html",context)

def loginPage(request):
    return render(request, "login.html")