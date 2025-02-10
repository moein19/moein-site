# Generated by Django 5.1.6 on 2025-02-09 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/bloggers/%Y/%m/%d/')),
                ('birth_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('register_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('posts_count', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
    ]
