# Generated by Django 5.0 on 2023-12-14 16:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("userAuth", "0003_company_alter_jobapplication_jobid_delete_jobs"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jobapplication",
            old_name="jobID",
            new_name="companyID",
        ),
    ]
