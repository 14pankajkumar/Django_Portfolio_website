# Generated by Django 3.1.5 on 2021-01-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210111_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('title_url', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
