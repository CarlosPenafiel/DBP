#!/usr/bin/python3
import tkinter as tk
from tkinter.messagebox import *
import sys, os
from StatusBar import StatusBar

class GuiBaseClass():
	""" Class doc """
	
	def __init__ (self,root):
		""" Class initialiser """
		#create widgets
		self.root=root
		self.menu=dict()
		root.option_add('*tearOff',False)
		menubar=tk.Menu(root)
		self.menubar=menubar
		menu_file = tk.Menu(menubar)
		menu_help = tk.Menu(menubar)
		menubar.add_cascade(menu=menu_file, label='File', 
			underline=0)
		menubar.add_cascade(menu=menu_help, label='Help', 
			underline=0)
		menu_file.add_command(label='New', command=self.newFile, 
			underline=0)
		menu_file.add_command(label='Open...', command=self.openFile,
			underline=0)
		menu_file.add_separator()
		menu_file.add_command(label='Exit',command=self.Exit,underline=1)
		menu_help.add_command(label='Help about',command=self.helpabout,underline=1)
		
		#<---- add
		self.menu['menubar']=menubar
		self.menu['File']=menu_file
		self.menu['Help']=menu_help
		root.configure(menu=self.menubar)
		self.status_bar = StatusBar(root)
		self.frame1=tk.Frame(root, width=768, height=576)
		self.frame1.pack(expand=True, fill="both")
	
	def mainLoop(self):
		self.root.mainloop()
	
	def getFrame(self):
		return(self.frame1)
	
	def getMenu(self,entry): #muss hier nicht name noch eingebunden werden?
		if entry in self.menu:
			return (self.menu[entry])
		else:
			last = self.menu['menubar'].index('end')
			self.menu[entry]= tk.Menu(self.menubar)
			self.menu['menubar'].insert_cascade(
				last, menu=self.menu[entry],label=entry)
			return(self.menu[entry])
	
	def addStatusBar(self):
		self.status_bar.pack(side="bottom")
		self.setMessage=self.status_bar.set
		self.setProgress=self.status_bar.progress
	
	def fileExit(self,ask=True):
		pass
	
	def newFile(self):
		pass
	
	def openFile(self):
		print("Opening!")
		pass
	
	def Exit(self):
		answer= askyesno(title='Exit',message='Do you want to quit?')
		if answer == True:
			sys.exit(0)
	
	def helpabout(self):
		showinfo(title="Help about!",message="Version 1.0, 07.12.2017 \nThis program was created \nby Timon Bauer.")

if __name__ == '__main__':
	root=tk.Tk()
	bapp = GuiBaseClass(root)
	mnu=bapp.getMenu('Edit')
	mnu.add_command(label='Copy',command=lambda: print('Copy'))
	bapp.addStatusBar()
	bapp.setMessage("Loading")
	bapp.setProgress(20)
	root.after(2000)
	bapp.setMessage("Finished")
	bapp.setProgress(100)
	
	bapp.mainLoop()


