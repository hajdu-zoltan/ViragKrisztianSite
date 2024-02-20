from django.contrib import admin
from . models import User, Description, Image, ImageCategory, Video, PriceOffers

# Register your models here.
admin.site.register(User)
admin.site.register(Description)
admin.site.register(Image)
admin.site.register(ImageCategory)
admin.site.register(Video)
admin.site.register(PriceOffers)

