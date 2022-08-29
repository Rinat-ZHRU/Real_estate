from rest_framework import viewsets
from company_data_app.serializers import *


class CompanyDataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CompanyData.objects.all().order_by('id')
    serializer_class = CompanyDataSerializer


class CompanyReviewViewSet(viewsets.ModelViewSet):
    queryset = CompanyReview.objects.all().order_by('id')
    serializer_class = CompanyReviewSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all().order_by('id')
    serializer_class = ServiceSerializer


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer


class NewsReviewViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all().order_by('id')
    serializer_class = NewsSerializer


