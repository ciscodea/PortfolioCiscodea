"""Portfolio core models module"""

# Django
from django.db import models
from django.utils.translation import gettext as _


class Skill(models.Model):
    name = models.CharField(
        _("skill name"),
        max_length=255,
        blank=False,
        null=False
    )
    family_name = models.CharField(
        _("skill family name"),
        help_text=_("family from skill belongs e.g. Frameworks"),
        max_length=255,
        null=False,
        blank=False,
        default=_("others")
    )
    description = models.TextField(
        _("skill description"),
        blank=True,
        null=True
    )
    icon = models.ImageField(
        _("skill icon"),
        upload_to="images/skills/icons/",
        blank=True,
        null=True,
    )
    since_date = models.DateField(
        _("skill from date"),
        help_text=_("since what date did you acquire this skill")
    )

    def __str__(self):
        """Return str representation"""
        return self.name

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"
