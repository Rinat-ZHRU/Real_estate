# Generated by Django 4.0.6 on 2022-08-25 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_app', '0004_alter_objectimage_image_alter_objectlayout_layout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='objectrealest',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='objectrealest',
            name='price_ru',
        ),
        migrations.AlterField(
            model_name='objectrealest',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.project', verbose_name='Характеристики проекта'),
        ),
    ]
