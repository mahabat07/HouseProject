from .views import (UserProfileListAPIView,UserProfileDetailAPIView,
                    RegionViewSet,CityViewSet,DistrictViewSet,
                    PropertyListAPIView,PropertyDetailAPIView
                   ,ReviewListAPIView,ReviewDetailAPIView,RegisterView,LoginView,LogoutView)
from rest_framework import routers
from django.urls import path, include


router = routers.SimpleRouter()
router.register(r'region/', RegionViewSet)
router.register(r'city/', CityViewSet)
router.register(r'district/',DistrictViewSet)



urlpatterns = [
    path('',include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('property/',PropertyListAPIView.as_view(),name='property_list'),
    path('property/<int:pk>/',PropertyDetailAPIView.as_view(), name='property_detail'),
    path('review/',ReviewListAPIView.as_view(),name='review_list'),
    path('review/<int:pk>/',ReviewDetailAPIView.as_view(),name='review_detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')


]