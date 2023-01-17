# Generated by Django 3.2.16 on 2023-01-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_auto_20230117_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital',
            field=models.CharField(default=None, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='currency',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='country',
            name='language',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='country',
            name='region',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
