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
        
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.userID = request.user
            job_application.save()
            
            return redirect('display')
        else:
            messages.success(request, form.errors)
            messages.success(request, 'Failed to Add Application')

    return render(request,'createApplication.html',context)


@login_required
def displayApplications(request):

    currentUser = request.user

    query = jobApplication.objects.all().filter(userID = currentUser).order_by('-jobDeadline')
    context = {'query': query}
    print(context)
    
    return render(request,'displayApplications.html',context)