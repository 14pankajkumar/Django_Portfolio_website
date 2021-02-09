# Generated by Django 3.1.5 on 2021-01-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_application_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='slug',
            field=models.SlugField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='startup',
            name='slug',
            field=models.SlugField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='web',
            name='slug',
            field=models.SlugField(max_length=20, null=True, unique=True),
        ),
    ]