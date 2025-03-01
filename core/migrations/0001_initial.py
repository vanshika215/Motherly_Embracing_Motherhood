# Generated by Django 4.2.11 on 2024-03-14 17:34

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, max_length=100000, null=True)),
            ],
        ),
    ]
