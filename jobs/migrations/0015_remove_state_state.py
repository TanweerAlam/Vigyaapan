# Generated by Django 3.2.16 on 2023-01-19 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_state_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='state',
        ),
    ]