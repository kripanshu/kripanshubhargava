# Generated by Django 2.1 on 2018-08-04 23:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks_to_code', '0014_auto_20180804_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tinymce',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
