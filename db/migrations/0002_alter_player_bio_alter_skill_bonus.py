# Generated by Django 4.0.2 on 2023-12-21 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bio',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skill',
            name='bonus',
            field=models.CharField(max_length=255),
        ),
    ]