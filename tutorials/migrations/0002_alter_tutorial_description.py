# Generated by Django 3.2.9 on 2023-08-18 02:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
