#! /opt/ActivePython-2.7/bin/python

import sys
import re # regular expressions
import MySQLdb
import numbers
import datetime

db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()

# Get lists of categories:
sqlstatement="select Id,Name,BudgetAmount,BudgetPeriod from Categories"
cursor.execute(sqlstatement)
Categories=cursor.fetchall()

def ty(flag):
  if flag == 1:
    return "accumulating"
  else:
    return "monthly"

print("Press enter to keep budget amount the same or enter a new number")
for a in Categories:
   print("%s  %.2f %s" % (a[1],a[2],ty(a[3])))
   val = sys.stdin.readline().rstrip()
   if len(val) > 0:
     val = float(val)
     print("enter m or a for monthly or accumulating style budget")
     t = sys.stdin.readline().rstrip()
     if t == "m":
       u = 0
     else:
       u = 1
     sqlstatement="UPDATE Categories SET BudgetAmount=%.2f,BudgetPeriod=%d WHERE Id=%d" % (val,u,a[0])
     cursor.execute(sqlstatement)
     Dummy=cursor.fetchall()
     

