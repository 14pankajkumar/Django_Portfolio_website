# Generated by Django 3.1.5 on 2021-01-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('head', models.TextField()),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
