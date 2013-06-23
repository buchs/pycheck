#! /usr/bin/python

from Tkinter import *
main = Tk()
main.withdraw()

sp = Toplevel()
sp.geometry("100x100+500+500")
sp.overrideredirect(1)
can = Canvas(sp,width=100, height=100)
can.pack()
gif = PhotoImage(file='/home/buchs/fin/splash.gif')
can.create_image(0,0,image=gif,anchor="nw")
sp.after(5000,sp.destroy())
sp.update()
print('down to mainloop')
sp.mainloop()
