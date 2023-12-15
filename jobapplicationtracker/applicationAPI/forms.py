from userAuth.models import jobApplication
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

class DateInput(forms.DateInput):
        input_type = 'date'

class createJobApplicationData(forms.ModelForm):

    
    class Meta:
        model = jobApplication
        fields = "__all__"
        exclude = ('userID',)
        widgets = {
            'status': forms.Select(attrs={'class':'form-control'}),
            'applicationDate': DateInput(),
            'jobDeadline' : DateInput(),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        application_date = cleaned_data.get('applicationDate')
        job_deadline = cleaned_data.get('jobDeadline')

        if application_date and job_deadline and job_deadline < application_date:
            raise ValidationError("Job Deadline cannot be after Application Date")

        return cleaned_data

