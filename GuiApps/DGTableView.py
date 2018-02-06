
import tkinter.ttk as ttk
import tkinter as tk 
 
class DGTableView (ttk.Treeview):
    def __init__(self,parent,*args, **kwargs):
        ttk.Treeview.__init__(self, parent,*args,**kwargs)
        self.vsb = ttk.Scrollbar(parent, orient="vertical", command=self.yview)
        self.hsb = ttk.Scrollbar(parent, orient="horizontal", command=self.xview)        
        self.configure(yscrollcommand=self.vsb.set,
            xscrollcommand=self.hsb.set)
        self.column("#0",width=0)
        self.column("#0",minwidth=0)        
        self.vsb.pack(side="right", fill="y")
        self.pack(side="top", fill="both", expand=True)
        self.hsb.pack(side="bottom", fill="x")
    def readTabfile(self,filename):
        self.delete(*self.get_children())
        i = 0
        file = open(filename,"r")
        for line in file:
            cells= line.split("\t")
            if i == 0:
                for i in range(1,len(cells)):
                    if i == 1:
                        l=["col"+str(i)]
                    else:
                        l.append("col"+str(i))
                self.configure(columns=l)
                for i in range(1,len(cells)):
                    col="col"+str(i)
                    self.heading(col,text=cells[i-1])
            else:
                self.insert("",'end',values=cells)
            i = i + 1
        
   
if __name__ == '__main__':
    root = tk.Tk()
    root.title('DGApp')
    dgtab=DGTableView(root)
    dgtab.readTabfile("/home/groth/workspace/DBP2017/teachers/dgroth/GuiApps/iris.tab")
    #dgtab.readTabfile("../../data/ss_aa_matrix.txt")
    root.mainloop()
