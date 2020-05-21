from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import University


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    name = forms.CharField(max_length=254, required=True)
    surname = forms.CharField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'name', 'surname', 'email', 'password1', 'password2')


class ContactInfoForm(forms.Form):
    city = forms.CharField(max_length=254, required=True)
    country = forms.CharField(max_length=254, required=True)
    phone = forms.CharField(max_length=254, required=False)
    github = forms.CharField(max_length=254, required=False)
    linkedin = forms.CharField(max_length=254, required=False)
    personal_website = forms.CharField(max_length=254, required=False)
    email = forms.CharField(max_length=254, required=True)


class ExperienceForm(forms.Form):
    start = forms.CharField(max_length=254, required=True)
    end = forms.CharField(max_length=254, required=True)
    company = forms.CharField(max_length=254, required=True)
    position = forms.CharField(max_length=254, required=True)
    description = forms.CharField(max_length=254, required=True)


class SkillsForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)


class LanguagesForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)
    description = forms.CharField(max_length=254, required=True)


class InterestsForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)


class ProjectsForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)
    description = forms.CharField(max_length=254, required=True)


class OrganizationsForm(forms.Form):
    name = forms.CharField(max_length=254, required=True)
    description = forms.CharField(max_length=254, required=True)


def get_universities():
    un = University.objects.all()
    universities = []
    for i in un:
        universities.append((i.name, i.name))
    return universities


class EducationForm(forms.Form):
    start = forms.CharField(max_length=254, required=True)
    end = forms.CharField(max_length=254, required=True)
    field_of_study = forms.CharField(max_length=254, required=True)
    degree = forms.CharField(max_length=254, required=True)
    faculty = forms.CharField(max_length=254, required=False)
    university = forms.CharField(widget=forms.Select(choices=get_universities()), required=True)


class UniversityForm(forms.Form):
    name = forms.CharField(max_length=254, required=True, label="University name")
    city = forms.CharField(max_length=254, label="University city", required=True)
    zip = forms.CharField(max_length=254, label="University zip code", required=True)
    street = forms.CharField(max_length=254, label="University street", required=True)
    street_number = forms.CharField(max_length=254, label="University street number", required=True)


class NewCV(forms.Form):
    description = forms.CharField(max_length=254, required=False)
    name = forms.CharField(max_length=254, required=True)
