from django.contrib import admin

from .models import Ustadz, Santri, Kelas

class UstadzAdmin(admin.ModelAdmin):
    list_display = ('nip','nama', 'alamat', 'tanggal_lahir', 'email', 'nomor_telepon', 'mulai_bergabung')
    list_filter = ("jenis_kelamin","mulai_bergabung",)
    list_display_links = ("nip","nama",)
    list_per_page = 20

class KelasAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama', 'is_active', 'wali_kelas')
    list_per_page = 20
    list_display_links = ("kode","nama",)
    list_filter = ('wali_kelas','is_active')

class SantriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'alamat', 'tempat_lahir', 'tanggal_lahir', 'jenis_kelamin', 'kelas', 'is_active', 'orang_tua')
    list_per_page = 20

admin.site.register(Kelas, KelasAdmin)
admin.site.register(Ustadz, UstadzAdmin)
admin.site.register(Santri, SantriAdmin)
