# Generated by Django 3.0.4 on 2020-03-16 16:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_post_image_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='home_text',
            field=ckeditor.fields.RichTextField(max_length=5000, verbose_name='Anasayfa Yazisi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_upload',
            field=models.FileField(blank=True, upload_to='', verbose_name='Resim secin'),
        ),
    ]
