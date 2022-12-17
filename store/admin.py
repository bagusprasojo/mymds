from django.contrib import admin
from .models import Product, Variation, ReviewRating
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','created_date','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product, ProductAdmin)

class VariationsAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active','created_date','modified_date')
    list_editable = ('is_active',)
    list_filter = ('product','variation_category','variation_value','is_active')
    # prepopulated_fields = {'slug':('product_name',)}

class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('subject','product','review','rating','user','status','ip','created_at','updated_at')
    list_editable = ('status',)
    list_filter = ('status','rating',)

admin.site.register(Variation, VariationsAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
