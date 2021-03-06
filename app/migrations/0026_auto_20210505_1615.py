# Generated by Django 3.1.4 on 2021-05-05 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20210505_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
