# Generated by Django 3.2.16 on 2023-01-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0009_alter_visit_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_map', to='map.country'),
        ),
    ]