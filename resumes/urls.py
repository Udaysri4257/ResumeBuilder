from django.urls import path
from .views import *

urlpatterns = [
    path("home", home, name="home"),
    path("create/", create_resume, name="create_resume"),
    path("<int:id>/", show_resume, name="show_resume"),
    path("create/education", create_education, name="create_education"),
    path("create/employment", create_employment, name="create_employment"),
    path("create/project", create_project, name="create_project"),
    path("create/skills", create_skills, name="create_skills"),
    path("create/job_description", create_job_description, name="create_job_description"),
    path("create/project_description", create_project_description, name="create_project_description"),
    path("pdf/<int:id>/", create_resume_pdf, name="create_resume_pdf"),
    path("<int:id>/delete/", delete_resume, name="delete_resume"),
    path("education/<int:id>/delete/", delete_education, name="delete_education"),
    path("employment/<int:id>/delete/", delete_employment, name="delete_employment"),
    path("project/<int:id>/delete/", delete_project, name="delete_project"),
    path("skill/<int:id>/delete/", delete_skill, name="delete_skill"),
    path("jobdescription/<int:id>/delete/", delete_job_description, name="delete_job_description"),
    path("projectdescription/<int:id>/delete/", delete_project_description, name="delete_project_description"),
]
