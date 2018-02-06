#!/usr/bin/R
library(tcltk2)

increaseVar =function () {
	tclvalue(app$var)=as.integer(tclvalue(app$var))+1
	print(tclvalue(app$var))
}
onExit = function () {
	#place your MessageBox
	print("Let's exit : ")
	#we destroy only the toplevel
	tclvalue(app$done) = 1
	tkdestroy(app$tt)
}
gui = function () {
	# we keep all vars in a list variable
	app=list()
	app$done=0
	app$tt=tktoplevel()
	tkwm.title(app$tt,"DGApp")
	tkwm.geometry(app$tt,"300x400+50+150")
	#first exercise labelframe
	app$tklf=ttklabelframe(app$tt,text="Exercise 1")
	app$var=tclVar('0')
	tkpack(tklabel(app$tklf,textvariable=app$var))
	app$btn=ttkbutton(app$tklf,command=increaseVar,text='i+')
	tkpack(app$btn)
	tkpack(app$tklf,side='top',fill='both',expand=TRUE,padx=10,pady=10)
	# menu part
	topMenu = tkmenu(app$tt,tearoff=FALSE)
	tkconfigure(app$tt,menu=topMenu)
	fileMenu=tkmenu(topMenu,tearoff=FALSE)
	tkadd(topMenu,"cascade",label="File",menu=fileMenu, underline=0)
	tkadd(fileMenu,'separator')
	tkadd(fileMenu,"command",label="Exit",command=onExit, underline=0)
	return(app)
}

app=gui()
# the mainloop()
#tkwait.variable(app$done)
