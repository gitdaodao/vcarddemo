# Generated by Django 2.0.6 on 2018-07-04 06:43

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180703_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='正文'),
        ),
    ]
