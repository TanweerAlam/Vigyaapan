# Generated by Django 3.2.16 on 2023-01-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_remove_job_dept_of_ministry'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='jobs_image/%Y/%m/'),
        ),
    ]
