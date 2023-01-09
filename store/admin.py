from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGalery, MyColor
import admin_thumbnails
from django.utils.html import format_html
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGaleryInline(admin.TabularInline):
    model = ProductGalery
    extra = 0



class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','created_date','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

    inlines = [ProductGaleryInline]

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

class ProductGaleryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" height="30" style="border-radius:0%">'.format(object.image.url))

    thumbnail.short_description = 'Product Picture'

    list_display = ('thumbnail','image')

class MyColorAdmin(admin.ModelAdmin):
    list_display = ('color_name','color_hexa')

admin.site.register(Variation, VariationsAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGalery, ProductGaleryAdmin)
admin.site.register(MyColor, MyColorAdmin)
