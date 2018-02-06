# file StatusBar.py
import tkinter
from tkinter import *
from tkinter import ttk

class StatusBar(Frame):
    def __init__(self,master):
      Frame.__init__(self, master)
      self.label = Label(self, border=1, 
         relief='sunken', 
         anchor='w',width=50)
      self.label.pack(side='left',padx=4,pady=2)
      self.pb = ttk.Progressbar(self,
         length=60,mode='determinate')
      self.pb.configure(value=30)
      self.pb.pack(side='right',padx=4,pady=2)

    def set(self, format, *args):
      self.label.config(text=format % args)
      self.label.update_idletasks()
         
    def clear(self):
      self.label.config(text="")
      self.label.update_idletasks()
         
    def progress(self,n):
      self.pb.configure(value=n)
      self.pb.update_idletasks()

if __name__ == "__main__":

  root = Tk()
  root.title('DGApp')
  #import Screenshot
  import sys
  #shot=Screenshot.Screenshot()
  Frame(root, width=200, height=100).pack()
  status = StatusBar(root)
  status.pack(side=tkinter.BOTTOM, fill=tkinter.X)
  root.update()

  status.set("Connecting...")
  status.progress(25)
  #shot.shot('DGApp',root,'statusbar-python.png',ex=False)
  root.after(1000)
  status.set("Connected, logging in...")
  status.progress(50)
  root.after(1000)
  status.set("Login accepted...")
  status.progress(75)
  root.after(1000)
  status.clear()
  #sys.exit(0)
  root.mainloop()
