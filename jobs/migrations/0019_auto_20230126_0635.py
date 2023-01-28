# Generated by Django 3.2.16 on 2023-01-26 06:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20230125_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='extra_info_box_1',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='extra_info_box_2',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
