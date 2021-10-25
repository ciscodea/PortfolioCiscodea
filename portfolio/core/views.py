"""Core views module"""

# Django
from django.shortcuts import render

# Models
from .models import Skill


def home(request):
    skills = Skill.objects.all()
    context = {
        "skills": skills
    }
    return render(request, "core/home.html", context=context)