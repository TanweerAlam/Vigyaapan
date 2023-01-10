# Generated by Django 3.2.16 on 2023-01-09 14:53

from django.db import migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('jobs', '0007_auto_20230104_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]