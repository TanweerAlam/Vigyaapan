# Generated by Django 3.2.16 on 2023-01-19 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_job_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ministry',
            old_name='ministry',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='state',
            old_name='state',
            new_name='name',
        ),
    ]
