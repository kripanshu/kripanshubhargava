# Generated by Django 2.0.7 on 2018-08-04 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacks_to_code', '0013_auto_20180804_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='tinymce',
            field=models.TextField(blank=True, max_length=4000),
        ),
    ]