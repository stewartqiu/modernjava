from django.urls import path 
from . import views


app_name = 'myadmin'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),

    path('import_siswa/', views.import_siswa, name='import_siswa'),
    path('import_siswa/konfirmasi/', views.konfirmasi_xls_siswa, name='konfirmasi_xls_siswa'),
    path('import_siswa/<str:wrong>/', views.xls_siswa_wrong, name='xls_siswa_wrong'),
    
    path('import_kd/', views.import_kd, name='import_kd'),
    
    path('entry_guru/', views.entry_guru, name='entry_guru'),
   
   	path('spp/', views.spp, name='spp'),
]