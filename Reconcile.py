#! /opt/ActivePython-2.7/bin/python

from Tkinter import *
import tkMessageBox
# from ttk import *  # overrides the Tk equivalent widgets
import sys
import re # regular expressions
import MySQLdb
import numbers
import datetime

# Loading my personal libraries
# import sys
#sys.path.append('<your choice of path here>')
from MultiListboxRead import *

# Reconfigurable Section
commonbackground="#aba7d7"
cfont="Times 11" # favored font for content, as opposed to labels
ffont="Courier 10" # where I need fixed width
smfont="Times 9" # for mode line

# Get today's date info
tday = datetime.date.today()
thismonth = "%02d" % tday.month
currentyear = str(tday.year)

# now, get a month ago, beginning of the month
year = currentyear
month = tday.month - 2
while month < 0:
  year -= 1
  month += 11
monthnum = "%02d" % (month + 1)
BeginLastMonth = '"' + str(year) + '-' + monthnum + '-01"'

#-------------------------------------------------------- fudge -----------
BeginLastMonth = '"2010-07-10"'



print("getting database setup")
db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()

# Get lists of accounts, types and categories:
sqlstatement="select Id,Trim(Name) from Accounts"
cursor.execute(sqlstatement)
Accounts=cursor.fetchall()
sqlstatement="select Id,Trim(Name) from Categories"
cursor.execute(sqlstatement)
Categories=cursor.fetchall()
sqlstatement="select Id,Trim(Name) from TransTypes"
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

#------------ Display of Transactions For Reconciliation ------

def ToggleReconciled(event):
  global TMap, RMap

  idx = int(Transactions_lb.curselection()[0])
  Transactions_lb.select_clear(idx)
  
  if RMap[idx]:
    # it was marked reconciled
    RMap[idx] = 0
    Transactions_lb.itemconfigure(idx,bg='white')
  else:
    # it was not marked reconciled
    RMap[idx] = 1
    Transactions_lb.itemconfigure(idx,bg='green')

  # Now update the database
  sqlstatement = 'UPDATE Transactions SET Reconciled=%d WHERE Id=%d' \
                 % (RMap[idx],TMap[idx])
  cursor.execute(sqlstatement)
  junk = cursor.fetchall()


# first get the data to determine what the maximum size of payee field
# should be
sqlstatement='SELECT Trim(T.Payee) FROM Transactions AS T WHERE DateTrans >= ' + BeginLastMonth
cursor.execute(sqlstatement)
TLines = cursor.fetchall()
payeewidth = 0
for tl in TLines:
  w = len(tl[0])
  if w > payeewidth:
    payeewidth = w

Transactions = Tk()
Transactions.title('Reconciliation')

ftext = "%-10s | %-" + str(payeewidth) + "s | % 8.2f | %-" + str(max_accts) + \
        "s | %-" + str(max_cats) + "s"
ltext = "%-10s | %-" + str(payeewidth) + "s | %-8s | %-" + str(max_accts) + \
        "s | %-" + str(max_cats) + "s"

ltext = ltext % ("Date","Payee","Amount","Account","Category")
Transactions_label = Label(Transactions, text=ltext, borderwidth=1, \
                   relief=RAISED,font=ffont)
Transactions_label.grid(row=0,column=0,sticky="nw")

Transactions_lb = Listbox(Transactions, width=len(ltext), \
                          borderwidth=0, selectborderwidth=0,
			  relief="flat", exportselection=FALSE,font=ffont)
Transactions_lb.grid(row=1,column=0,sticky="nw")

Transactions_sb = Scrollbar(Transactions, orient=VERTICAL,
                            command=Transactions_lb.yview)
Transactions_sb.grid(row=1,column=1,sticky="nwse")

Transactions_lb.config(yscrollcommand=Transactions_sb.set)
Transactions_lb.bind("<Double-Button-1>", ToggleReconciled)

def UpdateTransactions():
  global TMap, RMap
  
  sqlstatement= 'SELECT T.DateTrans,Trim(T.Payee),T.Amount,Trim(A.Name),' + \
                'Trim(C.Name),T.Reconciled,T.Id FROM Transactions AS T, ' + \
                'Accounts AS A,' + \
                'Categories AS C WHERE T.Account = A.Id AND ' + \
                'T.Category = C.Id AND DateTrans >= ' + BeginLastMonth
  cursor.execute(sqlstatement)
  TLines=cursor.fetchall()
  Transactions_lb.delete(0,END)
  TMap=[]
  RMap=[]
  for line in TLines:
    if len(line) == 7:
      tx = ftext % line[0:5]
      Transactions_lb.insert(END,tx)
      TMap.append(line[6])
      RMap.append(line[5])
      if line[5]:
        Transactions_lb.itemconfigure(END,bg='green')
  Transactions_lb.see(END)



UpdateTransactions()

mainloop()
