from .models import UserProfile , Region, City, District, Property, Review
from modeltranslation.translator import TranslationOptions,register


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('first_name','last_name','username',)

@register(Region)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('region_name',)

@register(City)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('city_name',)

@register(District)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('district_name',)



@register(Property)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('title','description')

@register(Review)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('comment',)


