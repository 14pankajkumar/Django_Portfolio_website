# Generated by Django 3.1.4 on 2021-05-05 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20210123_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='DP',
            new_name='dp',
        ),
    ]
