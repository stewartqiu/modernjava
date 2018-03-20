

from uuid import getnode as get_mac
import subprocess
import os
from sys import platform
import xlrd




# ambil mac address
def getMacAddress():
	return get_mac()



# ambil hardware id
def getDiskId():
	osName = getOsName2()
	if osName == "windows":
		
		return 
	else:
		return os.popen("/usr/sbin/system_profiler SPHardwareDataType | fgrep 'Serial' | awk '{print $NF}'").read()  



def getOsName1():
	return os.name

# ambil jenis os
def getOsName2():
	if platform == "linux" or platform == "linux2":
    		return "linux"
	elif platform == "darwin":
    		return "macos"
	elif platform == "win32" or platform == "cygwin":
			return "windows"


# baca excel return dictionary[coln]
def bacaExcel(file):
	book = xlrd.open_workbook(file_contents = file, encoding_override = 'utf8')
	sheet = book.sheet_by_index(0)

	rows = []
	for nRow in range(1,sheet.nrows):
		rowData = sheet.row(nRow)
		data = {}
		for nCol in range(sheet.ncols):
			key = "col%s" % nCol
			data[key] = rowData[nCol].value
		rows.append(data)
	return rows








