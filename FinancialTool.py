#! /opt/ActivePython-2.7/bin/python

from Tkinter import *
import tkMessageBox
# from ttk import *  # overrides the Tk equivalent widgets
import sys
import re # regular expressions
import MySQLdb
import numbers
import datetime
import math

# Loading my personal libraries
# import sys
#sys.path.append('<your choice of path here>')
from MultiListboxRead import *

# Reconfigurable Section
commonbackground="#aba7d7"
cfont="Times 11" # favored font for content, as opposed to labels
ffont="Courier 10" # where I need fixed width
smfont="Times 9" # for mode line
AccumulatingBudgetStart = '"2010-09-01"'

# Main State Variable
EditingId=-1

if sys.platform == "linux2":
  bindkey='<Key-Return>'
else:
  bindkey='<Return>'

# Setting up dates -------------------------------------------------
# Get today's date info - want to force month to two digits in string
tday = datetime.date.today()
thismonth = "%02d" % tday.month
DateEnter = '"' + str(tday.year) + "-" + thismonth + "-" + \
            str(tday.day) + '"'
currentyear = str(tday.year)

# Function to adjust months ==================================
def monthadjust(month,year,delta):
  month -= 1  # adjust to be 0-11 for calculation, reverse later
  month += delta
  if delta > 0:
    while month > 11:
      year += 1
      month -= 12
  else:
    while month < 0:
      year -= 1
      month += 12
  month += 1 # undo adjustment
  return [month,year]

# now, get two months ago, beginning of the month
month,year = monthadjust(tday.month,tday.year,-2)
monthnum = "%02d" % month
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

num_accts = len(Accounts)
# find max column widths needed
max_accts = 0
for a in Accounts:
  if len(a[1]) > max_accts:
    max_accts = len(a[1])

max_cats = 0
for a in Categories:
  if len(a[1]) > max_cats:
    max_cats = len(a[1])



#------------------- Insert New Transaction -------------------------
def InsertNewTransaction(transtype,payee,amount,category,\
                         memostring,account,datevalue,DateEnter, \
                         sales_tax_value):
  reconciled=False
  insfmtstr =  "INSERT INTO Transactions VALUES "
  insfmtstr += "(NULL,%d,%s,%.2f,%d,%s,%d,%s,%s,%d,%d)"
  sqlstatement=insfmtstr % (transtype,payee,amount,category, \
                            memostring,account,datevalue,DateEnter, \
                            reconciled,sales_tax_value)
  cursor.execute(sqlstatement)
  status = cursor.fetchone()
  if not status == None:
    message = "I got an unusual return status from the database\ninsertion command.  I don't know what to do now\nbut please let my creator\nknow about this.\nstatus=" + str(status)
    tkMessageBox.showwarning('Warnings',message)


#--------------- Update Transaction ----------------------------
# used when editing a transaction

def UpdateTransaction(transtype,payee,amount,category,\
                         memostring,account,datevalue,DateEnter, \
                         sales_tax_value):

  global EditingId
  
  insfmtstr =  'UPDATE Transactions SET '
  insfmtstr += 'Type=%d,Payee=%s,Amount=%.2f,Category=%d,'
  insfmtstr += 'Memo=%s,Account=%d,DateTrans=%s,'
  insfmtstr += 'SalesTaxAmount=%d '
  insfmtstr += 'WHERE Id=%d'
  sqlstatement=insfmtstr % (transtype,payee,amount,category, \
                            memostring,account,datevalue, \
                            sales_tax_value,EditingId)
  cursor.execute(sqlstatement)
  status = cursor.fetchone()


#--------------- Process Transaction -------------------------
def ProcessTransaction(event):

  ignore = False
  message = "Cannot process input, note these warnings:\n"

  accounttuple = acct.curselection()
  if len(accounttuple) == 0:
    ignore = True
    message += "account not selected;\n"
  else:
    account = int(accounttuple[0])+1

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
    category = int(cattuple[0])+1
    
  datestr = date.get()  
  dateparts = datestr.split('/')
  if len(dateparts) < 2:
    ignore = True
    message += "need at least a month/day in date;\n"
  else:

    if len(dateparts) == 2:
      # just have month/day add in the current year before those
      dateparts.insert(0,currentyear)
    else:
      # if there are three parts given, then just assume they are
      # in the form month/day/year - reorder into year-month-day
      dateparts = (dateparts[2],dateparts[0],dateparts[1])

    # Next test to determine if this is a valid date
    try:
      datetest = datetime.date(int(dateparts[0]), \
                               int(dateparts[1]),int(dateparts[2]))
    except:
      ignore = True
      message += "date is not valid;\n"
    else:
      datevalue = '"' + dateparts[0] + "-" + dateparts[1] + "-" \
                  + dateparts[2] + '"'
      # tkMessageBox.showinfo('info','datevalue=' + datevalue)

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
      if exp_inc_state == 'expense':
        amount *= -1
    except:
      ignore = True
      message += "amount is invalid;\n"

  memostring = memo.get(1.0,END)
  memostring = memostring.strip()
  if len(memostring) == 0:
    memostring = '""'
  else:
    memostring = '"'+memostring+'"'
  
  if sales_tax.get() == True:
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
    if moderadiovar.get() == 0:
      InsertNewTransaction(transtype,payee,amount,category,\
                         memostring,account,datevalue,DateEnter, \
                         sales_tax_value)
    else:
      UpdateTransaction(transtype,payee,amount,category,\
                         memostring,account,datevalue,DateEnter, \
                         sales_tax_value)
    # these operations after a valid transaction clear out for the next
    pay.delete(0,END)
    amt.delete(0,END)
    memo.delete(1.0,END)

    # update the balance and transactions display
    UpdateBalances()
    UpdateTransactions()
    UpdateBudgetDisplay()

    
#----- End of ProcessTransaction --------------------------------------------

#----- ReturnToInsertMode ---------------------------------------------------
def ReturnToInsertMode():

  global EditingId
  
  pay.delete(0,END)
  amt.delete(0,END)
  memo.delete(1.0,END)
  date.delete(0,END)
  acct.selection_clear(0,END)
  typeradiovar.set(0)
  cat.selection_clear(0,END)
  EditingId = -1
  exp_inc_set('expense')  


#----- Edit Transaction --------------------------------------------------
def EditTransaction(event):

  global EditingId

  try:
    selection = Transactions_lb.get(Transactions_lb.curselection())
  except:
    return
  
  selectionbits = selection.split("|")
  datestr = selectionbits[0].strip()
  payee = selectionbits[1].strip()
  amount = selectionbits[2].strip() # at this point it is still a string
  account = selectionbits[3].strip()
  category = selectionbits[4].strip()
  
  # get the numbers for the account and category
  AccountIndex = -100
  CategoryIndex = -100
  for a in Accounts:
    if a[1] == account:
      AccountIndex = int(a[0])
      break

  for a in Categories:
    if a[1] == category:
      CategoryIndex = int(a[0])
      break

  # get the rest of the data from the database
  sqlstatement = ( 'SELECT Id,Type,Trim(Memo),SalesTaxAmount' + \
                 ' FROM Transactions where Payee="%s" AND Amount=%s AND'  + \
                 ' Category=%d AND Account=%d AND DateTrans="%s"' ) \
                  % (payee,amount,CategoryIndex,AccountIndex,datestr)
  cursor.execute(sqlstatement)
  seltrans=cursor.fetchall()
  if len(seltrans) > 1:
    tkMessageBox.showerror('Error','Got more than one transaction from ' + \
                           'the dB.\n' + \
                           'I don\'t know how to handle this.  Good bye.')
    exit()
  seltrans=seltrans[0]

  # Set up the GUI to edit this transaction
  acct.selection_clear(0,END)
  acct.selection_set(AccountIndex - 1)
  acct.see(AccountIndex - 1)
  typenum = int(seltrans[1])
  typeradiovar.set(typenum)
  cat.selection_clear(0,END)
  cat.selection_set(CategoryIndex - 1)
  cat.see(CategoryIndex - 1)
  dateparts=datestr.split("-")
  date.delete(0,END)
  date.insert(END,"/".join((dateparts[1],dateparts[2],dateparts[0])))
  pay.delete(0,END)
  pay.insert(END,payee)
  amt.delete(0,END)
  floatamount = float(amount)
  if floatamount < 0:
    exp_inc_set('expense')  
    floatamount *= -1
  else:
    exp_inc_set('income')
    
  amt.insert(END,floatamount)
  stamountv = float(seltrans[3])
  if stamountv < 0:
    stamount.set(0)
    sales_tax.set(False)
  else:
    stamount.set(stamountv)
    sales_tax.set(True)
  update_sales_tax
  memo.delete(1.0,END)
  if seltrans[2] != None:
    memo.insert(END,seltrans[2])
  EditingId = int(seltrans[0])
  moderadiovar.set(1)
  
#----- parsegeometry --------------------------------------------------
# handles the typical X-window geometry string

def parsegeometry(geometry):
    m = re.match("(\d+)x(\d+)([-+]\d+)([-+]\d+)", geometry)
    if not m:
        raise ValueError("failed to parse geometry string")
    return map(int, m.groups())

#----- constructgeometry --------------------------------------------------
# handles the typical X-window geometry string
# Ok to use the sign, except for -0, need special flag for that so use NaN
def constructgeometry(geolist):
  if math.isnan( geolist[2] ):
    if math.isnan( geolist[3] ):
      return "%dx%d-0-0" % (geolist[0],geolist[1])
    else:
      return "%dx%d-0%+d" % (geolist[0],geolist[1],geolist[3])
  else:
    if math.isnan( geolist[3] ):
      return "%dx%d%+d-0" % (geolist[0],geolist[1],geolist[2])
    else:
      return "%dx%d%+d%+d" % tuple(geolist)

#----- Main, action begins here ---------------------------------------

# Main window - place in the upper left          
win=Tk()
win.title("Financial Database - Enter Transactions")
win.configure(background=commonbackground)

# Maybe will need these some day
# screenwidth=Wm.winfo_screenwidth()
# screenheight=Wm.winfo_screenheight()

#-- Mode radio buttons --
mrbframe=Frame(master=win,background=commonbackground)
moderadiovar = IntVar()
moderadiovar.set(0)
Label(mrbframe,text="Mode:",background=commonbackground, \
      font=smfont).pack(side="left",pady=0)
Radiobutton(mrbframe,font=smfont,borderwidth=0,relief="flat", \
            variable=moderadiovar,value=0, \
            text="insert new",takefocus=0, \
            command=ReturnToInsertMode, \
            background=commonbackground).pack(side="left",pady=0)
Radiobutton(mrbframe,font=smfont,borderwidth=0,relief="flat", \
            variable=moderadiovar,value=1, \
            text="edit existing",takefocus=0, \
            background=commonbackground).pack(side="left", \
                                              pady=0)

#-- Account List --
aframe=Frame(master=win,background=commonbackground,borderwidth=1,\
             relief="groove")
acctlab=Label(aframe,text='Account',background=commonbackground,font=cfont)
acctlab.grid(row=0,column=0,sticky="nw")
acct=Listbox(aframe,font=cfont,height=8,width=max_accts, \
             exportselection=0)
acct.grid(row=1,column=0,sticky="nw")
i=0
for a in Accounts:
  acct.insert(i,a[1])
  i += 1
acct.bind(bindkey, ProcessTransaction)
acc_scroller = Scrollbar(aframe, orient='vertical', \
                         command=acct.yview,takefocus=0)
acct.config(yscrollcommand=acc_scroller.set)
acc_scroller.grid(row=1,column=1,sticky="news")

#-- Transaction Types --
tframe=Frame(master=win,background=commonbackground,borderwidth=1,\
             relief="groove")
typelab=Label(tframe, font=cfont, \
              text="Transaction Type", \
              background=commonbackground, \
              justify="left")
typelab.pack(anchor="nw")
typeradiovar = IntVar()
cnframe = Frame(master=tframe,background=commonbackground,borderwidth=0)
cnframe.pack(anchor="nw")
cknum=Entry(cnframe,font=cfont,textvariable=typeradiovar,width=7, \
            justify="right")
cknum.pack(anchor="nw",side="left")
cknum.bind(bindkey,ProcessTransaction)
cknumlab=Label(cnframe,font=cfont,text="ck. num",width=7, \
               background=commonbackground)
cknumlab.pack(anchor="nw",side="left")
i = 0
typerb=[]
for a in Types:
  typerb.append(Radiobutton(tframe,font=cfont,borderwidth=0,relief="flat", \
                            variable=typeradiovar,value=a[0], \
                            text=a[1],takefocus=0, \
                            background=commonbackground))
  typerb[i].pack(anchor='nw')
  i += 1
typeradiovar.set(0)

#-- Category List --
cframe=Frame(master=win,background=commonbackground)
catlab=Label(cframe,text="Category",background=commonbackground,font=cfont)
catlab.grid(row=0,column=0,sticky="n")
catlen = len(Categories)
needscrollbar = 0
if catlen > 15:
  catlen = 15
  needscrollbar = 1
cat=Listbox(cframe,width=max_cats,height=catlen,exportselection=0, \
            font=cfont)
cat.grid(row=1,column=0,sticky="n")
cat.bind(bindkey, ProcessTransaction)
for c in Categories:
  cat.insert(c[0],c[1])

if needscrollbar == 1:  
  cat_scroller = Scrollbar(cframe, orient='vertical', \
                           command=cat.yview,takefocus=0)
  cat.config(yscrollcommand=cat_scroller.set)
  cat_scroller.grid(row=1,column=1,sticky="news")

#-- Transaction Date and Expense/Income --
dframe=Frame(master=win,background=commonbackground)

dframe1=Frame(master=dframe,background=commonbackground,borderwidth=1, \
             relief="groove")
datelab=Label(dframe1,text='Date of purchase (mm/dd)', \
              justify="left",font=cfont, \
              background=commonbackground)
datelab.pack(anchor="nw",side="left")
date=Entry(dframe1,font=cfont,width=10)
date.pack(anchor="nw",side="left")
date.bind(bindkey, ProcessTransaction)
dframe1.pack(side="left",anchor="nw")

exp_inc_state = "expense"

#---- exp_inc_toggle - toggle the expense/income indicator button ---------

def exp_inc_toggle():
  global exp_inc_state
  if exp_inc_state == "expense":
     exp_inc_state = "income"
     exp_inc_but.configure(text="Income",bg="green")
  else:
     exp_inc_state = "expense"
     exp_inc_but.configure(text="Expense",bg="pink")

#---- exp_inc_set - sets the internal state of exp_inc_state to a specific
#     state.

def exp_inc_set(newstate):
  global exp_inc_state
  if newstate == "expense":
     exp_inc_state = "expense"
     exp_inc_but.configure(text="Expense",bg="pink")
  else:
     exp_inc_state = "income"
     exp_inc_but.configure(text="Income",bg="green")


exp_inc_but = Button(dframe,command=exp_inc_toggle,text="Expense", \
                     bg="pink",pady=4,padx=4)
exp_inc_but.pack(anchor="ne",side="right")

#-- Payee Name --
pframe=Frame(master=win,background=commonbackground,borderwidth=1, \
             relief="groove")
paylab=Label(pframe,text="Payee",background=commonbackground,font=cfont)
pay=Entry(pframe,font=cfont,width=35)
paylab.grid(row=0,column=0,sticky="nw")
pay.grid(row=0,column=1,sticky="news")
pay.bind(bindkey, ProcessTransaction)

#-- Payment Amount --
mframe=Frame(master=win,background=commonbackground,borderwidth=1, \
             relief="groove")
amtlab=Label(mframe,text="Amount",justify="left", \
             background=commonbackground,font=cfont)
amtlab.pack(anchor="nw",side="left")
amt=Entry(mframe,text="0.00",font=cfont,width=8,justify="right")
amt.pack(anchor="nw",side="left")
amt.bind(bindkey, ProcessTransaction)

#-- Sales Tax Owed --
# tiny little routine to couple sales tax items

#---- update_sales_tax --------------------------------------------------
# handle the change in sales tax window to allow entry box to be enabled
# if the check button is checked.

def update_sales_tax():
  if sales_tax.get() == True:
    stamt.config(state="normal")
  else:
    stamt.config(state="disabled")

sales_tax=BooleanVar()
sales_tax.set(False)
stamount=DoubleVar()
stamount.set(0)

stframe=Frame(master=mframe,background=commonbackground,borderwidth=1, \
              relief="groove")
stlabel=Label(stframe,text='Sales Tax',background=commonbackground, \
              font=cfont)
stsubframe=Frame(master=stframe,background=commonbackground)
stcheck=Checkbutton(stsubframe,command=update_sales_tax,variable=sales_tax, \
                    takefocus=False,background=commonbackground, \
                    relief="flat",borderwidth=0)
stamt=Entry(stsubframe,font=cfont,textvariable=stamount,width=7,\
            justify="right",state="disabled")
stlabel.pack(anchor="nw",side="left")
stcheck.pack(anchor="center",side="left")
stamt.pack(anchor="nw",side="left")
stsubframe.pack(anchor="nw")
stframe.pack(anchor="ne",side="right")

#-- Memo Field --
eframe=Frame(master=win,background=commonbackground,borderwidth=1, \
             relief="groove")
memolab=Label(eframe,text='Memo',background=commonbackground, font=cfont)
memolab.pack(anchor="nw",side="left")
memo=Text(eframe,font=cfont,height=2,width=35)
memo.pack(anchor="nw",side="left")
memo.bind(bindkey, ProcessTransaction)
memo.bind("<Key-Tab>","")

row=0
mrbframe.grid(row=row,column=0,columnspan=2,stick="nw")
cframe.grid(row=row,column=2,rowspan=6,sticky="n")
row += 1
aframe.grid(row=row,column=0,sticky="nw")
tframe.grid(row=row,column=1,sticky="nwe")
row += 1
dframe.grid(row=row,column=0,columnspan=2,sticky="nwe")
row += 1
pframe.grid(row=row,column=0,columnspan=2,sticky="nw")
row += 1
mframe.grid(row=row,column=0,columnspan=2,sticky="nwe")
row += 1
eframe.grid(row=row,column=0,columnspan=2,sticky="nw")


#--------------------------------------------------------------------
#------------ Now create display of Account Balances ----------------

Balances = Toplevel()
Balances.title("Account Balances")
BalancesMLB = MultiListBoxRead(Balances, (('Account', max_accts),  \
                                          ('Balance', 8        ) ), num_accts )
BalancesMLB.pack(expand=YES,fill=BOTH)


#---- UpdateBalances ------------------------------------------------

def UpdateBalances():
  sqlstatement="SELECT Trim(Accounts.Name),Sum(Transactions.Amount) FROM Transactions INNER JOIN Accounts WHERE Transactions.Account = Accounts.Id GROUP BY Transactions.Account"
  cursor.execute(sqlstatement)
  BalanceLines=cursor.fetchall()
  
  BalancesMLB.delete(0,END)
  for line in BalanceLines:
    if len(line) == 2:
      displayline = ( line[0], "% 8.2f" % line[1] )
      BalancesMLB.insert(END, displayline)


#------------ Display of Transactions of Current and Last Month------

# first get the payees to determine what the maximum size of payee field
# should be
sqlstatement='SELECT Trim(T.Payee) FROM Transactions AS T WHERE DateTrans >= ' + BeginLastMonth
cursor.execute(sqlstatement)
TLines = cursor.fetchall()
payeewidth = 0
for tl in TLines:
  w = len(tl[0])
  if w > payeewidth:
    payeewidth = w

Transactions = Toplevel()
Transactions.title('Transaction History')
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
Transactions_lb.bind("<Double-Button-1>", EditTransaction)

#---- UpdateTransactions -------------------------------------------------

def UpdateTransactions():
  sqlstatement= 'SELECT T.DateTrans,Trim(T.Payee),T.Amount,Trim(A.Name),' + \
                'Trim(C.Name) FROM Transactions AS T, Accounts AS A,' + \
                'Categories AS C WHERE T.Account = A.Id AND ' + \
                'T.Category = C.Id AND DateTrans >= ' + BeginLastMonth + \
                ' ORDER BY DateTrans'
  cursor.execute(sqlstatement)
  TLines=cursor.fetchall()
  Transactions_lb.delete(0,END)
  for line in TLines:
    if len(line) == 5:
      tx = ftext % line
      Transactions_lb.insert(END,tx)
  Transactions_lb.see(END)

  
#------------ Display of Budget Status ------

# tune window height by finding out how many of each of the budget-type
# items we have
sqlstatement =   "SELECT Count(C.BudgetAmount) FROM Categories " + \
               "AS C WHERE C.BudgetAmount > 0 AND C.BudgetPeriod = 0"
cursor.execute(sqlstatement)
cnt = cursor.fetchall()
monthlyheight = cnt[0][0]
# limit height
if monthlyheight > 5:
  monthlyheight = 5
  
sqlstatement =   "SELECT Count(C.BudgetAmount) FROM Categories " + \
               "AS C WHERE C.BudgetAmount > 0 AND C.BudgetPeriod = 1"
cursor.execute(sqlstatement)
cnt = cursor.fetchall()
accumheight = cnt[0][0]
if accumheight > 5:
  accumheight = 5
      
Budgets = Toplevel()
Budgets.title("Budget Status")
BudgetmLab = Label(Budgets,text="Monthly Budget Items",bg="yellow")
BudgetmLab.pack(fill="x")
BudgetMLBm = MultiListBoxRead(Budgets, \
                             ( ('Category', max_cats), \
                               ('Budget', 8),          \
                               ('Remaining', 8) ),
                              monthlyheight )
BudgetMLBm.pack(fill="x")

BudgetaLab = Label(Budgets,text="Accumulating Budget Items",bg="yellow")
BudgetaLab.pack(fill="x")
BudgetMLBa = MultiListBoxRead(Budgets, \
                             ( ('Category', max_cats), \
                               ('Addition/Month', 8),          \
                               ('Accumlation', 8) ), accumheight )
BudgetMLBa.pack(fill="x")

# Initially display the current month
budgetyear = tday.year
budgetmonth = tday.month


#---- UpdateBudgetDisplay -------------------------------------------------

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
                   "AND C.BudgetPeriod = 0 ORDER BY C.Id"
  cursor.execute(sqlstatement)
  BTLines=cursor.fetchall()

  # convert from Tuples to Lists so we can mess with it
  BLines = []
  for bt in BTLines:
    BLines.append(list(bt))
  

  sqlstatement = ( "SELECT T.Category,SUM(T.Amount) from Transactions " + \
                   "as T INNER JOIN Categories AS C ON " + \
                   "T.Category = C.Id  WHERE Year(T.DateTrans) = %d " + \
                   "AND Month(T.DateTrans) = %02d AND C.BudgetAmount > 0 " + \
                   "AND C.BudgetPeriod = 0 GROUP BY T.Category" ) \
                   % (budgetyear, budgetmonth)
  cursor.execute(sqlstatement)
  CLines=cursor.fetchall()

  for cline in CLines:
    for bline in BLines:
      if cline[0] == bline[1]:
        bline[3] = cline[1]
        break

  BudgetMLBm.delete(0,END)
  for bline in BLines:
    BudgetMLBm.insert(END,[bline[0],bline[2],float(bline[2])+float(bline[3])])
  BudgetMLBm.see(0)


  #--- Accumulating Budgets ---
  
  sqlstatement = ( 'select Trim(C.Name),C.BudgetAmount,' + \
                   '-1*SUM(T.Amount) as Accumulation ' + \
                   'from Transactions as T ' + \
                   'INNER JOIN Categories AS C ON T.Category = C.Id ' + \
                   'where C.BudgetAmount > 0 AND C.BudgetPeriod = 1 ' + \
                   'AND T.DateTrans > %s ' + \
                   'GROUP BY C.Id ORDER BY C.Id' ) % AccumulatingBudgetStart 
  cursor.execute(sqlstatement)
  BLines=cursor.fetchall()
  BudgetMLBa.delete(0,END)
  for bline in BLines:
    BudgetMLBa.insert(END,bline)
  BudgetMLBa.see(0)


# --- End of Function def UpdateBudgetDisplay() -----------------

#---- Adjust Window Positions ------------------------------------
def AdjustWindowPositions():
  global enterwingeo, balwingeo, tranwingeo, budwingeo
  
  win.update()
  geo=parsegeometry( win.geometry() )
  geo[2]=0
  geo[3]=0
  win.geometry( constructgeometry(geo) )
  enterwingeo=geo

  # put this Balances window below the main entry window,
  Balances.update()
  geo=parsegeometry( Balances.geometry() )
  geo[2]=0
  geo[3]=enterwingeo[1] + enterwingeo[3] + 40  # hopefully a gap of 40 pixels is enough
  Balances.geometry( constructgeometry(geo) )
  balwingeo=geo              
  
  Transactions.update()
  geo=parsegeometry( Transactions.geometry() )
  geo[2]=enterwingeo[0] + enterwingeo[2] + 20
  geo[3]=0
  Transactions.geometry( constructgeometry(geo) )
  tranwingeo=geo        

  Budgets.update()
  geo=parsegeometry( Budgets.geometry() )
  geo[2]=balwingeo[0] + balwingeo[2] + 20
  geo[3]=enterwingeo[1] + enterwingeo[3] + 40  # hopefully a gap of 40 pixels is enough
  Budgets.geometry( constructgeometry(geo) )
  budwingeo=geo        




# For initial setup
UpdateBalances()
UpdateTransactions()
UpdateBudgetDisplay()
AdjustWindowPositions()

# enter event loop
mainloop()
