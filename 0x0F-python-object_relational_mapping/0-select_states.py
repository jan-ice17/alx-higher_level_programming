#!/usr/bin/python3
""" Imported modules"""

import MySQLdb
import sys

def database_hbtn():
    db = MySQLdb.connect(
        user=sys.argv[1], 
        host=sys.argv[2], 
        password='Password@5756',
        database=sys.argv[3],
        auth_plugin='mysql_native_password'
        )
    
    mycursor = db.cursor()
    return db, mycursor

#Task 0
def database_show():
    db, dbcursor = database_hbtn()
    dbcursor.execute('USE hbtn_0e_0_usa')
    dbcursor.execute('INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada")')
    dbcursor.execute('SELECT * FROM states ORDER BY id ASC')
    for i in dbcursor:
        print(i)
    dbcursor.close()
    db.close()
