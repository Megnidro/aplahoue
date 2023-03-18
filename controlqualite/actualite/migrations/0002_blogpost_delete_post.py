# Generated by Django 4.1.7 on 2023-03-18 12:44

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actualite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='titre blog')),
                ('slug', models.SlugField(help_text='Exemple premier-article prendre en considération le tiret')),
                ('photo', django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_tall.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[370, 250], upload_to='work')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Content')),
                ('datepub', models.DateField(auto_now_add=True, verbose_name='Date de publication')),
                ('published', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=500)),
                ('auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'ordering': ['-datepub'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]