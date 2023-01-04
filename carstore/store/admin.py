from django.contrib import admin
from .models import *


class ad_car_Admin(admin.ModelAdmin):
    list_display = ('id', 'mark', 'mod', 'year', 'millage', 'owners', 'images', 'price', 'description', 'user_id')


admin.site.register(ad_car, ad_car_Admin)
