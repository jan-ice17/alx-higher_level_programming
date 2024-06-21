#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

def hbtn_database
myDb = MySQLdb.connect(
    host="localhost",
    port=3306,
    user_name=sys.argv[1],
    my_password=sys.argv[2],
    database=sys.argv[3]       
    )

MyCursor = myDb.cursor()
return myDb, MyCursor


#Solution to task 0
def show_a_database():
    myDb, Mycursor = hbtn_database()
    Mycursor.execute('USE hbtn_0e_0_usa')
    Mycursor.execute('INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada")')
    Mycursor.execute('SELECT * FROM states ORDER BY id ASC')
    for i in Mycursor:
        print(i)
    Mycursor.close()
    MyDb.close()

def main():
    show_a_database()
   

if __name__=='__main__':
    main()