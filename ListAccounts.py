#! /usr/bin/python2

import MySQLdb
db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()

cursor.execute("""select * from Accounts""")

# index = cursor.fetchone()
# print index

fullist = cursor.fetchall()
for index in fullist:
    print index

cursor.close()
db.close()

