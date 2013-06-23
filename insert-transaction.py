#! /usr/bin/python2

import sys
import re # regular expressions
import MySQLdb

db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()

# Get lists of accounts, types and categories:
sqlstatement="select Id,Name from Accounts"
cursor.execute(sqlstatement)
Accounts=cursor.fetchall()
# print("\nAccounts:")
# for a in Accounts:
#     print(a)

sqlstatement="select Id,Name from Categories"
cursor.execute(sqlstatement)
Categories=cursor.fetchall()
# print("\nCategories:")
# for a in Categories:
#     print(a)

sqlstatement="select Id,Name from TransTypes"
cursor.execute(sqlstatement)
Types=cursor.fetchall()
# print("\nTypes:")
# for a in Types:
#     print(a)
# print("-------------------------------------------------------")

Type=-1
Payee='"HyVee"'
Amount=25.02
Category=5
Memo='"This is a sample memo"'
Account=1
DateTrans='"2010-09-22"'
DateEnter=DateTrans

formatstr = """INSERT INTO Transactions VALUES """
formatstr = formatstr+"""(NULL,%d,%s,%.2f,%d,%s,%d,%s,%s)"""
# print(formatstr % (Type,Payee,Amount,Category,Memo,
#                           Account,DateTrans,DateEnter))
sqlstatement=formatstr % (Type,Payee,Amount,Category,Memo,
                          Account,DateTrans,DateEnter)
# cursor.execute(formatstr,(Type,Payee,Amount,Category,Memo,
#                           Account,DateTrans,DateEnter))
cursor.execute(sqlstatement)
cursor.fetchone()

# Now go back and list all transactions
sqlstatement="""select * from Transactions where Account=%d""" % (Account,)
cursor.execute(sqlstatement)
rows=cursor.fetchall()
for r in rows:
    print(r)


cursor.close()
db.close()
