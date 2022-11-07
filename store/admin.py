from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(SaleHistory)
admin.site.register(Cart_products)