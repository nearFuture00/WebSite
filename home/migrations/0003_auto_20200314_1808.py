# Generated by Django 3.0.4 on 2020-03-14 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200314_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='home_text',
            field=models.TextField(max_length=5000, verbose_name='Anasayfa Yazisi'),
        ),
    ]
