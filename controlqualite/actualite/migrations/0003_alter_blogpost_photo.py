# Generated by Django 4.1.7 on 2023-03-18 13:01

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('actualite', '0002_blogpost_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=['top', 'center'], default='default_tall.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[370, 250], upload_to='work'),
        ),
    ]
