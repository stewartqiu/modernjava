

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from apps.private.function import stool, bacaexcel
import pyrebase
from .objects import KompetensiDasar, Siswa
import json

config = {
    "apiKey": "AIzaSyB_DUe9SqZCISicln0UeAHOh1n5bD8zHmI",
    "authDomain": "tester-only.firebaseapp.com",
    "databaseURL": "https://tester-only.firebaseio.com",
    "projectId": "tester-only",
    "storageBucket": "tester-only.appspot.com",
    "messagingSenderId": "1002754199973"
  };

# firebase = pyrebase.initialize_app(config)
# database = firebase.database()
# data = {"data": "test onlyy"}
# database.child("Testing/Web").set(data)
# database.child("Testing/Web").get().val()


# Create your views here.
def index(request):
	return render(request, "myadmin/main.html")



def login(request):
	return render(request, "myadmin/login.html")




def import_siswa(request):
	return render(request, 'myadmin/import_siswa.html', {'test': stool.getDiskId()})




def konfirmasi_xls_siswa(request):
	if request.method == "POST":
		
		if len(request.FILES) > 0:	
			file = request.FILES['pickExcel']
			if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
				return redirect(reverse('myadmin:xls_siswa_wrong', kwargs={'wrong':'wrong_extension'}))

			read = stool.bacaExcel(file.read())

			first_row = read[0]

			if len(first_row) is not 9:
				return redirect(reverse('myadmin:xls_siswa_wrong', kwargs={'wrong':'wrong_format'}))


			return render(request, 'myadmin/konfirmasi_xls.html' , {'dataList' : read})


		elif 'dataList' in request.POST:
			dataList = request.POST.get('dataList') 
			jsonify = json.loads(dataList)
			result = 0
			for data in dataList:
				result += 1 
			return HttpResponse(jsonify[2]['col0'])
		else :
			return HttpResponse(request.POST)

	else :
		raise Http404('URL tidak ditemukan')



def xls_siswa_wrong(request, wrong):
	message = ''
	if wrong == 'wrong_extension':
		message = 'File yang diunggah bukan file excel.'
	elif wrong == 'wrong_format' :
		message = 'Format kolom excel tidak sesuai'
	return render(request, 'myadmin/import_siswa.html', {'wrong_message': message})





	# Import excel data kd
	# Baca excel
	# Result excel masih raw
	# Cek kalau jumlah kolom benar,
	# Lakukan konfirmasi
	# Yes = Handle result excel yg masih raw -> simpan
	# no = Ulang

	# window popup atau page baru?

	#redirect for confirmation

def import_kd(request):

	if request.method == "POST":
		if request.FILES['pickExcel']:
			file = request.FILES['pickExcel']

			if not (file.name.endswith('.xls') or file.name.endswith('.xlsx')):
				return HttpResponse('wrong extension')

			read = stool.bacaExcel(file.read())

			first_row = read[0]

			if len(first_row) is not 8:
				return HttpResponse('wrong format')


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
				kd.keterangan = data['col7']
				kdList.append(kd)

			return render(request, "myadmin/import_kd.html", {'postResult' : kdList})

	return render(request, "myadmin/import_kd.html")



def entry_guru(request):
	return render(request, "myadmin/entry_guru.html")

	

def spp(request):
	return render(request, "myadmin/spp.html")









