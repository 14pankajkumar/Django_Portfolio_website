# Generated by Django 3.1.5 on 2021-01-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210111_1810'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('skill', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=10)),
            ],
        ),
    ]
