# Generated by Django 3.2.16 on 2023-01-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_auto_20230126_0635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'get_latest_by': '-created_on', 'ordering': ['-created_on'], 'verbose_name': 'Job', 'verbose_name_plural': 'Jobs'},
        ),
        migrations.AlterField(
            model_name='job',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]