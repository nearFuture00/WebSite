# Generated by Django 3.0.4 on 2020-03-16 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_post_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_upload',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
