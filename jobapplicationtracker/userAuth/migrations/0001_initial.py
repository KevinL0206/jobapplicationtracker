# Generated by Django 5.0 on 2023-12-14 16:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="jobs",
            fields=[
                ("jobID", models.AutoField(primary_key=True, serialize=False)),
                ("companyName", models.CharField(max_length=255)),
                ("jobDescription", models.TextField()),
                ("jobLocation", models.CharField(max_length=255)),
                ("jobDeadline", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="jobApplication",
            fields=[
                ("applicationID", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.CharField(max_length=255)),
                (
                    "userID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "jobID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userAuth.jobs"
                    ),
                ),
            ],
        ),
    ]
