#! /usr/bin/python

import csv
import sys
import re # regular expressions
import MySQLdb
import datetime

CategoryTranslationMap = { \
'automobile:gasoline': 'Gasoline', \
'automobile': 'Gasoline', \
'groceries': 'Groceries', \
'groceries:food': 'Groceries', \
'automobile:maintenance': 'Auto Repair', \
'gift giving': 'Gifts', \
'charitable dona': 'Charitable', \
'healthcare': 'Medical', \
'healthcare:dental': 'Medical', \
'healthcare:prescriptions': 'Medical', \
'adjustment': 'Miscellaneous', \
'bank charges': 'Miscellaneous', \
'bank charges:interest paid': 'Miscellaneous', \
'bills': 'Miscellaneous', \
'cash withdrawl': 'Miscellaneous', \
'cash withdrawal': 'Miscellaneous', \
'education': 'Miscellaneous', \
'education:books': 'Miscellaneous', \
'from karen': 'Miscellaneous', \
'': 'Miscellaneous', \
'clothing': 'Miscellaneous', \
'household': 'Miscellaneous', \
'household:furnishings': 'Miscellaneous', \
'investment inco:interest': 'Miscellaneous', \
'mom and dad': 'Rent Supp.', \
'credit cards': 'Debt Reduction', \
'bills:cable-satellite': 'Charter', \
'bills:electricity': 'RPU', \
'bills:telephone': 'Qwest', \
'wages & salary': 'Income', \
'karen pay': 'Income', \
'kevin-business': 'Income', \
'kevin-church' : 'Income', \
'mayo reimbursem': 'Income', \
'pet care:food': 'Pets', \
'postage and mai': 'Miscellaneous', \
'unforseen expen': 'Miscellaneous', \
'insurance': 'Auto Ins.', \
'vacation:lodging': 'Vacations' \
}
# unused categories
# '': 'Natural Gas' \
# '': 'Verizon' \
# '': 'Sunshine San.' \
# '': 'Post Bulletin' \
# '': 'Thrivent Ins.' \
# '': 'Lock-Away' \
# '': 'Hair Cuts' \


reslashes = re.compile('/')
todayparts = datetime.date.today()
today = '%4d-%02d-%02d' % (todayparts.year,todayparts.month,todayparts.day)
loaddatafilename = 'import-me.dat'
db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()

# Get lists of accounts, types and categories:
sqlstatement="select Id,Name from Accounts"
cursor.execute(sqlstatement)
xAccounts=cursor.fetchall()
Accounts={}
for (a,b) in xAccounts:
  Accounts[b]=a
  
sqlstatement="select Id,Name from Categories"
cursor.execute(sqlstatement)
xCategories=cursor.fetchall()
Categories={}
for (a,b) in xCategories:
  Categories[b]=a
  
sqlstatement="select Id,Name from TransTypes"
cursor.execute(sqlstatement)
xTypes=cursor.fetchall()
Types={}
for (a,b) in xTypes:
  Types[b]=a



fpo = open(loaddatafilename,'w')

# these two lines are linked
cr = csv.reader(open('Buchs Family Checkbook.csv','rb'), delimiter=',',quotechar='"')
# fields in this file are:
# "Num","Date","Payee","Category","S","Withdrawal","Deposit","Total","Comment"
#  r[0]  r[1]   r[2]    r[3]     r[4]  r[5]         r[6]      r[7]    r[8]

acct = Accounts['Mayo CU Checking']

minnum = 60000
maxnum = 1
atmcnt = 0
debcnt = 0
obsCategories = []

header = cr.next()

for r in cr:

  # --- Look at Transaction Type Field ---
  tt = r[0].lower()
  if r[0] == "":
    r[0] = int(Types["Electronic"])
  elif tt == "debit":
    debcnt += 1
    r[0] = int(Types["Debit"])
  elif tt == "atm":
    atmcnt += 1
    r[0] = int(Types["ATM"])
  elif "online" in tt:
    r[0] = int(Types["Electronic"])
  elif "charge" in tt:
    r[0] = int(Types["Electronic"])
  elif "bill" in tt:
    r[0] = int(Types["Electronic"])
  elif r[0] == ".":
    r[0] = int(Types["Electronic"])
  elif tt == "withdrawl":
    r[0] = int(Types["Electronic"])
  else:
    try:
      value = int(r[0])
    except:
      print('this transaction type slipped through:\n%s' % str(r))
      r[0] = int(Types["Electronic"])
    else:
      if value > maxnum: maxnum = value
      if value < minnum: minnum = value
      r[0] = value

  # --- Look at Date Field ---
  # should just have slashes
  dateparts = r[1].split('/')
  # are three parts specified?
  if len(dateparts) != 3:
    print('error: this date not good: %s',r[1])
  else:
    # check if a valid date using datetime
    try:
      datetime.date(int(dateparts[2]),int(dateparts[0]),int(dateparts[1]))
    except:
      print('error: this date not good: %s',r[1])
    r[1] = dateparts[2] + "-" + dateparts[0] + "-" + dateparts[1]

  # --- Look at Category Field ---
  #if r[3].lower() not in obsCategories:
  #  obsCategories.append(r[3].lower())
  try:
    newcat = CategoryTranslationMap[r[3].lower()]
  except:
    print('need a translation entry for category: %s' % r[3])
    newcat = 'Miscellaneous'
  r[3] = Categories[newcat]

  # ---- Look at Amounts fields - which one is populated ---
  if len(r[6]) == 0:
    if len(r[5]) == 0:
      print('things are bad on this line, both amounts are blank:\n%s' % str(r))
    else:
      amount = r[5]  # 5 is an expense
  else:
    amount = "-" + r[6] # 6 is a deposit

  # Check if it was reconciled, and if so, mark it
  if r[4] == "R":
    reconciled = 1
  else:
    reconciled = 0
    

# create table Transactions (Id bigint auto_increment primary key,
#     Type INTEGER not null,
#     Payee VARCHAR(40) not null,
#     Amount REAL not null,
#     Category Integer not null,
#     Memo VARCHAR(500),
#     Account Integer not null,
#     DateTrans Date not null,
#     DateEnter Date not null);
  

  # for importing a file, "\N" is NULL, and the fields should
  # be tab-delimited, but string should not have quotes.  The
  # leading, escaped \N is understood by MySQL as a NULL
  
  fpo.write('\\N\t%d\t%s\t%s\t%d\t%s\t%d\t%s\t%s\t%d\t%f\n' % \
        (r[0],r[2],amount,r[3],r[8],acct,r[1],today,reconciled,-1))

# -- Summary Operations ---

fpo.close()

# Could actually execute the SQL Load Data command here in this python script
# instead of manually entering it into mysql.  The LOAD DATA would be
# on the file that was just written but
# now that I am still developing this, I want to separate things.

sql="LOAD DATA LOCAL INFILE '" + loaddatafilename + "' into table Transactions"
status = cursor.execute(sql)
print('cursor status = %s' % str(status))
status = cursor.fetchone()
print('cursor fetchone status = %s' % str(status))

cursor.close()
db.close()

#print('Observed categories:')
#for oc in obsCategories:
#  print(oc)

  
