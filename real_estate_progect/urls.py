from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


# urlpatterns = i18n_patterns(
#     path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
# )


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),  # для проверки и тестирования наших api через web-интерфейс
    path('admin/', admin.site.urls),
    path('real_estate/', include('real_estate_app.urls')),
    path('company_data/', include('company_data_app.urls')),
] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    # path('admin/', admin.site.urls),
    path('real_estate/', include('real_estate_app.urls')),
    path('company_data/', include('company_data_app.urls')),
)

if settings.DEBUG:  # если дебаг режим включен, то файлы медиа будет обрабатывать наш ДЖАНГО
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
