from django.db import models
from django.urls import reverse

class StakeHolder(models.Model):
    JENIS_CHOICES = [
        ('Santri', 'Santri'),
        ('Pengajar', 'Pengajar'),
        ('Pengurus', 'Pengurus'),
        ('Supplier', 'Supplier'),
        ('Lainnya', 'Lainnya'),
    ]

    jenis = models.CharField(max_length=20, choices=JENIS_CHOICES)
    kode = models.CharField(max_length=30, null=False, unique=True)
    nama = models.CharField(max_length=100, null=False, default="")

    class Meta:
        verbose_name = 'StakeHolder'
        verbose_name_plural = 'StakeHolders'

    def __str__(self):
        return self.jenis

class Ustadz(StakeHolder):    
    alamat = models.TextField()
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=10, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
    email = models.EmailField()
    nomor_telepon = models.CharField(max_length=20)
    mulai_bergabung = models.DateField()
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        return self.nama
        
    class Meta:

        verbose_name = 'Ustadz'
        verbose_name_plural = 'Ustadz-Ustadz'

class Kelas(models.Model):
    kode = models.CharField(max_length=30, null=False, unique=True)
    nama = models.CharField(max_length=120)
    is_active = models.BooleanField(null=False, default=True)
    wali_kelas = models.ForeignKey(Ustadz, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Kelas'
        verbose_name_plural = 'Kelas-kelas'


    def __str__(self):
        return self.kode

class Santri(StakeHolder):
    alamat = models.TextField()
    tempat_lahir = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=10, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')])
    level = models.ForeignKey(Kelas, on_delete=models.PROTECT)
    is_active = models.BooleanField(null=False, default=True)
    orang_tua = models.CharField(max_length=100)
    spp = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Santri'
        verbose_name_plural = 'Santris'

    def __str__(self):
        return self.nama


