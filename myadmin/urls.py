from django.urls import path 
from . import views


app_name = 'myadmin'

urlpatterns = [
    path('', views.index, name='index'),
    path('import_siswa/', views.importSiswa, name='import_siswa'),
    path('import_siswa/konfirmasi', views.konfirmImportSiswa, name='konfirm_import_siswa'),
    path('import_kd/', views.importKd, name='import_kd'),
    path('entry_guru/', views.entryGuru, name='entry_guru'),
    path('spp/', views.spp, name='spp'),
]