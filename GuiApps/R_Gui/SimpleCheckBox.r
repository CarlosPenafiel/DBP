#!/usr/bin/R
library(tcltk2)
tkdestroy(tt)
tt = tktoplevel()
vardetlef = tclVar("0")
cbdetlef = tkcheckbutton(tt,variable=vardetlef,text="I like Detlef!")
tkgrid(cbdetlef,padx =20)
tbOK = tkbutton(tt,text="OK",command = function () { 
	valdetlef = as.character(tclvalue(vardetlef)) 
	 print(valdetlef)
	 if (valdetlef == "1"){tkmessageBox(message="So do I!")}
	 if (valdetlef == "0"){tkmessageBox(message="You forgot to check!")}
	
	})
tkgrid(tbOK)
