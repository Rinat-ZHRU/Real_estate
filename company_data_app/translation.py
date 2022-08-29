from modeltranslation.translator import register, TranslationOptions
from company_data_app.models import News, Employee, Service, CompanyReview, CompanyData


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('full_name', 'job_title', 'description')


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(CompanyReview)
class CompanyReviewTranslationOptions(TranslationOptions):
    fields = ('name_user', 'review')


@register(CompanyData)
class CompanyDataTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'description')