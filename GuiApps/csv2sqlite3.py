#!/usr/bin/python3

import csv
import sqlite3
import re

class SqlUtils():
	def csv2sqlite3(self,sqlite3file,
				tablename, delimiter=',',quotechar='"'):
		# Load the CSV file into CSV reader
		#csvfile =open('../survey.min.txt','r')
		csvfile = open(sqlite3file,'r')
		creader = csv.reader(csvfile, delimiter = delimiter,quotechar=quotechar)
		#Iterat through the CSV file
		# inserting values into the database
		i = 0
		for t in creader:
			if i == 0:
				header = t	#hier aus erster Zeile auslesen
				delimiter_list = re.findall(re.escape(delimiter), header)
				if len(delimiter_list) == 1:
					delimiter_str = "?"
				elif len(delimiter_list) > 1:
					delimiter_str = "?," * (len(delimiter_list)-1)+"?"
				else:
					print("No delimiter found")
					return()
			if i > 0:
				cursor.execute('INSERT INTO survey VALUES ('+
								delimiter_str +')',t)
			i = i + 1
		#Close the csv fie
		csvfile.close()
		connection.commit()
		connection.close()

def main():
	util = SqlUtils().csv2sqlite3("herefile","name")

if __name__ == '__main__':
	main()
