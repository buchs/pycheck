#! /opt/ActivePython-2.7/bin/python

from Tkinter import *
import tkMessageBox
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

if sys.platform == "linux2":
  bindkey='<Key-Return>'
else:
  bindkey='<Return>'

# Get today's date info
tday = datetime.date.today()
thismonth = "%02d" % tday.month
DateEnter = '"' + str(tday.year) + "-" + thismonth + "-" + \
            str(tday.day) + '"'
currentyear = str(tday.year)

# now, get a month ago, beginning of the month
year = currentyear
month = tday.month - 2
while month < 0:
  year -= 1
  month += 11
monthnum = "%02d" % (month + 1)
BeginLastMonth = '"' + str(year) + '-' + monthnum + '-01"'

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

# just for testing

tk = Tk()
tk.withdraw()

#------------ Display of Budget Status ------

Budgets = Toplevel()
Budgets.title("Budget Status")
BudgetmLab = Label(Budgets,text="Monthly Budget Items",bg="yellow")
BudgetmLab.pack(fill="x")
BudgetMLBm = MultiListBoxRead(Budgets, \
                             ( ('Category', max_cats), \
                               ('Budget', 8),          \
                               ('Remaining', 8) ) )
BudgetMLBm.pack(expand=True,fill='both')

BudgetaLab = Label(Budgets,text="Accumulating Budget Items",bg="yellow")
BudgetaLab.pack(fill="x")
BudgetMLBa = MultiListBoxRead(Budgets, \
                             ( ('Category', max_cats), \
                               ('Addition/Month', 8),          \
                               ('Accumlation', 8) ) )
BudgetMLBa.pack(expand=True,fill='both')

# Initially display the current month
budgetyear = tday.year
budgetmonth = tday.month


# Update function defined
def UpdateBudgetDisplay():
  global budgetyear, budgetmonth

  # ---- Monthly Budgets ----
  # for the monthly budget items, need to handle the case where nothing
  # has been spent so far.  So, get the budget categories and get the
  # sums of expenditures for each separately.
  
  sqlstatement =   "SELECT Trim(C.Name),C.Id,C.BudgetAmount,0 " + \
                   "FROM Categories " + \
                   "AS C WHERE C.BudgetAmount > 0 " + \
                   "AND C.BudgetPeriod = 1"
  cursor.execute(sqlstatement)
  BLines=cursor.fetchall()

  sqlstatement = ( "SELECT T.Category,SUM(T.Amount) from Transactions " + \
                   "as T INNER JOIN Categories AS C ON " + \
                   "T.Category = C.Id  WHERE Year(T.DateTrans) = %d " + \
                   "AND Month(T.DateTrans) = %02d AND C.BudgetAmount > 0 " + \
                   "AND C.BudgetPeriod=0 GROUP BY T.Category" ) \
                   % (budgetyear, budgetmonth)
  cursor.execute(sqlstatement)
  CLines=cursor.fetchall()

  for line in CLines:
    for x in BLines:
      if line[0] == x[1]:
        x[2] = line[1]
        break

  BudgetMLBm.delete(0,END)
  for line in BLines:
    print("m: line=%s,%s,%s,%s" % line)
    BudgetMLBm.insert(END,[line[0],line[2],float(line[2])-float(line[3])])
  BudgetMLBm.see(0)


  #--- Accumulating Budgets ---
  
  sqlstatement = ( "select Trim(C.Name),C.BudgetAmount," + \
                   "SUM(T.Amount) as Accumulation from Transactions as T " + \
                   "INNER JOIN Categories AS C ON T.Category = C.Id " + \
                   "where C.BudgetAmount > 0 AND C.BudgetPeriod=1 " + \
                   "GROUP BY C.Id" ) 
  cursor.execute(sqlstatement)
  BLines=cursor.fetchall()
  BudgetMLBa.delete(0,END)
  for line in BLines:
    print("line=%s,%s,%s" % line)
    BudgetMLBa.insert(END,line)
  BudgetMLBa.see(0)
  print('budget status updated')


# Now call the update function 
UpdateBudgetDisplay()


# enter event loop
mainloop()
