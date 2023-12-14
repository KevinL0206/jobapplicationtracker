from django.shortcuts import render, redirect
from userAuth.models import jobApplication
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import createJobApplicationData
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def createJobApplication(request):
    form = createJobApplicationData()
    #form.fields['userID'].initial = request.user
    context = {'form':form}
    if request.method == "POST":
        form = createJobApplicationData(request.POST)
        print (form.errors)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.userID = request.user
            job_application.save()
            messages.success(request,'Job Application Added')
            return redirect('display')
        else:
            messages.success(request, 'Failed to Add Application')

    return render(request,'createApplication.html',context)


def displayApplications(request):
    
    return render(request,'displayApplications.html')