from django.contrib import admin
from .models import Payment, Order, OrderProduct
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number","payment","first_name","last_name","email","phone","order_note","is_ordered","status")
    list_filter = ("status",)
    list_display_links = ("order_number","first_name","last_name",)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ("payment_id","payment_method","user","status","created_at")
    list_filter = ("payment_method",)
    list_display_links = ("payment_id","payment_method",)

admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct)
