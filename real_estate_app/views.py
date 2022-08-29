from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from real_estate_app.models import City, Category, Advantage, Project, ObjectRealEst, ObjectVideo, ObjectLayout, ObjectImage
from real_estate_app.serializers import *


"""
CRUD
C = create
R = read
U = update
D = delete
"""


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all().order_by('id')
    serializer_class = CitySerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class ObjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectRealEst.objects.all().order_by('id')
    serializer_class = ObjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    lookup_field = 'pk'
    ordering_fields = ['name']
    search_fields = ['address']
    filterset_fields = ['category']


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer


class AdvantageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Advantage.objects.all().order_by('id')
    serializer_class = AdvantageSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectImage.objects.all().order_by('id')
    serializer_class = ImageSerializer


class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectVideo.objects.all().order_by('id')
    serializer_class = VideoSerializer


class LayoutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ObjectLayout.objects.all().order_by('id')
    serializer_class = LayoutSerializer
