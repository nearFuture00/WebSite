# Generated by Django 3.0.4 on 2020-03-16 16:17

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200316_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='home_text',
            field=models.TextField(max_length=5000, verbose_name='Anasayfa Yazisi'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=ckeditor.fields.RichTextField(verbose_name='Yazi'),
        ),
    ]
