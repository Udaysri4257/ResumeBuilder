from django.contrib import admin
from resumes.models import *

# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "phone",
        "email",
        "created_on",
        "author",
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "school",
        "degree",
        "start_date",
        "end_date",
        "resume"
    )


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "position",
        "start_date",
        "end_date",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "project_name",
        "start_date",
        "end_date",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "skills",
    )
