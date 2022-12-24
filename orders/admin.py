from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 0
    readonly_fields=("payment","user","product","quantity","product_price","ordered")

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number","payment","first_name","last_name","email","phone","order_note","is_ordered","status","created_at")
    list_filter = ("status","is_ordered")
    list_display_links = ("order_number","first_name","last_name",)
    list_per_page = 20
    search_fields = ("order_number","first_name","last_name","email",)

    inlines = [OrderProductInline]

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_id","payment_method","user","status","created_at")
    list_filter = ("payment_method",)
    list_display_links = ("payment_id","payment_method",)
    list_per_page = 20

    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # user = models.ForeignKey(Account, on_delete=models.SET_NULL, blank=True, null=True)
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    # color = models.CharField(max_length=50)
    # size = models.CharField(max_length=50)
    # quantity = models.IntegerField()
    # product_price = models.FloatField()
    # ordered = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ("order","user","payment","quantity","created_at")
    list_per_page = 20
    # list_filter = ("payment_method",)
    # list_display_links = ("payment_id","payment_method",)

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
