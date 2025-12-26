from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.core.validators import  MinValueValidator , MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(65)],
                                           null= True , blank= True)
    phone_number = PhoneNumberField(null= True , blank= True)
    photo = models.ImageField(upload_to= 'user_images',null=True , blank= True)
    ROLE_CHOICES = (
        ('seller', 'selver'),
        ('buyer', 'buyer'))
    user_role = models.CharField(choices=ROLE_CHOICES,max_length= 16,default='buyer')

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class Region(models.Model):
    region_name = models.CharField(max_length= 65,unique= True)


    def __str__(self):
        return self.region_name


class City(models.Model):
    city_name = models.CharField(max_length= 100)
    region = models.ForeignKey(Region,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.city_name},{self.region}'


class District(models.Model):
    district_name = models.CharField(max_length= 100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.district_name},{self.city}'


class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    PROPERTY_TYPE_CHOICES = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('land', 'land'),
        ('commercial', 'commercial'),
        ('garage', 'garage'))
    property_type = models.CharField(choices=PROPERTY_TYPE_CHOICES,max_length= 20)
    region = models.ForeignKey(Region,on_delete= models.CASCADE)
    city = models.ForeignKey(City,on_delete= models.CASCADE)
    district = models.ForeignKey(District,on_delete= models.CASCADE)
    address = models.CharField(max_length= 100,blank= True)
    area = models.DecimalField(max_digits=10,decimal_places=2)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    rooms = models.PositiveIntegerField(null=True,blank=True)
    floor = models.PositiveIntegerField(null=True, blank=True)
    total_floors = models.PositiveIntegerField(null=True,blank=True)
    CONDITION_CHOICES = (
        ('basic', 'basic'),
        ('renovated', 'renovated'),
        ('euro', 'euro'),
        ('designer', 'designer'),
        ('furniture', 'furniture'),
        ('appliances', 'appliances'))
    condition_type = models.CharField(choices=CONDITION_CHOICES,max_length= 25)
    seller = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, verbose_name='Активно')

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images')

    def __str__(self):
        return f'{self.image},{self.property}'


class Review(models.Model):
    author = models.ForeignKey(UserProfile,on_delete= models.CASCADE,related_name='reviews_given')
    seller = models.ForeignKey(UserProfile,on_delete= models.CASCADE,related_name='reviews_received')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                          MaxValueValidator(5)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.author},{self.seller} , {self.rating}'








