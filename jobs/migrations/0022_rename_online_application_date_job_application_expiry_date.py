# Generated by Django 3.2.16 on 2023-01-28 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0021_auto_20230128_0750'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='online_application_date',
            new_name='application_expiry_date',
        ),
    ]
