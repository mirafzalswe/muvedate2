# Generated by Django 4.2 on 2024-03-17 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20240316_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='content',
        ),
        migrations.RemoveField(
            model_name='page',
            name='video',
        ),
    ]
