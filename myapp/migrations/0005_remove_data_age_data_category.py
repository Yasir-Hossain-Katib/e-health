# Generated by Django 4.1.2 on 2022-12-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_data_patient_delete_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='age',
        ),
        migrations.AddField(
            model_name='data',
            name='category',
            field=models.CharField(default='hello', max_length=100),
            preserve_default=False,
        ),
    ]
