from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'age', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


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

