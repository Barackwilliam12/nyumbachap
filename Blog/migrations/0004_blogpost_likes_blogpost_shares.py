# Generated by Django 5.1.1 on 2024-09-24 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blogpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='likes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='shares',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
