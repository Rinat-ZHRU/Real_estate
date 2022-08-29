from django.db import models


class News(models.Model):
    """Новости"""
    name = models.CharField('Название новости', max_length=250)
    description = models.TextField('Текст новости', null=True, blank=True)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'


class Employee(models.Model):
    """Сотрудники"""
    full_name = models.CharField('ФИО Сотрудника', max_length=255)
    job_title = models.CharField('Должность', max_length=255)
    tel = models.CharField('Телефон', max_length=20)
    email = models.EmailField(blank=True, null=True)
    description = models.CharField('Краткая информация о сотруднике', max_length=255)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class CompanyData(models.Model):
    """Данные о компании"""
    name = models.CharField('Название', max_length=50)
    address = models.CharField('Адрес', max_length=100)
    # longitude = models.CharField('Долгота местонахождения', max_length=20)
    # latitude = models.CharField('Широта местонахождения', max_length=20)
    description = models.TextField('Общая информация')
    tel_1 = models.CharField('Тел_1', max_length=50, blank=True, null=True)
    tel_2 = models.CharField('Тел_2', max_length=50, blank=True, null=True)
    tel_3 = models.CharField('Тел_3', max_length=50, blank=True, null=True)
    email = models.EmailField('Электронная почта', blank=True, null=True)
    image = models.ImageField('Фото', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Данные о компании'
        verbose_name_plural = 'Данные о компании'


class Service(models.Model):
    """Услуги"""
    name = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предоставляемые услуги'
        verbose_name_plural = 'Предоставляемые услуги'


class CompanyReview(models.Model):
    """Отзывы о компании"""
    name_user = models.CharField('Имя оставляющего отзыв', max_length=100)
    tel = models.CharField('Телефон', blank=True, null=True, max_length=50)
    email = models.EmailField('Электронная почта', blank=True, null=True)
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.name_user

    class Meta:
        verbose_name = 'Отзывы о компании'
        verbose_name_plural = 'Отзывы о компании'

