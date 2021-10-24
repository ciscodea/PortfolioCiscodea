"""Core views module"""

# Django
from django.shortcuts import render

# Models
from .models import Skill


def home(request):
    text = "Hola soy el Pedro y Amo a la Yose "
    skills = Skill.objects.all()
    context = {
        "skills": skills
    }
    return render(request, "core/home.html", context=context)