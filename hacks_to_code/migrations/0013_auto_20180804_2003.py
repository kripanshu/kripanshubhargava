# Generated by Django 2.0.7 on 2018-08-04 20:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks_to_code', '0012_auto_20180804_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tinymce',
        ),
        migrations.AddField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(default='', verbose_name='Content'),
            preserve_default=False,
        ),
    ]