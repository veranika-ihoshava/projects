from django.contrib import admin
from shop.models import User, Product, Product_group, Order

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password')
    search_fields = ('name', 'login')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'price', 'count', 'group')
    search_fields = ('serial_number', 'name')
    list_filter = ('group',)
    raw_id_fields = ('group',)

class Product_groupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'login')

class OrderAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    filter_horizontal = ('products',)

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_group, Product_groupAdmin)
admin.site.register(Order, OrderAdmin)