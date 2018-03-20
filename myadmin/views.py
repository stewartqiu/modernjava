from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from private.function import stool, bacaexcel
import pyrebase
from .objects import KompetensiDasar, Siswa

# config = {
#     "apiKey": "AIzaSyB_DUe9SqZCISicln0UeAHOh1n5bD8zHmI",
#     "authDomain": "tester-only.firebaseapp.com",
#     "databaseURL": "https://tester-only.firebaseio.com",
#     "projectId": "tester-only",
#     "storageBucket": "tester-only.appspot.com",
#     "messagingSenderId": "1002754199973"
#   };

# firebase = pyrebase.initialize_app(config)
# database = firebase.database()
# data = {"data": "test onlyy"}
# database.child("Testing/Web").set(data)
# database.child("Testing/Web").get().val()


# Create your views here.
def index(request):
	return render(request, "myadmin/main.html")

def importSiswa(request):
	if request.method == "POST" and request.FILES['pickExcel']:
		file = request.FILES['pickExcel'].read()
		read = stool.bacaExcel(file)

		first_row = read[0]

		if len(first_row) is not 9:
			return HttpResponse("Format Salah")

		siswaList = []
		for data in read:
			siswa = Siswa()
			siswa.nis = data['col0']
			siswa.nama = data['col1']
			siswa.kelas = data['col2']
			siswa.thMasuk = data['col3']
			siswa.sppBulan = data['col4']
			siswa.noHpSiswa = data['col5']
			siswa.noHpOrtu1 = data['col6']
			siswa.noHpOrtu2 = data['col7']
			siswa.noHpWali = data['col8']
			siswaList.append(siswa)

		#return HttpResponseRedirect(reverse('myadmin:konfirm_import_siswa'))
		return redirect(reverse('myadmin:konfirm_import_siswa'))
		#return render(request, "myadmin/import_siswa.html", {'postResult' : siswaList[0]})

	return render(request, 'myadmin/import_siswa.html', {'test': stool.getDiskId()})

def konfirmImportSiswa(request):
	# data = request.data
	# nis = data[0].nis
	return HttpResponse(request.GET.get('data'))


	# Import excel data kd
	# Baca excel
	# Result excel masih raw
	# Cek kalau jumlah kolom benar,
	# Lakukan konfirmasi
	# Yes = Handle result excel yg masih raw -> simpan
	# no = Ulang

def importKd(request):

	if request.method == "POST":
		if request.FILES['pickExcel']:
			file = request.FILES['pickExcel'].read()
			read = stool.bacaExcel(file)
			kdList = []
			for data in read:
				kd = KompetensiDasar()
				kd.mapel = data['col0']
				kd.kelas = data['col1']
				kd.jurusan = data['col2']
				kd.semester = data['col3']
				kd.noUrut = data['col4']
				kd.jenis = data['col5']
				kd.kode = data['col6']
				kdList.append(kd)

			return render(request, "myadmin/import_kd.html", {'postResult' : kdList})
	return render(request, "myadmin/import_kd.html")



def entryGuru(request):
	return render(request, "myadmin/entry_guru.html")

	

def spp(request):
	return render(request, "myadmin/spp.html")









