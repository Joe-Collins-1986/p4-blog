# Generated by Django 3.2.16 on 2023-01-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_rename_visit_visit_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='status',
            field=models.CharField(default='not_visited', max_length=50),
        ),
    ]
