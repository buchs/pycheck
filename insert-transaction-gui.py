#! /opt/ActivePython-2.7/bin/python

from Tkinter import *
import tkMessageBox
# from ttk import *  # overrides the Tk equivalent widgets
import sys
import re # regular expressions
import MySQLdb
import numbers
import datetime

# Reconfigurable Section
commonbackground="#aba7d7"
cfont="Times 12" # favored font for content, as opposed to labels


if sys.platform == "linux2":
  bindkey='<Key-Return>'
else:
  bindkey='<Return>'

# Get today's date info
tday = datetime.date.today()
DateEnter = '"' + str(tday.year) + "-" + str(tday.month) + "-" + \
            str(tday.day) + '"'
currentyear = str(tday.year)


print("getting database setup")

db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()

# Get lists of accounts, types and categories:
sqlstatement="select Id,Name from Accounts"
cursor.execute(sqlstatement)
Accounts=cursor.fetchall()
sqlstatement="select Id,Name from Categories"
cursor.execute(sqlstatement)
Categories=cursor.fetchall()
sqlstatement="select Id,Name from TransTypes"
cursor.execute(sqlstatement)
Types=cursor.fetchall()

print("got it, proceeding")

# find max column widths needed
max_accts = 0
for a in Accounts:
  if len(a[1]) > max_accts:
    max_accts = len(a[1])

max_cats = 0
for a in Categories:
  if len(a[1]) > max_cats:
    max_cats = len(a[1])



#------------------- Print_Contents ----------------------------

def print_contents(event):
  print("in print_contents")
  #print("event type = " + str(event.type) + ", keysym = " + \
  #      str(event.keysym))
  ignore = False
  message = "Cannot process input, note these warnings:\n"

  accounttuple = acct.curselection()
  if len(accounttuple) == 0:
    ignore = True
    message += "account not selected;\n"
  else:
    account = int(accounttuple[0])

  transtype = typeradiovar.get()
  if not isinstance(transtype,numbers.Integral) or transtype == 0:
    ignore = True
    message += "transaction type invalid;\n"
  transtype = int(transtype)

  cattuple = cat.curselection()
  if len(cattuple) == 0:
    ignore = True
    message += "no category selected;\n"
  else:
    category = int(cattuple[0])
    
  datestr = date.get()  
  dateparts = datestr.split('/')
  if len(dateparts) < 2:
    ignore = True
    message += "need at least a month/day in date;\n"
  else:
    if len(dateparts) == 2:
      # add in the current year
      dateparts.insert(0,currentyear)
    # test to determine if valid date
    try:
      datetest = datetime.date(int(dateparts[0]), \
                               int(dateparts[1]),int(dateparts[2]))
    except:
      ignore = True
      message += "date is not valid;\n"
    else:
      datevalue = '"' + "-".join(dateparts) + '"'

  payee = pay.get()
  if len(payee) == 0:
    ignore = True
    message += "payee is empty;\n"
  else:
    payee = '"'+payee+'"'
    
  amountstr = amt.get()
  if len(amountstr) == 0:
    ignore = True
    message += "amount is empty;\n"
  else:
    try:
      amount = float(amountstr)
    except:
      ignore = True
      message += "amount is invalid;\n"

  memostring = memo.get(1.0,END)
  memostring = memostring.strip()
  if len(memostring) == 0:
    memostring = "NULL"
  else:
    memostring = '"'+memostring+'"'

  reconciled=False
  
  if sales_tax.get() == True:
    print(str(stamount.get()))
    if len(str(stamount.get())) == 0:
      sales_tax_value=0
    else:
      sales_tax_value=stamount.get()
  else:
    sales_tax_value=-1
  
  if ignore:
    print(message)
    tkMessageBox.showwarning('Warnings',message)
  else:
    insfmtstr =  "INSERT INTO Transactions VALUES "
    insfmtstr += "(NULL,%d,%s,%.2f,%d,%s,%d,%s,%s,%d,%d)"
    sqlstatement=insfmtstr % (transtype,payee,amount,category, \
                              memostring,account,datevalue,DateEnter, \
                              reconciled,sales_tax_value)
    print(sqlstatement)
    cursor.execute(sqlstatement)
    status = cursor.fetchone()
    if not status == None:
      message = "I got an unusual return status from the database\ninsertion command.  I don't know what to do now\nbut please let my creator\nknow about this.\nstatus=" + str(status)
      tkMessageBox.showwarning('Warnings',message)
    
    # print("submitting: " + str(account) + "," + str(transtype) + \
    #       "," + category + \
    #       "," + datevalue + ",\"" + payee + "\"," + \
    #       str(amount) + "," + memostring )
    # reset fields
    pay.delete(0,END)
    amt.delete(0,END)
    memo.delete(1.0,END)
    
    
#----- End of Print_Contents ----------------------------------------------

#----- Main, action begins here -------------------------------------------
          
win=Tk()
win.title("Financial Database - Enter Transactions")
win.config(background=commonbackground)

#-- Account List --
aframe=Frame(master=win,background=commonbackground)
acctlab=Label(aframe,text='\nAccount',background=commonbackground)
acctlab.grid(row=0,column=0,sticky="nw")
acct=Listbox(aframe,font=cfont,height=6,width=max_accts, \
             exportselection=0)
acct.grid(row=1,column=0,sticky="nw")
i=0
for a in Accounts:
  acct.insert(i,a[1])
  i += 1
acct.bind(bindkey, print_contents)
acc_scroller = Scrollbar(aframe, orient='vertical', \
                         command=acct.yview,takefocus=0)
acct.config(yscrollcommand=acc_scroller.set)
acc_scroller.grid(row=1,column=1,sticky="news")

#-- Transaction Types --
tframe=Frame(master=win,background=commonbackground,borderwidth=1,relief="groove")
typelab=Label(tframe, \
              text="Transaction Type\n(check num. or ATM, etc.)", \
              background=commonbackground, \
              justify="left")
typelab.pack(anchor="nw")
typeradiovar = IntVar()
cknum=Entry(tframe,font=cfont,textvariable=typeradiovar,width=7)
cknum.pack(anchor="nw")
cknum.bind(bindkey,print_contents)
i = 0
typerb=[]
for a in Types:
  typerb.append(Radiobutton(tframe,font=cfont, \
                            variable=typeradiovar,value=a[0], \
                            text=a[1],takefocus=0, \
                            background=commonbackground))
  #print("type=%s" % a[1])
  typerb[i].pack(anchor='nw')
  i += 1
typeradiovar.set(0)

#-- Category List --
cframe=Frame(master=win,background=commonbackground)
catlab=Label(cframe,text="Category",background=commonbackground)
catlab.grid(row=0,column=0,sticky="n")
catlen = len(Categories)
needscrollbar = 0
if catlen > 25:
  catlen = 25
  needscrollbar = 1
cat=Listbox(cframe,width=max_cats,height=catlen,exportselection=0, \
            font=cfont)
cat.grid(row=1,column=0,sticky="n")
cat.bind(bindkey, print_contents)
for c in Categories:
  cat.insert(c[0],c[1])

if needscrollbar == 1:  
  cat_scroller = Scrollbar(cframe, orient='vertical', \
                           command=cat.yview,takefocus=0)
  cat.config(yscrollcommand=cat_scroller.set)
  cat_scroller.grid(row=1,column=1,sticky="news")

#-- Transaction Date --
dframe=Frame(master=win,background=commonbackground,borderwidth=1, \
             relief="groove")
datelab=Label(dframe,text='Date of purchase\n(mm/dd)', \
              justify="left",\
              background=commonbackground)
datelab.pack(anchor="nw")
date=Entry(dframe,font=cfont,width=12)
date.pack(anchor="nw")
date.bind(bindkey, print_contents)

#-- Payee Name --
pframe=Frame(master=win,background=commonbackground,borderwidth=1, \
             relief="groove")
paylab=Label(pframe,text="Payee",background=commonbackground)
payspacer=Label(pframe,text="  ",background=commonbackground)
pay=Entry(pframe,font=cfont,width=45)
paylab.grid(row=0,column=0,sticky="nw")
pay.grid(row=1,column=0,sticky="news")
payspacer.grid(row=1,column=1)
pay.bind(bindkey, print_contents)

#-- Payment Amount --
mframe=Frame(master=win,background=commonbackground,borderwidth=1, \
             relief="groove")
amtlab=Label(mframe,text="Amount",justify="left", \
             background=commonbackground)
amtlab.pack(anchor="nw")
amt=Entry(mframe,text="0.00",font=cfont)
amt.pack(anchor="nw")
amt.bind(bindkey, print_contents)

#-- Sales Tax Owed --
# tiny little routine to couple sales tax items
def update_sales_tax():
  if sales_tax.get() == True:
    stamt.config(state="normal")
  else:
    stamt.config(state="disabled")
sales_tax=BooleanVar()
sales_tax.set(False)
stamount=DoubleVar()
stamount.set(0)

stframe=Frame(master=win,background=commonbackground,borderwidth=1, \
              relief="groove")
stlabel=Label(stframe,text='Sales Tax',background=commonbackground)
stsubframe=Frame(master=stframe,background=commonbackground)
stcheck=Checkbutton(stsubframe,command=update_sales_tax,variable=sales_tax, \
                    takefocus=False)
stamt=Entry(stsubframe,font=cfont,textvariable=stamount,width=9,state="disabled")
stlabel.pack(anchor="nw")
stcheck.pack(anchor="nw",side="left")
stamt.pack(anchor="nw",side="left")
stsubframe.pack(anchor="nw")

#-- Memo Field --
eframe=Frame(master=win,background=commonbackground,borderwidth=1, \
             relief="groove")
memolab=Label(eframe,text='Memo',background=commonbackground)
memolab.pack(anchor="nw")
memo=Text(eframe,font=cfont,height=5,width=45)
memo.pack(anchor="nw")
memo.bind(bindkey, print_contents)
memo.bind("<Key-Tab>","")

aframe.grid(row=0,column=0,sticky="nw",ipadx=5)
tframe.grid(row=0,column=1,sticky="nw",ipadx=5)
cframe.grid(row=0,column=2,rowspan=5,sticky="n",ipadx=5)
dframe.grid(row=1,column=0,sticky="nw",ipadx=5)
pframe.grid(row=2,column=0,columnspan=2,sticky="news", \
            ipadx=5)
mframe.grid(row=3,column=0,columnspan=1,sticky="nw",ipadx=5)
stframe.grid(row=3,column=1,sticky="nw")
eframe.grid(row=4,column=0,columnspan=2,sticky="news",ipadx=5)

# enter event loop
mainloop()
