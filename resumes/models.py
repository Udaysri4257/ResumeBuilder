from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Resume(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    created_on = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, related_name="resumes", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    resume = models.ForeignKey("Resume", related_name="education", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.school


class Employment(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    employment_descriptions = models.ForeignKey("JobDescription", related_name="employer", on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey("Resume", related_name="employment", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.company


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    project_descriptions = models.ForeignKey("ProjDescription", related_name="projects", on_delete=models.CASCADE, null=True)
    resume = models.ForeignKey("Resume", related_name="projects", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.project_name


class Skill(models.Model):
    skills = models.CharField(max_length=200)
    resume = models.ForeignKey("Resume", related_name="skillset", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.skills


class JobDescription(models.Model):
    job_description = models.CharField(max_length=250)
    employment = models.ForeignKey("Employment", related_name="jobdescriptions", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.job_description


class ProjDescription(models.Model):
    proj_description = models.CharField(max_length=250)
    project = models.ForeignKey("Project", related_name="projdescriptions", on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.proj_description
