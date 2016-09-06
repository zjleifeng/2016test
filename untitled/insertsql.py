import MySQLdb
con=MySQLdb.connect(host="localhost",user="root",passwd="zjhan",db="test",charset="utf8")
cur=con.cursor()
sql= """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
user_id="test123"
password="password"
sql1="insert INTO e"
try:
    cur.execute(sql)
    con.commit()
except:
    con.rollback()
con.close()