# Generated by Django 4.0.6 on 2022-08-24 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advantage', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущество')),
                ('advantage_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущество')),
                ('advantage_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Преимущество')),
            ],
            options={
                'verbose_name': 'Преимущество объекта',
                'verbose_name_plural': 'Преимущества объекта',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=100, verbose_name='Название категории')),
                ('name_category_ru', models.CharField(max_length=100, null=True, verbose_name='Название категории')),
                ('name_category_en', models.CharField(max_length=100, null=True, verbose_name='Название категории')),
                ('description_category', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('description_category_ru', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('description_category_en', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('image_category', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name_category'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=100, verbose_name='Название города')),
                ('name_city_ru', models.CharField(max_length=100, null=True, verbose_name='Название города')),
                ('name_city_en', models.CharField(max_length=100, null=True, verbose_name='Название города')),
                ('description_city', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_city_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_city_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image_city', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Населенный пункт',
                'verbose_name_plural': 'Населенные пункты',
                'ordering': ['name_city'],
            },
        ),
        migrations.CreateModel(
            name='ObjectRealEst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.CharField(max_length=25, null=True, verbose_name='Лот')),
                ('name', models.CharField(max_length=250, verbose_name='Название объекта')),
                ('name_ru', models.CharField(max_length=250, null=True, verbose_name='Название объекта')),
                ('name_en', models.CharField(max_length=250, null=True, verbose_name='Название объекта')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес объекта')),
                ('address_ru', models.CharField(max_length=250, null=True, verbose_name='Адрес объекта')),
                ('address_en', models.CharField(max_length=250, null=True, verbose_name='Адрес объекта')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Цена')),
                ('price_ru', models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Цена')),
                ('price_en', models.DecimalField(decimal_places=2, max_digits=12, null=True, verbose_name='Цена')),
                ('square', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Площадь')),
                ('number_of_rooms', models.PositiveSmallIntegerField(verbose_name='Количество комнат')),
                ('number_of_bathrooms', models.PositiveSmallIntegerField(verbose_name='Количество санузлов')),
                ('floor', models.PositiveSmallIntegerField(verbose_name='Этаж')),
                ('advantage', models.ManyToManyField(blank=True, to='real_estate_app.advantage', verbose_name='Преимущества объекта')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.category', verbose_name='Категория')),
                ('category_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.category', verbose_name='Категория')),
                ('category_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.category', verbose_name='Категория')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.city', verbose_name='Населенный пункт')),
                ('city_en', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.city', verbose_name='Населенный пункт')),
                ('city_ru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.city', verbose_name='Населенный пункт')),
            ],
            options={
                'verbose_name': 'Объект недвижимости',
                'verbose_name_plural': 'Объекты недвижимости',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pr', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название проекта')),
                ('name_pr_ru', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название проекта')),
                ('name_pr_en', models.CharField(blank=True, max_length=250, null=True, verbose_name='Название проекта')),
                ('description_pr', models.TextField(blank=True, null=True, verbose_name='Описание проекта')),
                ('description_pr_ru', models.TextField(blank=True, null=True, verbose_name='Описание проекта')),
                ('description_pr_en', models.TextField(blank=True, null=True, verbose_name='Описание проекта')),
                ('cadastral_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Кадастровый номер')),
                ('buildings_project', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество домов в проекте')),
                ('construction_area', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Общая площадь строительства')),
                ('number_of_storeys', models.CharField(blank=True, max_length=20, null=True, verbose_name='Этажность')),
                ('construction_technology', models.CharField(blank=True, max_length=50, null=True, verbose_name='Технология строительства')),
                ('construction_technology_ru', models.CharField(blank=True, max_length=50, null=True, verbose_name='Технология строительства')),
                ('construction_technology_en', models.CharField(blank=True, max_length=50, null=True, verbose_name='Технология строительства')),
                ('ceiling_height', models.CharField(blank=True, max_length=10, null=True, verbose_name='Высота потолка')),
                ('apartments_number', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество квартир')),
                ('apartments_rooms', models.CharField(blank=True, max_length=50, null=True, verbose_name='Комнатность квартир')),
                ('apartments_renovation', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отделка квартир')),
                ('apartments_renovation_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отделка квартир')),
                ('apartments_renovation_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отделка квартир')),
                ('apartments_area', models.CharField(blank=True, max_length=20, null=True, verbose_name='Площади квартир')),
            ],
            options={
                'verbose_name': 'Проект и его характеристики',
                'verbose_name_plural': 'Проекты и их характеристики',
            },
        ),
        migrations.CreateModel(
            name='ObjectVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='', verbose_name='Видео')),
                ('video_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video', to='real_estate_app.objectrealest', verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Видео объекта',
                'verbose_name_plural': 'Видео объекта',
            },
        ),
        migrations.AddField(
            model_name='objectrealest',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real_estate_app.project', verbose_name='Характеристики проекта'),
        ),
        migrations.CreateModel(
            name='ObjectLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layout', models.ImageField(upload_to='', verbose_name='Фото планировки')),
                ('layout_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='layout', to='real_estate_app.objectrealest', verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Фото планировки объекта',
                'verbose_name_plural': 'Фото планировки объекта',
            },
        ),
        migrations.CreateModel(
            name='ObjectImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
                ('image_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='real_estate_app.objectrealest', verbose_name='Ссылка на объект')),
            ],
            options={
                'verbose_name': 'Фото объекта',
                'verbose_name_plural': 'Фото объекта',
            },
        ),
    ]
