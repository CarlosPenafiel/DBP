#!/usr/bin/python3
import csv
import sqlite3
import sys

class SqlUtils():
    def csv2sqlite3(self,csvfile,sqlite3file,
               tablename,delimiter=',',quotechar='"'):
        conn=sqlite3.connect(sqlite3file)
        curs=conn.cursor()
        curs.execute("DROP TABLE IF EXISTS "+tablename)       
        cfile = open(csvfile,"r")
        csvr = csv.reader(cfile,delimiter=delimiter,quotechar='"')
        x = 1
        for row in csvr:
            if x == 1:
                ncol=len(row)
                stm="CREATE TABLE "+tablename+" ("
                istm="INSERT INTO "+tablename+" VALUES"+" ("
                for col in row:
                    stm=stm+col+" TEXT"
                    istm=istm+"?"
                    if col != row[len(row)-1]:
                        stm = stm+","
                        istm = istm+","
                stm=stm+")"
                istm=istm+")"                 
                x=x+1
                conn.execute(stm)
            else:
                if (len(row)>0):
                    if (ncol+1) == len(row):
                        # R data.frame with row names
                        conn.execute(istm,row[1:len(v)])
                    else:
                        conn.execute(istm,row)
                    
        cfile.close()
        conn.commit()
        conn.close()       
    def test(self):
        print("test")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: "+ sys.argv[0]+" filename.tab database.sqlite3 tablename")
        sys.exit(0)
    else:
        sql=SqlUtils()
        #sql.test()
        sql.csv2sqlite3(sys.argv[1],sys.argv[2],sys.argv[3],delimiter="\t")
doc="""
Templates:
cfile=open(,"r")
csvr=csv.reader(cfile,delimiter=",",quote='"')
for row in csvr:
cfile.close()

conn=sqlite3.connect(filename)
curs=conn.cursor()
curs.execute("stm")
curs.commit()
curs.close()
"""
