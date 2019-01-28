
import sys

sys.path.append('C:\Python27\Lib\site-packages\MySQLdb')

import MySQLdb


con=MySQLdb.connect("localhost","root","","test" )

cur=con.cursor()

sel=("select id, custName, nSql from TBLA")
cur.execute(sel)
res1=cur.fetchall()

for outrow in res1:
    print 'Customer ID : ', outrow[0], ': ', outrow[1]
    nSql = outrow[2]
    cur.execute(nSql)
    res2=cur.fetchall()

    for inrow in res2:
        dateK =inrow[0]
        id= inrow[1]
        name= inrow[2]
        city=inrow[3]
        insertstmt=("insert into TBLB (dateK, id, name, city) values ('%s', '%s', '%s', '%s')" % (dateK, id, name, city))
        cur.execute(insertstmt)

con.commit()
con.close()
