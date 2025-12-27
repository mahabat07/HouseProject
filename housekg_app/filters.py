from django_filters import FilterSet
from .models import  Property


class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'property_type':['exact'],
            'region':['exact'],
            'district':['exact'],
            'area':['gt','lt'],
            'price':['gt','lt'],
            'rooms':['gt','lt'],
            'condition_type':['exact']
        }