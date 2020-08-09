#!/usr/bin/python3
"""
hat takes in an argument and displays all values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]
    name_arg = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(name_arg))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
