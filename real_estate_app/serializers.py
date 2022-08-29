from real_estate_app.models import Category, City, ObjectRealEst, \
    Advantage, ObjectImage, ObjectVideo, ObjectLayout, Project
from rest_framework import serializers

# Сериализаторы нужны для преобразования типов данных Python в JSON и наоборот


class AdvantageSerializer(serializers.ModelSerializer):
    """Приемущества объекта"""

    class Meta:
        model = Advantage
        fields = '__all__'  # все поля


class ProjectSerializer(serializers.ModelSerializer):
    """Характеристики проекта"""

    class Meta:
        model = Project
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    """Фото объекта"""

    class Meta:
        model = ObjectImage
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    """Фото объекта"""

    class Meta:
        model = ObjectVideo
        fields = '__all__'


class LayoutSerializer(serializers.ModelSerializer):
    """Фото планировки объекта"""

    class Meta:
        model = ObjectLayout
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    """Список городов"""

    class Meta:
        model = City
        fields = '__all__'  # все поля

class CategorySerializer(serializers.ModelSerializer):
    """Список категорий"""

    class Meta:
        model = Category
        fields = '__all__'

class ObjectSerializer(serializers.ModelSerializer):
    """Список объектов недвижимости"""
    category = CategorySerializer()
    city = CitySerializer()
    advantage = AdvantageSerializer()
    project = ProjectSerializer(many=True)
    image = ImageSerializer(many=True)
    video = VideoSerializer(many=True)
    layout = LayoutSerializer(many=True)

    class Meta:
        model = ObjectRealEst
        fields = ['id', 'lot', 'name', 'address', 'price', 'number_of_rooms', 'number_of_bathrooms',
                  'floor', 'city', 'category', 'advantage', 'project', 'image', 'video', 'layout']


    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     serializers_user = UserSerializer(instance=instance.user)
    #     response["user"] = serializers_user.data
    #     return response