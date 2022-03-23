from django.contrib import admin
from .models.product import Product,Post1
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.pagination import Post


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'desc', 'publish_date','image']

admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
# admin.site.register(Post, AdminPost)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Post1)
# admin.site.register(Post)


