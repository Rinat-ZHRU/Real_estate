from django.urls import path
from real_estate_app.views import CityViewSet, CategoryViewSet, ObjectViewSet, ProjectViewSet

urlpatterns = [
    path('city/', CityViewSet.as_view({'get': 'list'}), name='Список городов'),
    path('category/', CategoryViewSet.as_view({'get': 'list'}), name='Список категорий'),
    path('project/', ProjectViewSet.as_view({'get': 'list'}), name='Характеристики проекта'),
    path('object/', ObjectViewSet.as_view({'get': 'list'}), name='Объекты недвижимости'),
    path('object/<int:pk>/', ObjectViewSet.as_view({'get': 'retrieve'}), name='Детализация объекта недвижимости'),
]