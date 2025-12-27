from .models import (UserProfile,Region,City,District,Property,Review)
from .serializers import (UserProfileListSerializer,UserProfileDetailSerializer,
                          RegionSerializer,CitySerializer,
                          DistrictSerializer,PropertyListSerializer,
                          PropertyDetailSerializer,
                          ReviewListSerializer,ReviewDetailSerializer,
                          UserProfileRegisterSerializer,LoginSerializer)
from rest_framework import viewsets,generics,status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import  PropertyFilter
from rest_framework.filters import  SearchFilter,OrderingFilter
from .pagination import  PropertyPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = UserProfileRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)




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
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['property_type','region','district','area','price','rooms','condition_type']
    filterset_class = PropertyFilter
    search_fields = ['is_active']
    ordering_fields = ['price','is_active']
    pagination_class = PropertyPagination
    permission_classes = [IsAuthenticated]


class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertyDetailSerializer


class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer

class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer




