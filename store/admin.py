from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGalery, MyColor, BaseProduct, BaseProductGalery, ProductBaseProductItems
import admin_thumbnails
from django.utils.html import format_html
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGaleryInline(admin.TabularInline):
    model = ProductGalery
    extra = 0

@admin_thumbnails.thumbnail('image')
class BaseProductGaleryInline(admin.TabularInline):
    model = BaseProductGalery
    extra = 0

class ProductBaseProductInline(admin.TabularInline):
    model = ProductBaseProductItems
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','default_base_product','price','image','category','user','created_date','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

    # inlines = [ProductGaleryInline]
    inlines = [ProductBaseProductInline,ProductGaleryInline]

class ProductBaseProductItemsAdmin(admin.ModelAdmin):
    list_display = ('product','base_product_gallery','is_default')
    



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
    

class BaseProductGaleryAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" height="30" style="border-radius:0%">'.format(object.image.url))

    thumbnail.short_description = 'Base Product Picture'

    list_display = ('thumbnail','image')


class MyColorAdmin(admin.ModelAdmin):
    list_display = ('color_name','color_hexa')

class MyBaseProduct(admin.ModelAdmin):
    list_display = ('base_product_name',)
    inlines = [BaseProductGaleryInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductBaseProductItems, ProductBaseProductItemsAdmin)
admin.site.register(Variation, VariationsAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGalery, ProductGaleryAdmin)
admin.site.register(MyColor, MyColorAdmin)
admin.site.register(BaseProduct, MyBaseProduct)
admin.site.register(BaseProductGalery, BaseProductGaleryAdmin)

