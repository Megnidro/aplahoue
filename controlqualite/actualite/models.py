from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django_resized import ResizedImageField
from django.utils.translation import gettext_lazy as _


class BlogPost(models.Model):
    title = models.CharField(max_length=500, verbose_name="titre blog")
    slug = models.SlugField(help_text="Exemple premier-article prendre en considération le tiret")
    photo = ResizedImageField(size=[370, 250], crop=['top', 'left'], default='default_tall.jpg',
                              upload_to='work')
    description = RichTextField(blank=True, null=True, verbose_name=_("Content"))
    datepub = models.DateField(verbose_name="Date de publication", auto_now_add=True)
    published = models.BooleanField(default=False)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=500)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:home")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-datepub']
        verbose_name = "Blog"
