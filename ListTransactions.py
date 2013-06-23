#! /usr/bin/python2

import sys
import MySQLdb

pagesize=24

db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()

cursor.execute("""select * from Transactions""")

fullist = cursor.fetchall()
lines = 0
for index in fullist:
    print index
    lines += 1
    if lines == pagesize:
        print("press enter to continue")
        sys.stdin.readline()
        lines = 0

cursor.close()
db.close()

