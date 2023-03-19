from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _


class RealisationPost(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField(blank=True, null=True, verbose_name=_("Content"))
    photo = ResizedImageField(size=[370, 250], crop=['top', 'left'], default='default_tall.jpg',
                              upload_to='work')
    maitre_douvrage = models.CharField(max_length=500)
    architecte = models.CharField(max_length=500)
    livraison = models.DateField()
    montant_travaux = models.CharField(max_length=100)
    specificite_technique = models.CharField(max_length=500)
    published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("realisations:home")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-livraison']
        verbose_name = "Realisation"
