# Generated by Django 3.2.16 on 2023-01-13 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_visit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='visit',
            new_name='status',
        ),
    ]