from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Booking)
admin.site.register(Menu)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
