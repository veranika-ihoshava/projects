from django.contrib import admin
from shop.models import User, Product, Product_group, Order, Application

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password')
    search_fields = ('name', 'login')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'name', 'price', 'count', 'group', 'show_image')
    search_fields = ('serial_number', 'name')
    list_filter = ('group',)
    raw_id_fields = ('group',)

class Product_groupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'login')

class OrderAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)
    filter_horizontal = ('products',)

class Applications(admin.ModelAdmin):
    list_display = ('username', 'surname', 'login', 'applied_date')

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_group, Product_groupAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Application, Applications)
