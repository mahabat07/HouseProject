from .models import *
from rest_framework import serializers



class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','age','username','user_role']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id','region_name']


class CitySerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ['id','city_name','region']


class DistrictSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()

    class Meta:
        model = District
        fields = ['id','district_name','city']

class PropertyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyImage
        fields = ['image']


class PropertyListSerializer(serializers.ModelSerializer):
    property_images = PropertyImageSerializer(many=True, read_only=True)
    city = serializers.StringRelatedField()


    class Meta:
        model = Property
        fields = ['id','title','price','city','property_images']

class PropertyDetailSerializer(serializers.ModelSerializer):
    property_images = PropertyImageSerializer(many=True, read_only=True)
    seller = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    district = serializers.StringRelatedField()

    class Meta:
        model = Property
        fields ='__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['id','author','rating','created_at']

class ReviewDetailSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ['id','author','seller','rating','comment','created_at']

