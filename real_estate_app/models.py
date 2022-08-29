from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    """ГОРОД"""
    name_city = models.CharField('Название города', max_length=100)
    description_city = models.TextField('Описание', null=True, blank=True)
    image_city = models.ImageField('Фото', null=True, blank=True)

    class Meta:
        ordering = ['name_city']
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'

    def __str__(self):
        return f'{self.name_city}'


class Category(models.Model):
    """Категории недвижимости"""
    name_category = models.CharField('Название категории', max_length=100)
    description_category = models.TextField('Описание категории', null=True, blank=True)
    image_category = models.ImageField('Фото', null=True, blank=True)

    class Meta:
        ordering = ['name_category']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name_category}'


class Advantage(models.Model):
    """Преимущества объекта"""
    advantage = models.CharField('Преимущество', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Преимущество объекта'
        verbose_name_plural = 'Преимущества объекта'

    def __str__(self):
        return f'{self.advantage}'


class Project(models.Model):
    """Строящиеся проекты"""
    name_pr = models.CharField('Название проекта', max_length=250, null=True, blank=True)
    description_pr = models.TextField('Описание проекта', null=True, blank=True)
    cadastral_number = models.CharField('Кадастровый номер', max_length=20, null=True, blank=True)
    buildings_project = models.PositiveSmallIntegerField('Количество домов в проекте', null=True, blank=True)
    construction_area = models.PositiveSmallIntegerField('Общая площадь строительства', null=True, blank=True)
    number_of_storeys = models.CharField('Этажность', max_length=20, null=True, blank=True)
    construction_technology = models.CharField('Технология строительства', max_length=50, null=True, blank=True)
    ceiling_height = models.CharField('Высота потолка', max_length=10, null=True, blank=True)
    apartments_number = models.PositiveSmallIntegerField('Количество квартир', null=True, blank=True)
    apartments_rooms = models.CharField('Комнатность квартир', max_length=50, null=True, blank=True)
    apartments_renovation = models.CharField('Отделка квартир', max_length=100, null=True, blank=True)
    apartments_area = models.CharField('Площади квартир', max_length=20, null=True, blank=True)
    image_pr = models.ImageField(verbose_name='Фото', null=True, blank=True)
    video_pr = models.FileField('Видео', null=True, blank=True)


    class Meta:
        verbose_name = 'Проект и его характеристики'
        verbose_name_plural = 'Проекты и их характеристики'

    def __str__(self):
        return f'{self.name_pr}'


class ObjectRealEst(models.Model):
    """Объект недвижимости"""
    lot = models.CharField('Лот', max_length=25, null=True)
    name = models.CharField('Название объекта', max_length=250)
    address = models.CharField('Адрес объекта', max_length=250)
    description = models.TextField('Описание', null=True, blank=True)
    price = models.DecimalField('Цена', max_digits=12, decimal_places=2)
    square = models.DecimalField('Площадь', max_digits=6, decimal_places=2)
    number_of_rooms = models.PositiveSmallIntegerField('Количество комнат')
    number_of_bathrooms = models.PositiveSmallIntegerField('Количество санузлов')
    floor = models.PositiveSmallIntegerField('Этаж')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name='Населенный пункт', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, verbose_name='Характеристики проекта', on_delete=models.CASCADE, null=True, blank=True)
    advantage = models.ManyToManyField(Advantage, verbose_name='Преимущества объекта', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

    def __str__(self):
        return f'{self.name}'

    # def get_absulute_url(self):  # для отображения в браузере "возврат ....."
    #     return reverse('')


class ObjectImage(models.Model):
    """Фото объекта"""
    image = models.ImageField(verbose_name='Фото', null=True, blank=True)
    image_link = models.ForeignKey(ObjectRealEst, verbose_name='Ссылка на объект', on_delete=models.CASCADE,
                                   related_name='image')

    class Meta:
        verbose_name = 'Фото объекта'
        verbose_name_plural = 'Фото объекта'


class ObjectVideo(models.Model):
    """Видео объекта"""
    video = models.FileField('Видео', null=True, blank=True)
    video_link = models.ForeignKey(ObjectRealEst, verbose_name='Ссылка на видео', on_delete=models.CASCADE,
                                   related_name='video')

    class Meta:
        verbose_name = 'Видео объекта'
        verbose_name_plural = 'Видео объекта'


class ObjectLayout(models.Model):
    """Фото планировки объекта"""
    layout = models.ImageField(verbose_name='Фото планировки', null=True, blank=True)
    layout_link = models.ForeignKey(ObjectRealEst, verbose_name='Ссылка', on_delete=models.CASCADE,
                                    related_name='layout')

    class Meta:
        verbose_name = 'Фото планировки объекта'
        verbose_name_plural = 'Фото планировки объекта'

