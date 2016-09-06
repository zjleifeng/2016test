import MySQLdb

con=MySQLdb.connect(host="localhost",user="root",passwd="zjhan",db="test",charset="utf8")
#con=MySQLdb.connect(host="localhost",user="root",passwd="zjhan",db="test",charset="utf8")
cur=con.cursor()

#deltable
#deldb="DROP TABLE IF EXISTS EMPLOYEE"

#cur.execute(deldb)



sql="""CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT ) """
cur.execute(sql)

con.close()