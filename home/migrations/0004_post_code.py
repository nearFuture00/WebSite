# Generated by Django 3.0.4 on 2020-03-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200314_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='code',
            field=models.TextField(blank=True, verbose_name='Kod'),
        ),
    ]
