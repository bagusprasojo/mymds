from django.db import models
from kesantrian.models import StakeHolder
from accounts.models import Account
from datetime import datetime

class COA(models.Model):
    JENIS_CHOICES = [
        ('AKTIVA', 'Aktiva'),
        ('BIAYA', 'Biaya'),
        ('HPP', 'Harga Pokok Penjualan'),
        ('PENDAPATAN', 'Pendapatan'),
        ('PASIVA', 'Pasiva'),
    ]

    kode = models.CharField(max_length=10, unique=True)
    nama = models.CharField(max_length=255)
    account_induk = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    jenis = models.CharField(max_length=10, choices=JENIS_CHOICES)
    is_akun_kas = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_modify = models.DateTimeField(auto_now=True, null=True)
    user_create = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='coa_created', null=True)
    user_modify = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='coa_modified', null=True)


    class Meta:
        verbose_name = 'COA'
        verbose_name_plural = 'COAs'

    def __str__(self):
        return self.kode + ' - ' + self.nama


class AP(models.Model):
    id_transaksi = models.IntegerField()
    kelas_model = models.CharField(max_length=255)
    no_bukti_transaksi = models.CharField(max_length=255)
    tgl_transaksi = models.DateTimeField(null=True)
    nominal = models.IntegerField()
    tgl_jatuh_tempo = models.DateTimeField()
    terbayar = models.IntegerField()
    sisa = models.IntegerField()
    stakeholder = models.ForeignKey(StakeHolder, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_modify = models.DateTimeField(auto_now=True, null=True)
    user_create = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='ap_created', null=True)
    user_modify = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='ap_modified', null=True)


    class Meta:
        verbose_name = 'AP'
        verbose_name_plural = 'APs'

    def __str__(self):
        return f"No Bukti Transaksi: {self.no_bukti_transaksi}"


class AR(models.Model):
    id_transaksi = models.IntegerField()
    kelas_model = models.CharField(max_length=255)
    no_bukti_transaksi = models.CharField(max_length=255)
    tgl_transaksi = models.DateTimeField(null=True)
    nominal = models.IntegerField()
    tgl_jatuh_tempo = models.DateTimeField()
    terbayar = models.IntegerField()
    sisa = models.IntegerField()
    stakeholder = models.ForeignKey(StakeHolder, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True, null=True)
    date_modify = models.DateTimeField(auto_now=True, null=True)
    user_create = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='ar_created', null=True)
    user_modify = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name='ar_modified', null=True)


    class Meta:
        verbose_name = 'AR'
        verbose_name_plural = 'ARs'

    def __str__(self):
        return f"No Bukti Transaksi: {self.no_bukti_transaksi}"

