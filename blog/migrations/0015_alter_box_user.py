# Generated by Django 3.2.16 on 2023-01-12 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0014_box'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boxes', to=settings.AUTH_USER_MODEL),
        ),
    ]
