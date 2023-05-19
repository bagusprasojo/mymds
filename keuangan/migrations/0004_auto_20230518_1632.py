# Generated by Django 3.1 on 2023-05-18 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kesantrian', '0002_auto_20230518_1346'),
        ('keuangan', '0003_auto_20230518_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='coa',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='coa',
            name='date_modify',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='coa',
            name='user_create',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ap_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coa',
            name='user_modify',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ap_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='AP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_transaksi', models.IntegerField()),
                ('nominal', models.IntegerField()),
                ('tgl_jatuh_tempo', models.DateField()),
                ('kelas_model', models.CharField(max_length=255)),
                ('no_bukti_transaksi', models.CharField(max_length=255)),
                ('terbayar', models.IntegerField()),
                ('sisa', models.IntegerField()),
                ('date_create', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modify', models.DateTimeField(auto_now=True, null=True)),
                ('stakeholder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kesantrian.stakeholder')),
                ('user_create', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coa_created', to=settings.AUTH_USER_MODEL)),
                ('user_modify', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coa_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AP',
                'verbose_name_plural': 'APs',
            },
        ),
    ]
