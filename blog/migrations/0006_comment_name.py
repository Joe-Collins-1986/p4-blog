# Generated by Django 3.2.16 on 2023-01-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='none', max_length=80),
        ),
    ]
