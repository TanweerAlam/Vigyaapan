# Generated by Django 3.2.16 on 2023-01-28 07:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0020_auto_20230127_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='admit_card_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='application_expiry_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='correction_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='exam_date',
        ),
        migrations.RemoveField(
            model_name='job',
            name='fee_last_date',
        ),
        migrations.AddField(
            model_name='job',
            name='important_dates',
            field=tinymce.models.HTMLField(default='\n    Application Begin : Unannounced\n    Last Date for Apply Online : Unannounced\n    Pay Exam Fee Last Date : Unannounced\n    Admit Card Date : Unannounced\n    Exam Date : Unannounced\n    '),
        ),
    ]
