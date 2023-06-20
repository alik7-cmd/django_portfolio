from django.shortcuts import render
from .models import About
from .models import Education
from .models import Experience
from .models import Project


# Create your views here.

def home(request):
    about = About.objects.all()[0]
    education = Education.objects.all()
    experience = Experience.objects.all()
    project = Project.objects.all()
    skills = names = [
        "Formidable knowledge on latest android development tools with best practice(e.g: Jetpack Library,Coroutines, "
        "Retrofit and RESTful APIs etc)",
        "Version controlling and Git",
        "Experienced on Developing Android SDK.",
        "Experienced on Architecture pattern like MVVM, MVP & MVC Design pattern (SOLID), Functional programming "
        "concepts, Clean code & Android clean architecture.",
        "Dependency injection library Hilt & Dagger 2",
        " Unit Testing Using Mockito and Espresso.",
        "Working experience with Room and Realm DB.",
        "Web development with Django using python."]

    args = {
        'about': about,
        'education': education,
        'experience': experience,
        'project': project,
        'skills' : skills
    }
    return render(request, "layouts.html", args)


def education(request):
    data = Education.objects.all()
    context = {
        'education': data
    }
    return render(request, "education.html", context)


def experience(request):
    return render(request, "experience.html")
