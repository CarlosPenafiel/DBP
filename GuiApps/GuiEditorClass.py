#!/usr/bin/python3
from GuiBaseClass import GuiBaseClass
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import *
from DGTableView import DGTableView
import time

class GuiEditorClass(GuiBaseClass):
	""" Class doc """
	
	def __init__ (self,root):
		""" Class initialiser """
		super().__init__(root)
		self.frame=self.getFrame()
		self.note = ttk.Notebook(self.frame)
		self.tab1 = ttk.Frame(self.note)
		self.tab2 = ttk.Frame(self.note)
		self.note.add(self.tab1, text = "Tab One")
		self.note.add(self.tab2, text = "Tab Two")
		self.text1=ScrolledText(self.tab1)
		self.text1.bind("<<Modified>>",self.checkText)
		mnf=self.getMenu('File')
		self.txtcontent = ""
		mnf.insert_command(0,label='Save', command=self.Save,
			underline=0)
		mnf.insert_command(2,label='Save As', command=self.SaveAs,
			underline=0)
		self.text2 = ScrolledText(self.tab2)
		self.frame.pack(expand=True,fill="both")
		self.note.pack(expand=True,fill="both")
		self.text1.pack()
		self.text2.pack()
		self.addStatusBar()
	def checkText(self,widget):
		print("changed")
	def newFile(self):
		self.text.pack_forget()
		self.text=ScrolledText(self.tab1)
		self.text.pack(expand=True,fill="both")
	
	def openFile(self):
		self.tab2 = ttk.Frame(self.note)
		self.text2 = ScrolledText(self.tab2)
		self.note.add(self.tab2,text="Text Two")
		filename = filedialog.askopenfilename(
			filetypes=(('Text files','*txt'),('All Files','*.*'))) #initialdir="~"
		self.setProgress(10)
		self.setMessage("Loading")
		root.after(400)
		self.setProgress(20)
		self.setMessage("Fake Loading 1")
		root.after(400)
		self.setProgress(50)
		self.setMessage("Fake Loading 2")
		root.after(400)
		self.setProgress(75)
		self.setMessage("Fake Loading 3")
		root.after(400)
		self.setProgress(100)
		self.setMessage("Finished")
		root.after(400)
		file = open(filename, 'r')
		for line in file:
			self.text2.insert("end",line)
		file.close()	#text.get für bekommen
		self.setProgress(0)
		self.setMessage("")
		self.note.select(self.tab2)
		self.text2.pack()
	
	def Save(self):
		filename = filedialog.asksavefilename()
		self.txtcontent=self.text1.get("1.0","end")
		print(self.txtcontent)
		pass
	
	def SaveAs(self):
		filename = filedialog.asksaveasfilename()
		pass
	


if __name__ == '__main__':
	root = tk.Tk()
	txtEditor=GuiEditorClass(root)
	
	
	txtEditor.mainLoop()

