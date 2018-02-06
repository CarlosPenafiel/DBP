#!/usr/bin/python3
import sys
from GoUtils import GoUtils
from SqlUtils import SqlUtils

class GoImport(object):
	""" Class doc """
	
	def __init__(self):
		""" Class initialiser """
		pass
	def test(self):
		print("test")
	def myimport(self,goobofile,sqlite3file):
		go=GoUtils(goobofile)
		sql=SqlUtils()
		go.extractNames(outfile="gonames.tab")
		sql.csv2sqlite3("gonames.tab",sqlite3file,
						"gonames",delimiter="\t")
		sql.csv2sqlite3("gotree.tab",sqlite3file,
						"gotree",delimiter="\t")
		sql.csv2sqlite3("goobsoletes.tab",sqlite3file,
						"goobsoletes",delimiter="\t")
		print("done")

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("Usage: ",sys.argv[0]," goobofile sqlite3file")
	else:
		t=GoImport()
		t.myimport(sys.argv[1],sys.argv[2])

