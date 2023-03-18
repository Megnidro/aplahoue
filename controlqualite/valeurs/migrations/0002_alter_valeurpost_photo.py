# Generated by Django 4.1.7 on 2023-03-18 13:39

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('valeurs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valeurpost',
            name='photo',
            field=django_resized.forms.ResizedImageField(crop=['top', 'left'], default='default_tall.jpg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[370, 250], upload_to='work'),
        ),
    ]