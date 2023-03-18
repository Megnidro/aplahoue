from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _


class ValeurPost(models.Model):
    title = models.CharField(max_length=300)
    photo = ResizedImageField(size=[370, 250], crop=['top', 'left'], default='default_tall.jpg',
                              upload_to='work')
    description = RichTextField(blank=True, null=True, verbose_name=_("Content"))

    def get_absolute_url(self):
        return reverse("valeurs:home")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Valeurs"
