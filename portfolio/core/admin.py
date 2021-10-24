"""Core admin module"""

# Django
from django.contrib import admin

# Models
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass
