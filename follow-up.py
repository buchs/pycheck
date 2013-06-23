#! /usr/bin/python
import csv
import sys
import re # regular expressions
import MySQLdb
import datetime
db=MySQLdb.connect(host="hope",user="buchs",passwd="buchs0",
                   db='Finance')
cursor=db.cursor()
sql="""select Id from Transactions where Type=-4 AND Payee="Opening Balance" AND Amount=-5456.84 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=30.60 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=35.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=21.77 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=35.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4753 AND Payee="Children's Worship Bulletins" AND Amount=16.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4754 AND Payee="Bethany Lutheran College" AND Amount=3974.00 AND Category=17 AND Memo="Lisa's Spring Tuition" AND Account=1 AND DateTrans="2006-01-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4756 AND Payee="Affinity 4" AND Amount=2.40 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-01-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-2641.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4757 AND Payee="American College of Musicians" AND Amount=94.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="paycheck" AND Amount=-617.16 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Dividend Credit" AND Amount=-1.93 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Account Adjustment" AND Amount=-262.85 AND Category=17 AND Memo="Adjustment we added in" AND Account=1 AND DateTrans="2006-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4758 AND Payee="Creative Communications" AND Amount=8.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4759 AND Payee="Ascension Lutheran Church" AND Amount=445.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4760 AND Payee="Aquila" AND Amount=138.74 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4761 AND Payee="Sam's Club Charge" AND Amount=93.68 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-02-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=145.62 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=36.97 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-583.44 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-02-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=34.01 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4762 AND Payee="Bank of America" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4763 AND Payee="American Express Blue" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4764 AND Payee="Midwest Wireless" AND Amount=116.33 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4765 AND Payee="Capital One Bank" AND Amount=330.47 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-2651.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4766 AND Payee="Ascension Lutheran Church" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4769 AND Payee="Brian Kom" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=30.54 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4767 AND Payee="Qwest" AND Amount=23.73 AND Category=17 AND Memo="This may be lost, never receive" AND Account=1 AND DateTrans="2006-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4768 AND Payee="MBNA America" AND Amount=226.80 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4770 AND Payee="Arlin Bornschlegle" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4771 AND Payee="Ascension Lutheran Church" AND Amount=1469.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4772 AND Payee="Chase Financial" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-3841.27 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.88 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-572.15 AND Category=17 AND Memo="Trip reimbursement for Feb 6." AND Account=1 AND DateTrans="2006-03-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to David" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=145.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-1183.33 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4774 AND Payee="Aquila" AND Amount=122.80 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4775 AND Payee="Sam's Club Charge" AND Amount=93.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-2811.41 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4776 AND Payee="Bank of America" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4777 AND Payee="American Express Blue" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4778 AND Payee="Midwest Wireless" AND Amount=131.40 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4779 AND Payee="Department Vehicle Services" AND Amount=39.50 AND Category=17 AND Memo="Volvo" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4780 AND Payee="Capital One Bank" AND Amount=677.52 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4781 AND Payee="MBNA America" AND Amount=135.72 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=32.02 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4782 AND Payee="Marci Sperber" AND Amount=65.84 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=47.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=38.44 AND Category=17 AND Memo="Camry gas" AND Account=1 AND DateTrans="2006-03-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-540.72 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=13.69 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4783 AND Payee="Chase Financial" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4784 AND Payee="Affinity 4" AND Amount=6.41 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="David" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4785 AND Payee="Ascension Lutheran Church" AND Amount=1460.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="Kevin for trip" AND Account=1 AND DateTrans="2006-03-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.39 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-03-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.17 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4786 AND Payee="American Express" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4787 AND Payee="Ascension Lutheran Church" AND Amount=65.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=29.12 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2006-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4788 AND Payee="Ascension Lutheran Church" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="paycheck" AND Amount=-1001.34 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=145.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="To David" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="To Lisa" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=56.81 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4789 AND Payee="Aquila" AND Amount=120.51 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4790 AND Payee="Waste Management" AND Amount=79.95 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-2811.41 AND Category=17 AND Memo="Trip reimbursement for Feb 6." AND Account=1 AND DateTrans="2006-04-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Bicycle Sports" AND Amount=26.95 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4791 AND Payee="United States Treasury" AND Amount=731.86 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4792 AND Payee="Minnesota Revenue" AND Amount=1.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4793 AND Payee="Bank of America" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4794 AND Payee="Taste of Home Books" AND Amount=23.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4795 AND Payee="Sam's Club Discover Card" AND Amount=185.26 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4796 AND Payee="Midwest Wireless" AND Amount=185.21 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4797 AND Payee="Bethany Lutheran College" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4798 AND Payee="Capital One Bank" AND Amount=1000.27 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4799 AND Payee="MBNA America" AND Amount=272.82 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Trip Reimbursement" AND Amount=-325.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4800 AND Payee="Ascension Lutheran Church" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.73 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2006-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4801 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-637.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4802 AND Payee="Post Master" AND Amount=200.97 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4804 AND Payee="Chase Financial" AND Amount=1440.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Paycheck + 1716.71 HC Reim" AND Amount=-4528.11 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-04-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4805 AND Payee="Post Master" AND Amount=28.62 AND Category=17 AND Memo="Will be reimbursed by church" AND Account=1 AND DateTrans="2006-04-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4806 AND Payee="Ascension Lutheran Church" AND Amount=1335.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=93.86 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.83 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MEFCU" AND Amount=27.00 AND Category=17 AND Memo="Safe Deposit Box" AND Account=1 AND DateTrans="2006-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter auto pay?" AND Amount=177.02 AND Category=1 AND Memo="Not sure if this is the card it" AND Account=1 AND DateTrans="2006-05-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=145.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano plus reimbursement 200.97" AND Amount=-517.02 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4807 AND Payee="Aquila" AND Amount=62.85 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4808 AND Payee="Midwest Wireless" AND Amount=145.61 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4809 AND Payee="Sam's Club Charge" AND Amount=590.29 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=38.55 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2006-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3811.40 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-05-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4810 AND Payee="Children's Worship Bulletins" AND Amount=16.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4811 AND Payee="Bank of America" AND Amount=3600.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4812 AND Payee="Capital One Bank" AND Amount=800.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4813 AND Payee="Target National Bank" AND Amount=215.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Zorbas" AND Amount=40.37 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4814 AND Payee="Ascension Lutheran Church" AND Amount=668.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-690.67 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4815 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4816 AND Payee="Leandra Hubka" AND Amount=15.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.40 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-05-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-05-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-440.40 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4817 AND Payee="Nick Rudlong" AND Amount=15.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4818 AND Payee="Chase Financial" AND Amount=764.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4819 AND Payee="MBNA America" AND Amount=108.87 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4820 AND Payee="Ascension Lutheran Church" AND Amount=668.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4821 AND Payee="American Express" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4822 AND Payee="Aquila" AND Amount=39.57 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MEFCU" AND Amount=200.00 AND Category=17 AND Memo="Safe Deposit Box" AND Account=1 AND DateTrans="2006-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.85 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MEFCU" AND Amount=160.00 AND Category=17 AND Memo="Safe Deposit Box" AND Account=1 AND DateTrans="2006-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="" AND Amount=-220.88 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=147.09 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.73 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=87.66 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2006-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-215.81 AND Category=17 AND Memo="Trip reimbursement for May 25" AND Account=1 AND DateTrans="2006-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-2811.40 AND Category=17 AND Memo="Paycheck" AND Account=1 AND DateTrans="2006-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4823 AND Payee="Bank of America" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4824 AND Payee="Sam's Club Discover Card" AND Amount=354.41 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4825 AND Payee="Midwest Wireless" AND Amount=111.62 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4826 AND Payee="Capital One Bank" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4827 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MEFCU" AND Amount=100.00 AND Category=17 AND Memo="Safe Deposit Box" AND Account=1 AND DateTrans="2006-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-734.60 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4828 AND Payee="Target" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-508.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4829 AND Payee="MBNA America" AND Amount=74.73 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4830 AND Payee="Affinity 4" AND Amount=1.13 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-06-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.40 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4831 AND Payee="Chase Financial" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4832 AND Payee="Aquila" AND Amount=31.79 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4834 AND Payee="DVS - Camry" AND Amount=103.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4835 AND Payee="Ascension Lutheran Church" AND Amount=1335.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="To David" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4836 AND Payee="Sam's Club" AND Amount=135.87 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-389.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-2811.41 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4837 AND Payee="Ascension Lutheran Church" AND Amount=50.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=71.97 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2006-07-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Trip Reimbursement" AND Amount=-565.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4838 AND Payee="Waste Management" AND Amount=81.16 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4839 AND Payee="Sam's Club Discover Card" AND Amount=201.56 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4840 AND Payee="Midwest Wireless" AND Amount=99.94 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4841 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4842 AND Payee="Bank of America" AND Amount=2588.23 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4843 AND Payee="Capital One Bank" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=138.21 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-734.21 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4844 AND Payee="Gordon Krueger" AND Amount=175.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4845 AND Payee="Target National Bank" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.67 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.39 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-07-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="paycheck minus 250 cash" AND Amount=-383.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4846 AND Payee="Schmidt Music" AND Amount=125.90 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4847 AND Payee="Affinity 4" AND Amount=19.74 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4848 AND Payee="MBNA America" AND Amount=55.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4850 AND Payee="Chase Financial" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4851 AND Payee="Voided" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4852 AND Payee="Ascension Lutheran Church" AND Amount=1335.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4853 AND Payee="Lutheran Heritage Foundation" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Church Reimbursement" AND Amount=-578.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4854 AND Payee="Mr. Pizza" AND Amount=26.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.41 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-08-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Liberty Check" AND Amount=21.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4855 AND Payee="MN Energy Resources" AND Amount=27.56 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4856 AND Payee="Sam's Club Discover Card" AND Amount=100.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4857 AND Payee="Children's Worship Bulletins" AND Amount=16.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4858 AND Payee="Capital One Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4859 AND Payee="Voided" AND Amount=500.00 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4860 AND Payee="Midwest Wireless" AND Amount=98.46 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4861 AND Payee="Ascension Lutheran Church" AND Amount=623.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=135.22 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4862 AND Payee="MTNA" AND Amount=99.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4863 AND Payee="American College of Musicians" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4864 AND Payee="Real Simple" AND Amount=24.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="paycheck+151.44 toyota" AND Amount=-803.55 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4865 AND Payee="Gordon Krueger" AND Amount=150.00 AND Category=17 AND Memo="Dog Sitting" AND Account=1 AND DateTrans="2006-08-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=57.97 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2006-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.67 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2006-08-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.39 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HMM Reimb" AND Amount=-50.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4866 AND Payee="Target" AND Amount=1000.00 AND Category=17 AND Memo="Watch - Kevin" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4867 AND Payee="Schmidt Music" AND Amount=118.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4868 AND Payee="Kohl's" AND Amount=184.55 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4869 AND Payee="MBNA America" AND Amount=130.69 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4870 AND Payee="Chase Financial" AND Amount=1635.59 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4871 AND Payee="Ascension Lutheran Church" AND Amount=623.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=75.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-08-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Money to Lisa and David" AND Amount=260.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2889.43 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-08-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-689.01 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-08-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4872 AND Payee="Ascension Lutheran Church" AND Amount=625.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-09-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4873 AND Payee="MN Energy Resources" AND Amount=26.44 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2006-09-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4874 AND Payee="Midwest Wireless" AND Amount=100.69 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-09-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=139.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Optima" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4875 AND Payee="Sam's Club Discover Card" AND Amount=71.12 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4901 AND Payee="Bank of America" AND Amount=102.47 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.40 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-290.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-286.61 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4902 AND Payee="Capital One Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4903 AND Payee="Chase Financial Toyota" AND Amount=50.00 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4904 AND Payee="Kohl's" AND Amount=221.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4905 AND Payee="Target National Bank" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=22.04 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2006-09-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-09-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4906 AND Payee="MBNA America" AND Amount=662.62 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4907 AND Payee="Schmidt Music" AND Amount=118.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2006-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4908 AND Payee="Affinity 4" AND Amount=3.27 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4909 AND Payee="Reiman Publications" AND Amount=23.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=57.97 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2006-09-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2811.40 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-09-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4910 AND Payee="Chase Financial" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.67 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2006-09-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Trip Reimbursement" AND Amount=-1078.22 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-301.13 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.81 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-09-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4911 AND Payee="Ascension Lutheran Church" AND Amount=1264.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-10-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4912 AND Payee="Thrivent" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4913 AND Payee="MN Energy Resources" AND Amount=27.24 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2006-10-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4914 AND Payee="Bank Card Center - Simmons" AND Amount=369.36 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-1531.23 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4915 AND Payee="Waste Management" AND Amount=80.28 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4916 AND Payee="Bank of America" AND Amount=137.54 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4917 AND Payee="Sam's Club Discover Card" AND Amount=204.18 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=139.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3080.94 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-10-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=57.97 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2006-10-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4918 AND Payee="VOID Void" AND Amount=57.97 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4919 AND Payee="Chase Financial-Kevin" AND Amount=1955.60 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4920 AND Payee="Capital One Bank" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4921 AND Payee="MBNA America" AND Amount=194.44 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4922 AND Payee="Midwest Wireless" AND Amount=103.32 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4923 AND Payee="Kohl's" AND Amount=65.68 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4924 AND Payee="Schmidt Music" AND Amount=118.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4925 AND Payee="Target" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4926 AND Payee="Chase Financial-Karen" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-77.30 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-10-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3101.16 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-10-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4927 AND Payee="Gordon Krueger" AND Amount=150.00 AND Category=17 AND Memo="Dog Sitting" AND Account=1 AND DateTrans="2006-10-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4928 AND Payee="MN Energy Resources" AND Amount=33.63 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2006-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4929 AND Payee="Simmons First National Bank" AND Amount=234.72 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4930 AND Payee="Country Books" AND Amount=19.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4931 AND Payee="Taste of Home Books" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4932 AND Payee="VOID Central College Abroad" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4933 AND Payee="Central College" AND Amount=350.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4934 AND Payee="Central College" AND Amount=175.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.93 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-10-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=54.63 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2006-11-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="" AND Amount=-442.86 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to kids" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4935 AND Payee="Ascension Lutheran Church" AND Amount=1256.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4936 AND Payee="Mayo Health Care" AND Amount=23.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.58 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2006-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=103.86 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3101.16 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-11-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4937 AND Payee="Pizza Man" AND Amount=25.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4938 AND Payee="Sam's Club Discover Card" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4939 AND Payee="Bank of America" AND Amount=229.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4940 AND Payee="Chase Financial Toyota" AND Amount=740.69 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4941 AND Payee="Midwest Wireless" AND Amount=112.97 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4942 AND Payee="Capital One Bank" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo" AND Amount=-231.26 AND Category=17 AND Memo="trip reimbursement for Oct 18" AND Account=1 AND DateTrans="2006-11-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4943 AND Payee="NPH" AND Amount=78.77 AND Category=17 AND Memo="books" AND Account=1 AND DateTrans="2006-11-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4948 AND Payee="Children's Worship Bulletins" AND Amount=16.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4944 AND Payee="Kohl's" AND Amount=70.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4945 AND Payee="Schmidt Music" AND Amount=118.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2006-11-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4946 AND Payee="Target" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3101.16 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay+ Traveler's Cheques" AND Amount=-597.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-11-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Trip Reimbursement" AND Amount=-676.39 AND Category=17 AND Memo="For EPEP trip" AND Account=1 AND DateTrans="2006-11-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4949 AND Payee="Ascension Lutheran Church" AND Amount=1264.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-11-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.58 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2006-11-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4947 AND Payee="Chase Financial-Karen" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-429.03 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2006-11-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4950 AND Payee="DVS - Plymouth" AND Amount=39.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4951 AND Payee="MMTA - Piano Prelims" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Woodman's" AND Amount=46.15 AND Category=17 AND Memo="Von Steihl" AND Account=1 AND DateTrans="2006-11-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-11-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-154.26 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2006-12-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4952 AND Payee="MN Energy Resources" AND Amount=62.23 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2006-12-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4953 AND Payee="Bank Card Center - Simmons" AND Amount=1543.03 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4954 AND Payee="Bank of America 2154" AND Amount=76.78 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4955 AND Payee="Sam's Club Discover Card" AND Amount=90.15 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4956 AND Payee="Midwest Wireless" AND Amount=136.71 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2006-12-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4957 AND Payee="Taste of Home Books" AND Amount=31.95 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4958 AND Payee="NPH" AND Amount=39.84 AND Category=17 AND Memo="books" AND Account=1 AND DateTrans="2006-12-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3101.15 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-12-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=128.71 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4959 AND Payee="Ascension Lutheran Church" AND Amount=623.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=58.00 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2006-12-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="paycheck minus 450 cash" AND Amount=-41.61 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Paycheck + 783.19 HC Reimn" AND Amount=-4184.35 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2006-12-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4960 AND Payee="cascade animal medical center" AND Amount=48.01 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2006-12-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4961 AND Payee="HyVee" AND Amount=111.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.58 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2006-12-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2006-12-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-650.42 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4962 AND Payee="Capital One Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4963 AND Payee="Chase Financial-Kevin" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4964 AND Payee="Bank of America" AND Amount=332.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4965 AND Payee="HyVee" AND Amount=98.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4966 AND Payee="Target National Bank" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4967 AND Payee="Chase Financial-Karen" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4968 AND Payee="Schmidt Music" AND Amount=118.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4969 AND Payee="Simmons First National Bank" AND Amount=253.42 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4970 AND Payee="Ascension Lutheran Church" AND Amount=623.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2006-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4972 AND Payee="Mr. Pizza" AND Amount=44.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2006-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4971 AND Payee="Void" AND Amount=-1.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-4246.93 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-01-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=122.78 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Register of deeds" AND Amount=12.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Minnesota Energy Resources" AND Amount=108.46 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-01-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=58.00 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2007-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="paycheck" AND Amount=-18.22 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4973 AND Payee="Ascension Lutheran Church" AND Amount=623.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2007-01-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4974 AND Payee="Kohl's" AND Amount=118.88 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4975 AND Payee="Bank of America" AND Amount=122.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4976 AND Payee="Waste Management" AND Amount=83.60 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4977 AND Payee="Midwest Wireless" AND Amount=100.90 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4978 AND Payee="Chase Financial-Kevin" AND Amount=613.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4979 AND Payee="Capital One Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4980 AND Payee="Ascension Lutheran Church" AND Amount=25.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=400.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club" AND Amount=170.40 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2825.71 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4981 AND Payee="Schmidt Music" AND Amount=118.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4982 AND Payee="Affinity 4" AND Amount=7.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4983 AND Payee="Target National Bank" AND Amount=1500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4984 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4985 AND Payee="Marriott" AND Amount=100.00 AND Category=23 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express-Hilton" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.61 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-01-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4986 AND Payee="Shannon Scharf" AND Amount=17.18 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Unknown" AND Amount=24.26 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Trip Reimbursement" AND Amount=-954.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4987 AND Payee="Ascension Lutheran Church" AND Amount=50.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2007-01-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2903.75 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-01-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-1090.43 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-02-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4988 AND Payee="Ascension Lutheran Church" AND Amount=1246.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2007-02-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=104.01 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-02-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=120.57 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Hilton" AND Amount=973.13 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=31.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4989 AND Payee="Reiman Publications" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4990 AND Payee="Kohl's" AND Amount=104.73 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4991 AND Payee="Midwest Wireless" AND Amount=182.75 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2007-02-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-426.61 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="from lisa" AND Amount=-650.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to David" AND Amount=650.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=62.01 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2007-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2825.72 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4994 AND Payee="Ascension Lutheran Church" AND Amount=623.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2007-02-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Lisa" AND Amount=400.00 AND Category=17 AND Memo="Lisa checking" AND Account=1 AND DateTrans="2007-02-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-186.62 AND Category=20 AND Memo="Took 200.00 in cash on checks t" AND Account=1 AND DateTrans="2007-02-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4993 AND Payee="Capital One Bank" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.61 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-02-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4992 AND Payee="Chase Financial Subaru" AND Amount=357.26 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4995 AND Payee="Target National Bank" AND Amount=1000.00 AND Category=17 AND Memo="Credit card payment" AND Account=1 AND DateTrans="2007-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4996 AND Payee="Schmidt Music" AND Amount=118.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2007-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4997 AND Payee="Bethany Lutheran College" AND Amount=150.00 AND Category=17 AND Memo="Donation" AND Account=1 AND DateTrans="2007-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Trip Reimbursement" AND Amount=-210.16 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2825.71 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-02-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.12 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=37.76 AND Category=10 AND Memo="Onalaska" AND Account=1 AND DateTrans="2007-03-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=750.00 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-03-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Hilton" AND Amount=1.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=123.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Trip Reimbursement" AND Amount=-1686.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-272.61 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Lisa" AND Amount=500.00 AND Category=17 AND Memo="Lisa checking" AND Account=1 AND DateTrans="2007-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4998 AND Payee="Taste of Home Books" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=62.01 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2007-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4999 AND Payee="Ascension Lutheran Church" AND Amount=18.99 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2007-03-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2982.76 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-03-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=14.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5000 AND Payee="Midwest Wireless" AND Amount=51.14 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2007-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5001 AND Payee="Schmidt Music" AND Amount=883.55 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2007-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5002 AND Payee="Capital One Bank" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5003 AND Payee="Target National Bank" AND Amount=2500.00 AND Category=17 AND Memo="Credit card payment" AND Account=1 AND DateTrans="2007-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5004 AND Payee="Ascension Lutheran Church" AND Amount=500.00 AND Category=17 AND Memo="Pastor Luetke" AND Account=1 AND DateTrans="2007-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=415.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.61 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-03-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Pump and Munch" AND Amount=44.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5005 AND Payee="Charity Luetke" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5006 AND Payee="Ascension Lutheran Church" AND Amount=135.00 AND Category=17 AND Memo="Zebadiah's Tuition for March" AND Account=1 AND DateTrans="2007-03-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2982.76 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-03-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.26 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-455.15 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=500.00 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="To Lisa" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="To David" AND Amount=600.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5007 AND Payee="Matthew Luetke" AND Amount=35.00 AND Category=17 AND Memo="Defurminator" AND Account=1 AND DateTrans="2007-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5008 AND Payee="American College of Musicians" AND Amount=38.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=123.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-65.53 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5009 AND Payee="Ascension Lutheran Church" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Menards" AND Amount=9.60 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=123.38 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5010 AND Payee="Ascension Lutheran Church" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=23.99 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-04-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2982.76 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-04-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=62.01 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2007-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5011 AND Payee="Ascension Lutheran Church" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5013 AND Payee="MN Revenue" AND Amount=26.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="United States Treasury" AND Amount=408.29 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Pump and Munch" AND Amount=37.30 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5014 AND Payee="Capital One Bank" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5015 AND Payee="Midwest Wireless" AND Amount=83.00 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2007-04-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5016 AND Payee="Schmidt Music" AND Amount=6.95 AND Category=17 AND Memo="Saxophone" AND Account=1 AND DateTrans="2007-04-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=80.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-166.23 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-04-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kevin Pay" AND Amount=-4251.31 AND Category=17 AND Memo="includes 1268.55 Healthcare Rei" AND Account=1 AND DateTrans="2007-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5017 AND Payee="Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="Credit card payment" AND Account=1 AND DateTrans="2007-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Karen's new accounts" AND Amount=110.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.73 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-04-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=181.54 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.71 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="safe deposit box" AND Amount=27.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=500.00 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial Subaru" AND Amount=10.95 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=64.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-05-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=-221.97 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Error - undetermined" AND Amount=32.72 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=123.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3402.48 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-05-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=40.00 AND Category=17 AND Memo="Kevin" AND Account=1 AND DateTrans="2007-05-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=62.01 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2007-05-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=281.78 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5018 AND Payee="Capital One Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5019 AND Payee="Mr. Pizza" AND Amount=25.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5020 AND Payee="Void" AND Amount=25.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=21.94 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5021 AND Payee="Louise Sherwood" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5022 AND Payee="Midwest Wireless" AND Amount=119.54 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2007-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.73 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2408.76 AND Category=20 AND Memo="includes $2424.40 purchased pto" AND Account=1 AND DateTrans="2007-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5023 AND Payee="Mayo Clinic - MMSI" AND Amount=183.52 AND Category=16 AND Memo="Refund of overpayment on Dental" AND Account=1 AND DateTrans="2007-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5024 AND Payee="Chase Financial-Karen" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5025 AND Payee="" AND Amount=10.71 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=-656.97 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.18 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=1.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Error - undetermined" AND Amount=248.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Kevin" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2408.76 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-06-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="To Lisa" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to David" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=112.51 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-496.97 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=55.59 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=64.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=45.66 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=40.54 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=81.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-295.13 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Waste Management" AND Amount=86.72 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5051 AND Payee="DVS - Camry" AND Amount=103.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="Credit card payment" AND Account=1 AND DateTrans="2007-06-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2408.76 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-06-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=61.97 AND Category=1 AND Memo="AutoPay - Kevin entered this 7/" AND Account=1 AND DateTrans="2007-06-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=39.71 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-06-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5052 AND Payee="Affinity 4" AND Amount=11.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=500.00 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=1365.02 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.73 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-06-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=0.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=62.01 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2007-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Karen Pay" AND Amount=-924.72 AND Category=17 AND Memo="100 went to cash, 100 went to l" AND Account=1 AND DateTrans="2007-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Error - undetermined" AND Amount=-1.92 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=350.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2408.76 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-07-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=80.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=107.73 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5026 AND Payee="Midwest Wireless" AND Amount=218.64 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2007-07-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5027 AND Payee="Void" AND Amount=218.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=64.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Trip Reimbursement" AND Amount=-550.00 AND Category=17 AND Memo="For EPEP trip" AND Account=1 AND DateTrans="2007-07-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="from lisa" AND Amount=-300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-585.04 AND Category=17 AND Memo="took $60 cash" AND Account=1 AND DateTrans="2007-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.71 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=33.21 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2408.77 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-07-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="ISJ Clinic" AND Amount=25.83 AND Category=16 AND Memo="Confirmation: 6QS76-BSZNF, paym" AND Account=1 AND DateTrans="2007-07-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=20.58 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Corporate Payment Services" AND Amount=550.00 AND Category=17 AND Memo="Online Bill Payment, requested" AND Account=1 AND DateTrans="2007-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="IRA" AND Amount=-18132.30 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Karen Pay" AND Amount=-352.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=220.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=22.25 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-07-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=23.67 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-07-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-157.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="Credit card payment" AND Account=1 AND DateTrans="2007-07-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=80.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=500.00 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=24.92 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=9.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2487.97 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-2.49 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=106.39 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5029 AND Payee="Justin Buchs Hammonds" AND Amount=170.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5030 AND Payee="Country Books" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5031 AND Payee="Midwest Wireless" AND Amount=267.77 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Napa" AND Amount=52.30 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.75 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=97.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=61.83 AND Category=1 AND Memo="" AND Account=1 AND DateTrans="2007-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Home Equity Loan" AND Amount=-20598.87 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Trip Reimbursement" AND Amount=-164.90 AND Category=17 AND Memo="For EPEP trip" AND Account=1 AND DateTrans="2007-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-170.88 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5028 AND Payee="" AND Amount=20.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=21.38 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=9351.41 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=2953.24 AND Category=17 AND Memo="Credit card payment" AND Account=1 AND DateTrans="2007-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2125.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=3449.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2408.77 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-08-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Health Care" AND Amount=347.12 AND Category=16 AND Memo="Paid in Full - July 28, 2007 bi" AND Account=1 AND DateTrans="2007-08-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5032 AND Payee="Precious Is the Child Preschool" AND Amount=100.00 AND Category=17 AND Memo="IRA Rollover - Part 3 of 3" AND Account=1 AND DateTrans="2007-08-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5053 AND Payee="Franklin Templeton Bank & Trust" AND Amount=8136.07 AND Category=17 AND Memo="IRA Rollover - Part 1 of 3" AND Account=1 AND DateTrans="2007-08-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5054 AND Payee="Evergreen Investments" AND Amount=5000.00 AND Category=17 AND Memo="IRA Rollover - Part 2 of 3" AND Account=1 AND DateTrans="2007-08-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=27.21 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Karen's Checking" AND Amount=-375.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay + Reimbursement" AND Amount=-961.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic" AND Amount=347.12 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=75.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=124.91 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=64.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=5000.00 AND Category=17 AND Memo="Kevin IRA" AND Account=1 AND DateTrans="2007-08-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=40.80 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Bicycle Sports" AND Amount=32.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3212.98 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-08-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=786.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-5.27 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-08-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Marketplace" AND Amount=25.00 AND Category=17 AND Memo="Healing Depression and Anxiety" AND Account=1 AND DateTrans="2007-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Our Redeemer Lutheran Church" AND Amount=50.00 AND Category=15 AND Memo="Kevin Church" AND Account=1 AND DateTrans="2007-09-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=109.12 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5033 AND Payee="Ascension Lutheran Church" AND Amount=375.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5034 AND Payee="Bethany Lutheran College" AND Amount=3949.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Center for Massage Therapy" AND Amount=71.88 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2007-09-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-160.93 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=10.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="oops" AND Amount=-347.12 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=43.31 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=75.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=787.42 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2408.76 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-09-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5035 AND Payee="Bethany Lutheran College" AND Amount=375.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=2304.15 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=1022.72 AND Category=17 AND Memo="Credit card payment" AND Account=1 AND DateTrans="2007-09-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-09-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=61.83 AND Category=1 AND Memo="" AND Account=1 AND DateTrans="2007-09-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.73 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-09-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2733.95 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-09-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=157.38 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-09-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-2.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5056 AND Payee="Thrivent" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-09-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=58.27 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-10-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=1014.88 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Trip Reimbursement" AND Amount=-400.00 AND Category=20 AND Memo="ICCD Conf. Registration" AND Account=1 AND DateTrans="2007-10-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-330.15 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=109.12 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="Kevin for trip" AND Account=1 AND DateTrans="2007-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2713.92 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-10-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5057 AND Payee="NPH" AND Amount=126.32 AND Category=17 AND Memo="books" AND Account=1 AND DateTrans="2007-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=61.83 AND Category=1 AND Memo="" AND Account=1 AND DateTrans="2007-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Waste Management" AND Amount=88.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=66.22 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=97.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2007-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-407.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-10-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Capital One Bank" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target National Bank" AND Amount=607.49 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="GE Card" AND Amount=673.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Blue" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Optima" AND Amount=93.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo paycheck" AND Amount=-2713.93 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-10-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Trip Reimbursement" AND Amount=-944.65 AND Category=20 AND Memo="Last part of Lake Tahoe trip" AND Account=1 AND DateTrans="2007-10-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Arrow Hardware" AND Amount=8.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5037 AND Payee="Immanuel-St. Joseph Clinic" AND Amount=143.10 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2007-10-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.68 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-10-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5060 AND Payee="??" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="??" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Trip Reimbursement" AND Amount=-495.00 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic Pharmacy" AND Amount=46.40 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=208.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Unknown" AND Amount=124.48 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=-708.47 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Adjustment to Balance to Current" AND Amount=13.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=97.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.71 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Unknown" AND Amount=8.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Unknown" AND Amount=30.58 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="walmart" AND Amount=26.77 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Unknown" AND Amount=26.40 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=211.66 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=101.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=106.43 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2713.93 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-11-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="To Lisa" AND Amount=450.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Karen's Checking" AND Amount=-1200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-85.48 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=452.87 AND Category=16 AND Memo="Confirmation Number: MMCRPB0000" AND Account=1 AND DateTrans="2007-11-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Woodman's" AND Amount=84.08 AND Category=17 AND Memo="Von Steihl" AND Account=1 AND DateTrans="2007-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Woodman's" AND Amount=56.47 AND Category=17 AND Memo="Von Steihl" AND Account=1 AND DateTrans="2007-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=20.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=61.83 AND Category=1 AND Memo="" AND Account=1 AND DateTrans="2007-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5062 AND Payee="Telephone" AND Amount=2.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5063 AND Payee="NPH" AND Amount=30.99 AND Category=17 AND Memo="books" AND Account=1 AND DateTrans="2007-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5064 AND Payee="Ascension Lutheran Church" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5065 AND Payee="Ascension Lutheran Church" AND Amount=725.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5066 AND Payee="??" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Fleet Farm" AND Amount=10.58 AND Category=17 AND Memo="toilet seat" AND Account=1 AND DateTrans="2007-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kwik Trip" AND Amount=20.16 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-11-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-207.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="GE Card" AND Amount=707.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=91.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=151.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.74 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2713.92 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-11-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5038 AND Payee="NPH" AND Amount=39.50 AND Category=17 AND Memo="books" AND Account=1 AND DateTrans="2007-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5061 AND Payee="Raache" AND Amount=44.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic Pharmacy" AND Amount=10.00 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2007-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5067 AND Payee="Oronoco Auto Parts" AND Amount=1114.75 AND Category=10 AND Memo="Purchase of Olds 98" AND Account=1 AND DateTrans="2007-11-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="BP Gas" AND Amount=48.36 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-11-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=503.60 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=926.48 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=3725.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kwik Trip" AND Amount=38.04 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2007-11-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic Pharmacy" AND Amount=29.95 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2007-11-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic Pharmacy" AND Amount=11.47 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2007-11-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Correction" AND Amount=-468.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-11-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3642.34 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-12-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=46.00 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=124.17 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.72 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2007-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=49.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5039 AND Payee="" AND Amount=46.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5040 AND Payee="" AND Amount=27.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5042 AND Payee="" AND Amount=26.85 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=117.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic" AND Amount=20.16 AND Category=16 AND Memo="David's Bill, paid in full, Con" AND Account=1 AND DateTrans="2007-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=61.82 AND Category=1 AND Memo="" AND Account=1 AND DateTrans="2007-12-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-702.00 AND Category=20 AND Memo="Prescription 51.61, Karen churc" AND Account=1 AND DateTrans="2007-12-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2713.92 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2007-12-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=939.69 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2007-12-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=97.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-157.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Karen's Checking" AND Amount=-1500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="To Lisa" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kevin Church" AND Amount=-4294.38 AND Category=17 AND Memo="pay out from savings" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5041 AND Payee="Brian Kom" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5043 AND Payee="Bethany Lutheran College" AND Amount=2000.00 AND Category=20 AND Memo="Donation" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5044 AND Payee="Zion Lutheran Church" AND Amount=1800.00 AND Category=20 AND Memo="donation" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5068 AND Payee="Tony Nowak" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5069 AND Payee="Kristine Nowak" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5070 AND Payee="Leanne Holdorf" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5071 AND Payee="Alan Holdorf" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5072 AND Payee="Kathy Holdorf" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5073 AND Payee="Brian McFadden" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5074 AND Payee="Daniel McFadden" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5075 AND Payee="Matthew Luetke" AND Amount=150.00 AND Category=17 AND Memo="Defurminator" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=220.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=1223.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2359.28 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Marriott Chase" AND Amount=109.98 AND Category=20 AND Memo="Trip to Rockville" AND Account=1 AND DateTrans="2007-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kevin Pay" AND Amount=-2797.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Account Adjustment" AND Amount=0.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=287.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2007-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="Kevin-Church reconcilliation" AND Account=1 AND DateTrans="2008-01-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=90.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=123.71 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=104.42 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.68 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-01-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=64.76 AND Category=1 AND Memo="" AND Account=1 AND DateTrans="2008-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kevin Pay" AND Amount=-3076.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=321.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="credit card" AND Amount=138.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-1381.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5045 AND Payee="David" AND Amount=400.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5046 AND Payee="Affinity 4" AND Amount=2.53 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5047 AND Payee="Bethany Lutheran College" AND Amount=375.00 AND Category=17 AND Memo="Tuition" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5048 AND Payee="Bethany Lutheran College" AND Amount=2380.00 AND Category=17 AND Memo="Tuition" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=97.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=48.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=342.13 AND Category=16 AND Memo="online bill pay" AND Account=1 AND DateTrans="2008-01-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2008-01-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="GE Card" AND Amount=655.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=36.93 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-01-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.68 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic" AND Amount=342.13 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2008-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=36.93 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=1134.92 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2421.91 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-01-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=88.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Dividend Credit" AND Amount=-1.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=82.43 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=135.20 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Kevin" AND Amount=1214.69 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=64.76 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2866.90 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5049 AND Payee="Advanta National Bank" AND Amount=639.39 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5050 AND Payee="Reiman Publications" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=105.27 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=73.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Church Reimbursement" AND Amount=-700.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-599.09 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=113.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5076 AND Payee="EAA" AND Amount=22.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5077 AND Payee="Bethany Lutheran College" AND Amount=350.00 AND Category=17 AND Memo="Tuition" AND Account=1 AND DateTrans="2008-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2008-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=39.88 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-02-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.68 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-02-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5078 AND Payee="Unknown" AND Amount=39.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=80.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=424.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-02-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3147.17 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-02-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="GE Card" AND Amount=3.36 AND Category=17 AND Memo="couldn't be covered by Mayo, co" AND Account=1 AND DateTrans="2008-02-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-677.44 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=87.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??Kevin??" AND Amount=37.61 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=25.70 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-03-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=135.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kwik Trip" AND Amount=49.64 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-03-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=767.82 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2008-03-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2573.90 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=101.74 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=73.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=64.76 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-03-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=1500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=39.40 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-03-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5079 AND Payee="Piano Tuning" AND Amount=55.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5080 AND Payee="David" AND Amount=450.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=111.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2008-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.68 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2421.90 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-414.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=973.95 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=47.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5082 AND Payee="Kids Against World Hunger" AND Amount=300.00 AND Category=17 AND Memo="karen reimbursed 50 - kevin wil" AND Account=1 AND DateTrans="2008-03-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.92 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Karen's Checking" AND Amount=-500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay + Reimbursement" AND Amount=-804.23 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5081 AND Payee="postmaster" AND Amount=65.00 AND Category=17 AND Memo="was reimbursed" AND Account=1 AND DateTrans="2008-04-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=181.74 AND Category=17 AND Memo="was reimbursed" AND Account=1 AND DateTrans="2008-04-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=85.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=135.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Kevin's Church Account" AND Amount=-400.00 AND Category=17 AND Memo="Newspaper ad and Kids against H" AND Account=1 AND DateTrans="2008-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5012 AND Payee="??" AND Amount=25.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5084 AND Payee="??" AND Amount=60.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=64.76 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=84.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2806.46 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=194.93 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2008-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=73.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Error - undetermined" AND Amount=-217.82 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4" AND Amount=1200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5085 AND Payee="United States Treasury" AND Amount=1253.33 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5086 AND Payee="Minnesota Revenue" AND Amount=449.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=109.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=46.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2008-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2507.75 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mankato Clinic" AND Amount=192.84 AND Category=16 AND Memo="Lisa Eye Exam; Online Bill Pmt," AND Account=1 AND DateTrans="2008-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Clinic" AND Amount=177.64 AND Category=16 AND Memo="health care bills; online bill" AND Account=1 AND DateTrans="2008-04-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=1250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=591.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.74 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-04-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-679.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5087 AND Payee="Bethany Lutheran College" AND Amount=100.00 AND Category=17 AND Memo="Tuition" AND Account=1 AND DateTrans="2008-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5088 AND Payee="Reiman Publications" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=220.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="safe deposit box" AND Amount=27.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=7.16 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.80 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=135.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-107.47 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kevin Pay" AND Amount=-2430.95 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-277.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=73.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="To Lisa" AND Amount=400.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=105.34 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2008-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kevin Pay" AND Amount=-2396.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=3.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=34.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.74 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=35.02 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=45.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=106.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=1529.26 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=1500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2008-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=111.58 AND Category=16 AND Memo="confirmation 7S93X-Q70NT" AND Account=1 AND DateTrans="2008-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5091 AND Payee="" AND Amount=103.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=-2980.47 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3351.84 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=83.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=119.87 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=73.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=103.23 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2008-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=75.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5092 AND Payee="MN Dept of Treasury" AND Amount=106.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3033.11 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Sam's Club Discover Card" AND Amount=104.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-8.57 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2008-06-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.71 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-06-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=44.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=34.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=38.69 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=338.17 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5083 AND Payee="Auf Deutche Strausse" AND Amount=291.20 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5093 AND Payee="Benjamin Woltmann" AND Amount=20.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=81.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2578.89 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-07-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Birthday gift" AND Amount=-50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5089 AND Payee="" AND Amount=47.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5090 AND Payee="" AND Amount=113.68 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=-165.96 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-07-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=119.73 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=119.27 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=103.55 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2008-07-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Kevin Charitable Savings" AND Amount=-89.70 AND Category=17 AND Memo="RLF Expenses" AND Account=1 AND DateTrans="2008-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5095 AND Payee="Tonna Mechanical" AND Amount=260.37 AND Category=17 AND Memo="AC repair" AND Account=1 AND DateTrans="2008-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=73.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5094 AND Payee="" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=35.01 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="" AND Amount=65.78 AND Category=1 AND Memo="" AND Account=1 AND DateTrans="2008-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2578.90 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=102.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="IRS Incentive Check" AND Amount=-1421.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5096 AND Payee="Tonna Mechanical" AND Amount=76.00 AND Category=17 AND Memo="AC combing" AND Account=1 AND DateTrans="2008-07-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Kevin's Church Account" AND Amount=-4000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=44.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=186.59 AND Category=17 AND Memo="was reimbursed" AND Account=1 AND DateTrans="2008-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Toyota Financial" AND Amount=411.25 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2008-07-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=798.39 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5098 AND Payee="Dave Martinson Construction" AND Amount=5850.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.74 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-07-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=80.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2477.38 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-07-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-425.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5099 AND Payee="Dr. Vinyl" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Dividend Credit" AND Amount=-1.39 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=82.88 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="" AND Amount=2860.38 AND Category=17 AND Memo="Correction for Missed Statement" AND Account=1 AND DateTrans="2008-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Miscellaneous checks" AND Amount=-3501.33 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Health Care" AND Amount=361.47 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2008-08-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Alltell" AND Amount=104.25 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2008-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Optima" AND Amount=80.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5100 AND Payee="Clements Auto" AND Amount=2400.00 AND Category=10 AND Memo="Lisa's Car Downpayment" AND Account=1 AND DateTrans="2008-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=115.87 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5101 AND Payee="Grandville" AND Amount=50.00 AND Category=17 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2008-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5102 AND Payee="Grandville" AND Amount=200.00 AND Category=17 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2008-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="Newspaper Ad" AND Account=1 AND DateTrans="2008-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=104.10 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2008-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-08-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2378.90 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5103 AND Payee="??" AND Amount=24.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5104 AND Payee="Bethany Lutheran College" AND Amount=25.00 AND Category=17 AND Memo="Tuition" AND Account=1 AND DateTrans="2008-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=854.64 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2008-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sam's Club Discover Card" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Johnson&Johnson" AND Amount=-6.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Insurance check & Krueger reimb." AND Amount=-4615.57 AND Category=17 AND Memo="4365.57 insurance, 250 Gordon r" AND Account=1 AND DateTrans="2008-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5106 AND Payee="Kurt Holdorf" AND Amount=200.00 AND Category=17 AND Memo="Snicker's drawing" AND Account=1 AND DateTrans="2008-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=43.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=79.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.82 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=384.07 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2813.21 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-08-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Interest" AND Amount=-1.66 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-08-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-1085.91 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=19.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="To Lisa" AND Amount=400.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Blue" AND Amount=78.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2388.90 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-09-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=68.55 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=202.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5107 AND Payee="??" AND Amount=308.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5108 AND Payee="??" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="Newspaper Ad" AND Account=1 AND DateTrans="2008-09-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-1817.88 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-09-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Blue" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2388.89 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5110 AND Payee="Ascension Lutheran Church" AND Amount=163.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.81 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-09-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=1357.09 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=43.42 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-09-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5105 AND Payee="Kevin cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5111 AND Payee="Grandville" AND Amount=607.00 AND Category=17 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2008-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5112 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=17 AND Memo="Dog Sitting" AND Account=1 AND DateTrans="2008-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5113 AND Payee="Bethany Lutheran College" AND Amount=700.00 AND Category=17 AND Memo="Tuition" AND Account=1 AND DateTrans="2008-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5114 AND Payee="Affinity 4" AND Amount=2.84 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=86.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.42 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-09-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5115 AND Payee="??" AND Amount=3.18 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=77.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2388.90 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-10-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=84.51 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Optima" AND Amount=95.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-305.33 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5118 AND Payee="Thrivent" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=207.99 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2008-10-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="Newspaper Ad" AND Account=1 AND DateTrans="2008-10-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sam's Club Discover Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4 Credit Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5117 AND Payee="??" AND Amount=28.98 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-10-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-225.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2694.05 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=1200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=559.20 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.81 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-10-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=76.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5119 AND Payee="??" AND Amount=32.44 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-10-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.69 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-10-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=-350.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-431.79 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2712.62 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-11-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=93.86 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-11-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5120 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=17 AND Memo="Dog Sitting" AND Account=1 AND DateTrans="2008-11-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5121 AND Payee="??" AND Amount=27.62 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="To Lisa" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="Newspaper Ad" AND Account=1 AND DateTrans="2008-11-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2707.62 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-11-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=89.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=28.00 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-11-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=41.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=85.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=648.03 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-117.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-11-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5122 AND Payee="??" AND Amount=88.50 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-11-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=23.81 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-11-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2707.62 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-12-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-425.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Error - undetermined" AND Amount=-609.02 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5123 AND Payee="Taste of Home Books" AND Amount=14.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5124 AND Payee="Reiman Publications" AND Amount=28.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5125 AND Payee="Taste of Home Books" AND Amount=14.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=93.45 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=24.66 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=2950.45 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-425.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-12-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5128 AND Payee="Bethany Lutheran College" AND Amount=2000.00 AND Category=15 AND Memo="Donation" AND Account=1 AND DateTrans="2008-12-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2707.62 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5126 AND Payee="??" AND Amount=26.00 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2008-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5127 AND Payee="Ascension Lutheran Church" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=47.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="Newspaper Ad" AND Account=1 AND DateTrans="2008-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target National Bank" AND Amount=729.58 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Blue" AND Amount=41.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-29.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="To Lisa" AND Amount=102.95 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=20.41 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2008-12-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=23.68 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2008-12-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5129 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=17 AND Memo="Dog Sitting" AND Account=1 AND DateTrans="2008-12-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2806.97 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2008-12-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Pay" AND Amount=-425.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=632.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5097 AND Payee="Pine Haven" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2008-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Target National Bank" AND Amount=865.37 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=13.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=93.45 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Error - undetermined" AND Amount=0.13 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Money from Mom Dutton" AND Amount=-553.05 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Blue" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=80.60 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-01-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=9.55 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-01-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2405.77 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-01-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=65.77 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-01-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Kevin Charitable Savings" AND Amount=-212.70 AND Category=17 AND Memo="RLF 89.70, RLF taxable 83, Chur" AND Account=1 AND DateTrans="2009-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Kevin Charitable Savings" AND Amount=-3000.00 AND Category=17 AND Memo="$2k to BLC, $1k to PH" AND Account=1 AND DateTrans="2009-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5130 AND Payee="Bethany Lutheran College" AND Amount=25.00 AND Category=15 AND Memo="" AND Account=1 AND DateTrans="2009-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=97.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sunshine Sanitation" AND Amount=25.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5131 AND Payee="Thrivent" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5132 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=3676.01 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2009-01-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=29.90 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2009-01-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Office" AND Amount=6.67 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target National Bank" AND Amount=193.28 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Extra Pay + Misc" AND Amount=-337.33 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Capital One Bank" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=24.86 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Kevin Charitable Savings" AND Amount=-40.00 AND Category=17 AND Memo="For RLF donation + taxes" AND Account=1 AND DateTrans="2009-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Kevin Charitable Savings" AND Amount=-44.85 AND Category=17 AND Memo="To RLF for Website" AND Account=1 AND DateTrans="2009-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5133 AND Payee="Moon Beach Camp" AND Amount=130.00 AND Category=17 AND Memo="Deposit for Family Camp Aug 2-8" AND Account=1 AND DateTrans="2009-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2407.41 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-01-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo Clinic" AND Amount=317.71 AND Category=16 AND Memo="Should pay off 2008 charges" AND Account=1 AND DateTrans="2009-01-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.52 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-01-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="American Express Optima" AND Amount=71.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=80.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=92.74 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5134 AND Payee="State Farm" AND Amount=25.00 AND Category=17 AND Memo="Identity Restoration Coverage" AND Account=1 AND DateTrans="2009-02-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3049.07 AND Category=20 AND Memo="Also includes healthcare reimbu" AND Account=1 AND DateTrans="2009-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sunshine Sanitation" AND Amount=25.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5135 AND Payee="Reiman Publications" AND Amount=29.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5136 AND Payee="Reiman Publications" AND Amount=10.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5137 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="Rent Supplement" AND Account=1 AND DateTrans="2009-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=70.20 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2009-02-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=24.79 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-02-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=70.20 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2009-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=39.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3645.53 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5138 AND Payee="??" AND Amount=56.80 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=450.52 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="walmart" AND Amount=105.56 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Lakewood Dental" AND Amount=140.00 AND Category=16 AND Memo="Karen cleaning/exam" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=25.77 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Rochester Family Eye Clinic" AND Amount=154.83 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Error - undetermined" AND Amount=-5.20 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.84 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=550.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=70.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5139 AND Payee="Reiman Publications" AND Amount=31.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=93.09 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="??" AND Amount=200.00 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=25.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3090.67 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=24.79 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=65.78 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-03-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=5.69 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-03-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Karen's Checking" AND Amount=-1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5140 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2009-03-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=39.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2581.44 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-03-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=559.56 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=2500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5141 AND Payee="Gordon Krueger" AND Amount=75.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2009-04-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=69.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sunshine Sanitation" AND Amount=26.12 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=93.09 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2581.44 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=123.17 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-04-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-04-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=65.81 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5147 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2009-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=38.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Kevin Charitable Savings" AND Amount=-1500.00 AND Category=17 AND Memo="For RLF donation + taxes" AND Account=1 AND DateTrans="2009-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5144 AND Payee="Minnesota Revenue" AND Amount=70.69 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5145 AND Payee="United States Treasury" AND Amount=2319.61 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5146 AND Payee="Minnesota Revenue" AND Amount=879.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5148 AND Payee="Michigan Tech Fund" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-129.95 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-04-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2581.44 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-04-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5142 AND Payee="Void" AND Amount=-2581.44 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5143 AND Payee="Void" AND Amount=-2581.44 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=24.90 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-04-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5024 AND Payee="??" AND Amount=9.72 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-04-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=180.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="safe deposit box" AND Amount=27.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.83 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-04-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=67.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2663.29 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-05-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sunshine Sanitation" AND Amount=28.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=132.28 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-05-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=93.09 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5149 AND Payee="??" AND Amount=45.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=78.38 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=65.67 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-05-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4 Credit Card" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Account Adjustment" AND Amount=-476.38 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="second adjustment due to reconci" AND Amount=1.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5150 AND Payee="??" AND Amount=170.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=122.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=220.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2390.23 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-05-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=38.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=24.90 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-05-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=31.10 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Karen's Checking" AND Amount=-2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-84.85 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5151 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2009-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.59 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=140.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=152.95 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2206.84 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5152 AND Payee="Interlaken Golf Club" AND Amount=1071.83 AND Category=17 AND Memo="Rehearsal Dinner for David and" AND Account=1 AND DateTrans="2009-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=66.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=125.27 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-06-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=97.29 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Karen's Checking" AND Amount=-200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Karen's Checking" AND Amount=-950.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-06-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=25.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4 Credit Card" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5153 AND Payee="State Farm" AND Amount=30.00 AND Category=17 AND Memo="Jessica's Wedding Ring" AND Account=1 AND DateTrans="2009-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5154 AND Payee="Sam's Club Discover Card" AND Amount=188.10 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2009-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5155 AND Payee="DVS - Camry" AND Amount=105.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=65.67 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-06-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Checks" AND Amount=30.40 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2229.18 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-06-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Checks" AND Amount=34.85 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Capital One" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5156 AND Payee="??" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=24.90 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-06-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.07 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2303.87 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5157 AND Payee="??" AND Amount=23.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5160 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=37.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=10.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from MECU Savings" AND Amount=-500.00 AND Category=17 AND Memo="Reimburse for Premier Bank Acco" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="First National Bank of Omaha" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Alltell" AND Amount=130.55 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=4748 AND Payee="??" AND Amount=22.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5162 AND Payee="Affinity 4" AND Amount=3.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5163 AND Payee="??" AND Amount=152.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5164 AND Payee="Tonna Mechanical" AND Amount=103.81 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5165 AND Payee="Transfer to American Expres Optima" AND Amount=31.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5166 AND Payee="Olmsted County Vital Records" AND Amount=115.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5176 AND Payee="Premier Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=97.29 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=25.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5167 AND Payee="David Buchs" AND Amount=1600.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=36.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=65.67 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-07-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5161 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2009-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2219.20 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5169 AND Payee="Thrivent" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5170 AND Payee="State Farm" AND Amount=403.74 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=100.00 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2009-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5168 AND Payee="??" AND Amount=22.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.16 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-07-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2217.18 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=600.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=980.72 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5030 AND Payee="??" AND Amount=75.91 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5031 AND Payee="??" AND Amount=155.03 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5172 AND Payee="Moon Beach Camp" AND Amount=682.16 AND Category=17 AND Memo="Deposit for Family Camp Aug 2-8" AND Account=1 AND DateTrans="2009-08-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Charitable giving" AND Amount=-50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5171 AND Payee="Wycliff" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=63.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=63.45 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-08-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sam's Club Discover Card" AND Amount=164.74 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2009-08-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=131.42 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-08-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Charter Cable" AND Amount=188.70 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-08-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2217.19 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4 Credit Card" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5036 AND Payee="Amythest Dental" AND Amount=113.00 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2009-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.14 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-08-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer from Kevin Charitable Savings" AND Amount=-750.00 AND Category=17 AND Memo="For RLF donation + taxes" AND Account=1 AND DateTrans="2009-08-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=36.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Capital One" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5174 AND Payee="Kohl's" AND Amount=43.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2217.18 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-08-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5173 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="Mom and Dad's Apartment" AND Account=1 AND DateTrans="2009-08-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5175 AND Payee="Gordon Krueger" AND Amount=180.00 AND Category=18 AND Memo="Anniversary Gift" AND Account=1 AND DateTrans="2009-08-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=62.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-08-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=238.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=126.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5177 AND Payee="Kristine Nowak" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="State Farm" AND Amount=80.65 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Alltell" AND Amount=118.87 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Savings" AND Amount=-2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2217.18 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-09-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="To Lisa" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-09-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Savings" AND Amount=-2500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=400.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=107.39 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5178 AND Payee="Lunch Bunch" AND Amount=32.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5179 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2009-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5180 AND Payee="Gordon Krueger" AND Amount=175.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2009-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=25.14 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-09-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=182.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sam's Club Discover Card" AND Amount=303.12 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2009-09-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5181 AND Payee="dept of state for passport" AND Amount=160.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2217.20 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-09-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Savings" AND Amount=-287.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Capital One" AND Amount=4000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=61.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=241.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=134.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-09-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=80.65 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2908.34 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-10-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Alltell" AND Amount=120.72 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-10-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-10-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=107.53 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-10-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-4461.53 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.12 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5184 AND Payee="Thrivent" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=35.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4 Credit Card" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sam's Club Discover Card" AND Amount=100.00 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5183 AND Payee="brightway windows" AND Amount=110.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5185 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=3500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=60.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-10-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5182 AND Payee="??" AND Amount=13.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=25.12 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-11-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3133.25 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-11-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=80.65 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-404.88 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="??" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=107.53 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-11-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Thrivent" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=500.00 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-11-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3133.26 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-11-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5186 AND Payee="DMV" AND Amount=41.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5187 AND Payee="DVM" AND Amount=41.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-290.27 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=1500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.12 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-11-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=202.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-0.86 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=-1387.29 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-11-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3133.25 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-12-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mill's Gas" AND Amount=35.46 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2009-12-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="CK SPa" AND Amount=26.40 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=180.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=80.65 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5189 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2009-12-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="gift cards" AND Amount=205.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Closeing Out Karen's Accounts" AND Amount=-4053.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Check from Lisa" AND Amount=-500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Savings" AND Amount=-1500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Affinity 4 Credit Card" AND Amount=500.00 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5188 AND Payee="??" AND Amount=151.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="stucs pizza" AND Amount=41.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target" AND Amount=34.53 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2009-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=25.32 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.10 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2009-12-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=160.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3133.25 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=125.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.12 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2009-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Capital One" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="from lisa" AND Amount=-100.00 AND Category=17 AND Memo="took 200 for cash, original amo" AND Account=1 AND DateTrans="2009-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-379.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-3224.53 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kwik Trip" AND Amount=46.39 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5201 AND Payee="David and Jessica Buchs" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5202 AND Payee="Jessica Buchs" AND Amount=175.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5203 AND Payee="David Buchs" AND Amount=175.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=58.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5190 AND Payee="Jan Anderson" AND Amount=600.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5191 AND Payee="Kristine Nowak" AND Amount=600.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5204 AND Payee="Bethany Lutheran College" AND Amount=2100.00 AND Category=15 AND Memo="" AND Account=1 AND DateTrans="2009-12-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Real Lutheran Fellowship" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Account Adjustment" AND Amount=-6687.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=7377.61 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=2106.35 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2009-12-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=80.65 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-139.40 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Our Redeemer Lutheran Church" AND Amount=500.00 AND Category=15 AND Memo="Kevin Church" AND Account=1 AND DateTrans="2010-01-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-01-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Menards" AND Amount=23.62 AND Category=17 AND Memo="softner salt." AND Account=1 AND DateTrans="2010-01-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=121.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-01-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.21 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2779.95 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="gift" AND Amount=-50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="walmart" AND Amount=75.14 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5206 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2010-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=7.01 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=750.00 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2010-01-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Healing Touch" AND Amount=53.32 AND Category=16 AND Memo="Massage" AND Account=1 AND DateTrans="2010-01-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Napa" AND Amount=27.65 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2010-01-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="healthcare reim from david" AND Amount=-895.34 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Westgate" AND Amount=209.92 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-01-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=202.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=31.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2010-01-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Charitable giving" AND Amount=-900.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Dividend Credit" AND Amount=-1.46 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-01-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.12 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-01-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2756.61 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-01-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Piano Pay" AND Amount=-103.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5193 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2010-02-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5207 AND Payee="Pine Haven" AND Amount=350.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=43.93 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-02-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=57.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=82.55 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2756.63 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-02-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Hollywood Theaters" AND Amount=3.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Hollywood Theaters" AND Amount=12.94 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Clark Gas" AND Amount=39.16 AND Category=10 AND Memo="Is this the right charge accoun" AND Account=1 AND DateTrans="2010-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=1000.00 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2010-02-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.10 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-02-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer From Savings" AND Amount=-1500.00 AND Category=17 AND Memo="Overage" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5194 AND Payee="Self Defense Class" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5208 AND Payee="??" AND Amount=184.89 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Greenway Gas" AND Amount=31.04 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=90.82 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Westgate" AND Amount=28.49 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="cascade animal medical center" AND Amount=123.18 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2010-02-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Capital One" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo paycheck" AND Amount=-2756.62 AND Category=13 AND Memo="" AND Account=1 AND DateTrans="2010-02-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Piano Pay" AND Amount=-310.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.22 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-02-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.06 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Account Adjustment" AND Amount=-3458.12 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-02-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="" AND Amount=-293.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="B and R Oil" AND Amount=13.78 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-03-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5196 AND Payee="" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=81.59 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2863.69 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-03-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Piano Pay" AND Amount=-100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.10 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-03-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=80.50 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-03-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Charitable giving" AND Amount=-1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5198 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5209 AND Payee="Thrivent" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=56.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Lutheran Heritage Foundation" AND Amount=300.00 AND Category=15 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Lakewood Dental" AND Amount=147.00 AND Category=16 AND Memo="Karen cleaning/exam" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=79.14 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Love From MN" AND Amount=29.95 AND Category=14 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="JCPenney" AND Amount=29.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="B and R Oil" AND Amount=35.03 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="??" AND Amount=32.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Affinity 4 Credit Card" AND Amount=500.00 AND Category=17 AND Memo="Includes New Phone" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=186.32 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-4248.70 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-03-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="??" AND Amount=109.01 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5197 AND Payee="Transfer to Capital One" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.22 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-03-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amythest Dental" AND Amount=80.00 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2010-03-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Nashbar" AND Amount=53.26 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5199 AND Payee="??" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5210 AND Payee="Kohl's" AND Amount=100.24 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.22 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=656.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=55.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-03-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=81.59 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Karen Piano Pay" AND Amount=-36.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Savings" AND Amount=-750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Our Redeemer" AND Amount=-500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2863.69 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5212 AND Payee="Bethany Lutheran College" AND Amount=200.00 AND Category=15 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=170.82 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-04-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="AGHER Festival Registration" AND Amount=210.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-69.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=116.52 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-04-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.10 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=72.87 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-04-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Dept of Treasury" AND Amount=528.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="First National Bank of Omaha" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Savings" AND Amount=-750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5199 AND Payee="Lock Away Storage" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5211 AND Payee="AGHER Festival Music and CD" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5213 AND Payee="United States Treasury" AND Amount=506.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5214 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5215 AND Payee="Thrivent" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Qwest" AND Amount=25.12 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-04-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2863.69 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-04-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=3000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=40.95 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-04-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Day's Inn, Sheb. Falls" AND Amount=53.90 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=44.15 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=12.67 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-04-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=29.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-04-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=54.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Lock Away Storage" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2847.81 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-05-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=28.30 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-05-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=81.59 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=94.05 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-05-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-363.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=92.62 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Silver Lake Foods" AND Amount=17.57 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amythest Dental" AND Amount=164.00 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2010-05-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.10 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-05-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="First National Bank of Omaha" AND Amount=2000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Tax Correction + 200 from lisa" AND Amount=-311.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kwik Trip" AND Amount=37.55 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target" AND Amount=189.65 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Menards" AND Amount=68.87 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2863.71 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Black's Auto" AND Amount=128.34 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-05-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Lock Away Storage" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=257.40 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2010-05-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Black's Auto" AND Amount=128.38 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-05-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Capital One" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=44.00 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=45.11 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Herbergers" AND Amount=30.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Get and Go Gas" AND Amount=35.25 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="UPS" AND Amount=14.02 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="DAHLC" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5218 AND Payee="David Buchs" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5219 AND Payee="David and Jessica Buchs" AND Amount=150.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5220 AND Payee="SCRIPPS" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee Sioux Falls" AND Amount=63.47 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=29.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.28 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-05-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5221 AND Payee="The Flower Cart" AND Amount=44.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5223 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Savings" AND Amount=-1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5226 AND Payee="Transfer to American Expres Optima" AND Amount=53.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.56 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Correction" AND Amount=-291.39 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-05-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2863.69 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-06-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Fleet Farm" AND Amount=67.64 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5219 AND Payee="Gordon Krueger" AND Amount=700.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2010-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5220 AND Payee="??" AND Amount=49.36 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5224 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Amythest Dental" AND Amount=170.00 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2010-06-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=79.81 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=275.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-288.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="JCPenney" AND Amount=26.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="walmart" AND Amount=98.50 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Bicycle Sports" AND Amount=85.89 AND Category=17 AND Memo="new rear wheel" AND Account=1 AND DateTrans="2010-06-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5220 AND Payee="Piano Pay" AND Amount=-48.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=103.73 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=35.56 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=51.43 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Walgreens" AND Amount=83.30 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-06-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.11 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-06-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="The Hole In One" AND Amount=27.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Shaw's Market" AND Amount=83.73 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=142.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Bookstore & Restaurant" AND Amount=81.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Wellfleet Spirit Shoppe" AND Amount=6.83 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Tax Refund Correction" AND Amount=-862.49 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2863.70 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=242.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Gas station" AND Amount=31.29 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Stop and Shop" AND Amount=22.51 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="PJ's Family Restaurant" AND Amount=45.96 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="The Hot Chocolate Sparrow" AND Amount=10.93 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mac's Seafood" AND Amount=9.39 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5225 AND Payee="First National Bank of Omaha" AND Amount=1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-24" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.28 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-06-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=116.55 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-06-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5221 AND Payee="??" AND Amount=101.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=104.58 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-06-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Good Food Store" AND Amount=73.18 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=31.86 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-06-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Famous Footwear" AND Amount=21.99 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=71.21 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-06-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="LL Bean" AND Amount=158.93 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-29" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Overage from Savings" AND Amount=-1000.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2953.05 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=28.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=52.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.47 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Correction" AND Amount=90.25 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-06-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target" AND Amount=85.03 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sears" AND Amount=36.80 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=79.81 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="US Postal Service" AND Amount=1.39 AND Category=17 AND Memo="Package to Lisa" AND Account=1 AND DateTrans="2010-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=58.50 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Good Food Store" AND Amount=206.16 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Fleet Farm" AND Amount=122.39 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="??" AND Amount=28.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5223 AND Payee="Tony Nowak" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="JCPenney" AND Amount=21.97 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Herbergers" AND Amount=45.63 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Herbergers" AND Amount=26.80 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Barnes and Noble" AND Amount=31.83 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target" AND Amount=88.66 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Fleet Farm" AND Amount=121.65 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Macy's" AND Amount=25.45 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5224 AND Payee="Kristine Nowak" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.11 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-07-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=36.53 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-07-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2843.69 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Pharmacy" AND Amount=31.59 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2010-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Verizon Wireless" AND Amount=107.57 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2010-07-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="First National Bank of Omaha" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="RMH Employee Cafe" AND Amount=0.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=93.99 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-07-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="RMH Employee Cafe" AND Amount=1.61 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=44.46 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-07-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="DAHLC" AND Amount=40.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=45.84 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-07-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5055 AND Payee="??" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Kwik Trip" AND Amount=35.10 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Capital One" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Sears" AND Amount=63.28 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Lakewood Dental" AND Amount=199.00 AND Category=16 AND Memo="Karen cleaning/exam" AND Account=1 AND DateTrans="2010-07-21" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="LL Bean" AND Amount=-35.48 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Mayo Health Care" AND Amount=786.18 AND Category=16 AND Memo="" AND Account=1 AND DateTrans="2010-07-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2853.70 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=5226 AND Payee="Gordon Krueger" AND Amount=450.00 AND Category=18 AND Memo="" AND Account=1 AND DateTrans="2010-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target" AND Amount=103.51 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Fleet Farm" AND Amount=94.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=48.27 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-07-23" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.81 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-07-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Transfer to American Expres Optima" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Target" AND Amount=79.11 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Superamerica" AND Amount=38.08 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-07-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MEFCU" AND Amount=-1.76 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Correction" AND Amount=-0.62 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Delta Air" AND Amount=765.30 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="Delta Air" AND Amount=765.30 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-07-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=77.20 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Northern Tool & Equipment" AND Amount=8.58 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=179.28 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Fleet Farm" AND Amount=76.56 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cash" AND Amount=300.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Misc Paychecks Deposit" AND Amount=-52.97 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-08-03" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Verizon Wireless" AND Amount=127.27 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2010-08-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=100.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-04" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target" AND Amount=134.75 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-05" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=80.80 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-06" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-2 AND Payee="HyVee" AND Amount=113.47 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-08-07" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=120.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="MN Energy Resources" AND Amount=19.00 AND Category=21 AND Memo="" AND Account=1 AND DateTrans="2010-08-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.04 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-4455.00 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-08-10" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="from lisa" AND Amount=-200.00 AND Category=17 AND Memo="took 200 for cash, original amo" AND Account=1 AND DateTrans="2010-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Cable" AND Amount=113.11 AND Category=1 AND Memo="AutoPay" AND Account=1 AND DateTrans="2010-08-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target" AND Amount=27.56 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-12" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=63.03 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Capital One" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="First National Bank of Omaha" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kwik Trip" AND Amount=36.09 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-08-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target" AND Amount=69.54 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=165.29 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-08-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Real Lutheran Fellowship" AND Amount=500.00 AND Category=15 AND Memo="" AND Account=1 AND DateTrans="2010-08-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Lock Away Storage" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=80.31 AND Category=22 AND Memo="" AND Account=1 AND DateTrans="2010-08-18" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-1 AND Payee="Cash" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-19" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer From Savings" AND Amount=-1000.00 AND Category=17 AND Memo="Overage" AND Account=1 AND DateTrans="2010-08-22" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Qwest" AND Amount=25.81 AND Category=4 AND Memo="online EFT" AND Account=1 AND DateTrans="2010-08-25" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=26.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-26" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial-Karen" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-08-31" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Transfer to American Expres Optima" AND Amount=50.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-01" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial" AND Amount=750.00 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2010-09-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=500.00 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2010-09-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Interest" AND Amount=-1.52 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-02" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="State Farm" AND Amount=80.29 AND Category=8 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Mayo paycheck" AND Amount=-2893.69 AND Category=20 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kitchen Collection" AND Amount=67.97 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Cut Above" AND Amount=28.17 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Love From MN" AND Amount=27.90 AND Category=14 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="HyVee" AND Amount=147.22 AND Category=11 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Kwik Trip" AND Amount=34.34 AND Category=10 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="From Piggy Bank" AND Amount=-136.30 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="ATM" AND Amount=240.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sunshine Sanitation" AND Amount=29.08 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-08" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="ATM" AND Amount=200.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-09" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target" AND Amount=149.10 AND Category=11 AND Memo="" AND Account=1 AND DateTrans="2010-09-11" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Sargeants on Second" AND Amount=58.98 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Charter Communication" AND Amount=104.56 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-13" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Verizon Wireless" AND Amount=111.50 AND Category=4 AND Memo="" AND Account=1 AND DateTrans="2010-09-14" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Rochester Post Bulletin" AND Amount=11.70 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="walmart" AND Amount=80.68 AND Category=11 AND Memo="" AND Account=1 AND DateTrans="2010-09-15" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Lock Away Storage" AND Amount=42.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-16" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Piano Pay" AND Amount=-388.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Starting Balance Adjustment" AND Amount=-1865.06 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-17" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="First National Bank of Omaha" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Capital One Bank" AND Amount=750.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-20" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Express Blue" AND Amount=26.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Chase Financial" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-27" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Target National Bank" AND Amount=500.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="Amazon Chase" AND Amount=250.00 AND Category=19 AND Memo="" AND Account=1 AND DateTrans="2010-09-28" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
sql="""select Id from Transactions where Type=-4 AND Payee="American Epress Optima" AND Amount=49.00 AND Category=17 AND Memo="" AND Account=1 AND DateTrans="2010-09-30" AND DateEnter="2010-09-30" """
cursor.execute(sql)
id=cursor.fetchone()
sql='insert into Reconciliation (TransId,Reconciled) Values (%d,1)' % id[0]
cursor.execute(sql)
cursor.fetchone()
cursor.close()
db.close()
