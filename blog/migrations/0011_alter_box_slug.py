# Generated by Django 3.2.16 on 2023-01-11 18:43

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_box_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='slug',
            field=models.SlugField(default=builtins.id, max_length=200),
        ),
    ]
