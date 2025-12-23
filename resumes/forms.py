from django.forms import ModelForm
from resumes.models import *


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = [
            "name",
            "phone",
            "email",
        ]


class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "resume",
            "school",
            "degree",
            "start_date",
            "end_date",
        ]


    def __init__(self, author, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields["resume"].queryset = Resume.objects.filter(author=author)


class EmploymentForm(ModelForm):
    class Meta:
        model = Employment
        fields = [
            "resume",
            "company",
            "position",
            "start_date",
            "end_date"
        ]


    def __init__(self, author, *args, **kwargs):
        super(EmploymentForm, self).__init__(*args, **kwargs)
        self.fields["resume"].queryset = Resume.objects.filter(author=author)


class ProjectsForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "resume",
            "project_name",
            "start_date",
            "end_date"
        ]


    def __init__(self, author, *args, **kwargs):
        super(ProjectsForm, self).__init__(*args, **kwargs)
        self.fields["resume"].queryset = Resume.objects.filter(author=author)


class SkillsForm(ModelForm):
    class Meta:
        model = Skill
        fields = [
            "resume",
            "skills"
        ]


    def __init__(self, author, *args, **kwargs):
        super(SkillsForm, self).__init__(*args, **kwargs)
        self.fields["resume"].queryset = Resume.objects.filter(author=author)


class JobDescriptionsForm(ModelForm):
    class Meta:
        model = JobDescription
        fields = [
            "employment",
            "job_description",
        ]


class ProjectDescriptionsForm(ModelForm):
    class Meta:
        model = ProjDescription
        fields = [
            "project",
            "proj_description",
        ]
