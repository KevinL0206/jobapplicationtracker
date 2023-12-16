from django.shortcuts import render, redirect, get_object_or_404
from userAuth.models import jobApplication
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import createJobApplicationData, editJobApplicationData
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


@login_required
def createJobApplication(request):
    form = createJobApplicationData()
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
def editApplication(request):

    form = editJobApplicationData()
    currentUser = request.user
    query = jobApplication.objects.all().filter(userID = currentUser).order_by('applicationID')
    userApplications = jobApplication.objects.filter(userID=currentUser)
    applicationIDs = [app.applicationID for app in userApplications]
    context = {
        'form':form,
        'applicationIDs': applicationIDs,
        'query': query
    }

    if request.method == "POST":
        data = request.POST.copy()
        applicationID= data.pop('application_id',None)
        form = editJobApplicationData(data)
        

        if form.is_valid():
            application = get_object_or_404(jobApplication,applicationID=int(applicationID[0]))
            for field_name, value in form.cleaned_data.items():

                if value is not None:
                    setattr(application, field_name, value)

            application.save()
            return redirect('display')
        
        else:
            return JsonResponse({'error': form.errors}, status=400)


    
    return render(request, 'editApplication.html',context)

def deleteApplication(request):
    currentUser = request.user
    query = jobApplication.objects.all().filter(userID = currentUser).order_by('applicationID')
    userApplications = jobApplication.objects.filter(userID=currentUser)
    applicationIDs = [app.applicationID for app in userApplications]
    context = {
        'applicationIDs': applicationIDs,
        'query': query
    }

    if request.method == "POST":
        data = request.POST.copy()
        applicationID= data.pop('application_id',None)

        if applicationID:
            row = jobApplication.objects.get(applicationID = int(applicationID[0]))
            row.delete()
            return redirect('display')
        else:
            messages.success(request, 'No Application Selected')

    return render(request, 'deleteApplication.html',context)


@login_required
def displayApplications(request):

    currentUser = request.user

    query = jobApplication.objects.all().filter(userID = currentUser).order_by('applicationID')
    context = {'query': query}
    print(context)
    
    return render(request,'displayApplications.html',context)