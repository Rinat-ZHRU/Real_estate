from company_data_app.models import *
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):
    """Список городов"""
    class Meta:
        model = News
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """Список городов"""
    class Meta:
        model = Employee
        fields = '__all__'


class CompanyDataSerializer(serializers.ModelSerializer):
    """Список городов"""
    class Meta:
        model = CompanyData
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    """Список городов"""
    class Meta:
        model = Service
        fields = '__all__'


class CompanyReviewSerializer(serializers.ModelSerializer):
    """Список городов"""
    class Meta:
        model = CompanyReview
        fields = '__all__'