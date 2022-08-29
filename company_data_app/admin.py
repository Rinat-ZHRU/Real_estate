from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from company_data_app.models import CompanyReview, Employee, Service, News, CompanyData


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    fields = ('name', 'description', 'date')


@admin.register(CompanyData)
class CompanyDataAdmin(TranslationAdmin):
    fields = ('name', 'address', 'description', 'tel_1', 'tel_2', 'tel_3', 'email', 'image')


@admin.register(Employee)
class EmployeeAdmin(TranslationAdmin):
    fields = ('full_name', 'job_title', 'tel', 'email', 'description', 'photo')


@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    fields = ('name', 'description')


@admin.register(CompanyReview)
class CompanyReviewAdmin(TranslationAdmin):
    fields = ('name_user', 'tel', 'email', 'review')