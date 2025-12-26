from .models import (UserProfile,Region,City,District,Property,Review)
from .serializers import (UserProfileListSerializer,UserProfileDetailSerializer,
                          RegionSerializer,CitySerializer,
                          DistrictSerializer,PropertyListSerializer,
                          PropertyDetailSerializer,
                          ReviewListSerializer,ReviewDetailSerializer)
from rest_framework import viewsets,generics

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyListSerializer

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer




