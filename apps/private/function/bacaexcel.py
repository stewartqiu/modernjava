import xlrd


def excelSiswa(file):
	book = xlrd.open_workbook(file_contents = file, encoding_override = 'utf8')
	first_sheet = book.sheet_by_index(0)

	row = []
	for row in range(1,first_sheet.nrows):
		rowData = first_sheet.row(row)
		data = {
			"nis" : rowData[0].value,
			"nama" : rowData[1].value,
			"kelas" : rowData[2].value,
			"tahunMasuk" : rowData[3].value,
			"nilaiSpp" : rowData[4].value,
			"hpSiswa" : rowData[5].value,
			"hpOrtu1" : rowData[6].value,
			"hpOrtu2" : rowData[7].value,
			"hpWali" : rowData[8].value,
		}
		rows.append(data)
	return rows


def excelKd(file):
	book = xlrd.open_workbook(file_contents = file, encoding_override = 'utf8')
	first_sheet = book.sheet_by_index(0)

	rows = []
	for row in range(1,first_sheet.nrows):
		data = { 	
			"mapel": first_sheet.row(row)[0].value,
			"kelas": first_sheet.row(row)[1].value,
			"jurusan": first_sheet.row(row)[2].value,
			"semester": first_sheet.row(row)[3].value,
			"noUrut": first_sheet.row(row)[4].value,
			"jenis": first_sheet.row(row)[5].value,
			"kode": first_sheet.row(row)[6].value,
			"keterangan": first_sheet.row(row)[7].value,
		}
		rows.append(data)
	return rows



















