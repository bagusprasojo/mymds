from django.contrib import admin
from .models import COA
from .models import AP

class COAAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama', 'jenis','account_induk', 'is_akun_kas')
    list_per_page = 20

    
class APAdmin(admin.ModelAdmin):
    list_display = ('kelas_model', 'no_bukti_transaksi', 'tgl_transaksi', 'nominal', 'tgl_jatuh_tempo', 'terbayar', 'sisa', 'stakeholder', 'user_create', 'user_modify', 'date_create')
    list_per_page = 20

admin.site.register(AP, APAdmin)
admin.site.register(COA, COAAdmin)
