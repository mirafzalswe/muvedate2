# Generated by Django 4.2 on 2024-03-16 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_sort'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tutorials', to='pages.page'),
        ),
        migrations.AlterField(
            model_name='video',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='pages.page'),
        ),
    ]
