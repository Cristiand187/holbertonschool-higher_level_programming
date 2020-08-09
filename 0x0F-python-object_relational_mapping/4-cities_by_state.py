#!/usr/bin/python3
"""
Script will display states sorted by id in ascending order
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name\
                 FROM states AS s INNER JOIN cities AS c ON s.id = c.state_id\
                 ORDER BY c.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
