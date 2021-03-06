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
    state_name = argv[4]
    cities = ""

    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT c.id, c.name\
                 FROM states AS s INNER JOIN cities AS c ON s.id = c.state_id\
                 WHERE s.name = %s ORDER BY c.id ASC", (state_name, ))
    rows = cur.fetchall()
    for row in rows:
        if rows[len(rows) - 1] != row:
            cities += row[1] + ", "
        else:
            cities += row[1]
    print(cities)
    cur.close()
    db.close()
