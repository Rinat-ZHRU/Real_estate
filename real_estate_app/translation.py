from modeltranslation.translator import register, TranslationOptions
from real_estate_app.models import City, Category, Advantage, Project, ObjectRealEst


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('name_city', 'description_city')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name_category', 'description_category')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('name_pr', 'description_pr', 'construction_technology', 'apartments_renovation')


@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ('advantage',)


@register(ObjectRealEst)
class RealEstTranslationOptions(TranslationOptions):
    fields = ('name', 'address', 'description', 'category', 'city')


