from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, loginForm

# Create your views here.
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')



    context = {'form':form}
    return render(request, "register.html",context)

def loginPage(request):
    form = loginForm()
    context = {'form':form}


    return render(request, "login.html",context = {'form':form})