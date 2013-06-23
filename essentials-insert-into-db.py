#! /usr/bin/python2

import MySQLdb
db=MySQLdb.connect(db='bookmarks')
cursor=db.cursor()

cursor.execute("""select i from urls where url=%s""",(url,))
index = cursor.fetchone()

if index == None:
    cursor.execute("""INSERT INTO urls VALUES (NULL, %s)""", (url,))
    cursor.fetchone()
    cursor.execute("""select i from urls where url=%s""",(url,))
    index = cursor.fetchone()

# with url index number, insert the link into the link table.

cursor.execute("""INSERT INTO entries VALUES (NULL, %s, %s)""", (location,str(index[0]),))
cursor.fetchone()
