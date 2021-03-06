from django.contrib import admin
from shop.models import User, Product, Product_group, Order, Application
from shop.models import News

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

class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('login', 'username', 'surname', 'applied_date', 'checked')
    list_display = ('login', 'username', 'surname', 'applied_date')

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

class NewsAdmin(admin.ModelAdmin):
    list_display = 'slug', 'name', 'body', 'show_image', 'publication_start_at', 'publication_end_at'

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_group, Product_groupAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(News, NewsAdmin)
