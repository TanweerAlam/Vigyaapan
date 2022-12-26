# Generated by Django 3.2.16 on 2022-12-14 08:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20221210_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='isPublished',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='job',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]