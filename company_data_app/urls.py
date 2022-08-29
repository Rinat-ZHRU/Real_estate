from django.urls import path
from company_data_app.views import *
from rest_framework import routers

urlpatterns = [
    path('', CompanyDataViewSet.as_view({'get': 'list'}), name='Данные организации'),
    path('employee', EmployeeViewSet.as_view({'get': 'list'}), name='Сотрудники'),
    path('service', ServiceViewSet.as_view({'get': 'list'}), name='Услуги'),
    path('news', NewsReviewViewSet.as_view({'get': 'list'}), name='Новости'),
    path('review', CompanyReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name='Отзывы'),
    path('review/<int:pk>', CompanyReviewViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
        }
        ),
         name='Отзывы детально'
    ),
]