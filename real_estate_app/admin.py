from django.contrib import admin
from django.contrib.admin import TabularInline
from modeltranslation.admin import TranslationAdmin
from real_estate_app.models import City, Category, Project, ObjectRealEst, \
    ObjectImage, ObjectVideo, ObjectLayout, Advantage


class ImageAdminInline(TabularInline):
    extra = 1
    model = ObjectImage


class VideoAdminInline(TabularInline):
    extra = 1
    model = ObjectVideo


class LayoutAdminInline(TabularInline):
    extra = 1
    model = ObjectLayout


@admin.register(City)
class CityAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['id', 'name_city_ru', 'name_city_en']



@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['id', 'name_category_ru', 'name_category_en']


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['id', 'name_pr_ru', 'name_pr_en', 'cadastral_number', 'buildings_project', 'construction_area',
                    'number_of_storeys', 'apartments_renovation_ru', 'apartments_area']


@admin.register(Advantage)
class AdvantageAdmin(TranslationAdmin):
    readonly_fields = ['id']
    list_display = ['id', 'advantage_ru', 'advantage_en']


@admin.register(ObjectRealEst)
class ProductModelAdmin(TranslationAdmin):
    inlines = (ImageAdminInline, VideoAdminInline, LayoutAdminInline)
    list_display = ['id', 'name', 'price', 'square']  # для отображения в просмотре
    # для отображения при заполнении
    fields = ('id', 'lot', 'name', 'address', 'description', 'price', 'square', 'number_of_rooms',
              'number_of_bathrooms', 'floor', 'category_ru', 'city_ru', 'project', 'advantage')



