#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import *
from tkinter import filedialog
import DGBaseApp 
import DGTableView
import sys
import sqlite3
import os

class TiBSQLBrowser(DGBaseApp.DGBaseApp):
    def __init__ (self,root):
        super().__init__(root)
        self.frame= self.getFrame()
        mnu = self.getMenu("File")
        mnu.insert(1,"command", command=self.openDatabase,label="Open Database", underline =5)
        self.pw=ttk.Panedwindow(self.frame,orient='vertical')
        self.frame1=tk.Frame(self.pw)
        self.text1 = ScrolledText(self.frame1,height=8,width=5)
        self.btn1 = tk.Button(self.frame1, text='Run SQL!',command=self.runSQL)
        self.tview = DGTableView.DGTableView(self.pw)
        
        


        self.filetypes = (("Tab-Files","*.tab"),("Text Files","*.txt"),
        ("all Files","*"))
        self.dbtypes = (('SQLite-Files','*.sqlite3'),('All Files','*.*'))
        self.lastDir = ""
        self.currentDBFile ="/home/stud7117/DBP-labs/ex-2018-01-18/go2018.sqlite3"
        self.text1.insert("1.0","select * from gonames2018 limit 10")

        self.btn1.pack(fill="x", expand=False)
        self.text1.pack(expand=True,fill="both")
        self.pw.add(self.frame1)
        self.pw.add(self.tview)
        self.pw.pack(expand=True,fill="both")
        self.addStatusBar()
        root.geometry("400x300")
    def openFile(self):
        filename = filedialog.askopenfilename(
            filetypes=self.filetypes)
        self.tview.readTabfile(filename)
        self.lastDir = os.path.dirname(filename)
        
    def openDatabase(self):
        filename = filedialog.askopenfilename(
            filetypes=self.dbtypes)
        self.tview.readTabfile(filename)
        self.currentDBFile = filename
        self.lastDir = os.path.dirname(filename)
    
    def runSQL(self):
        self.tview.delete(*self.tview.get_children())
        stm = self.text1.get("1.0","end")
        conn = sqlite3.connect(self.currentDBFile)
        conn.row_factory = sqlite3.Row
        curs = conn.cursor()
        curs.execute(stm)
        x=0
        for row in curs:
            if x==0:
                self.tview.configure(columns=row.keys())
                for key in row.keys():
                    self.tview.heading(key,text=key)
                x = x + 1
            else:
                l = []
                for key in row.keys():
                    l.append(row[key])
                self.tview.insert("",'end',values=l)

'''
        self.conn = sqlite3.connect('filename')
        self.conn.row_factory = sqlite3.Row
        self.curs = self.conn.cursor()
        '''
    


if __name__ == '__main__':
    root=tk.Tk()
    bapp = TiBSQLBrowser(root)
    
    bapp.mainloop()
