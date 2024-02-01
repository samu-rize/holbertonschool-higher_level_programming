#!/usr/bin/python3

import MySQLdb
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    bdname = sys.argv[3]
    db = MySQLdb.connect( host="localhost",port=3306,user=username,passwd=password,db=bdname
    )
    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id"
    cur.execute(query)
    result = cur.fetchall()
    for row in result:
        print(row)
