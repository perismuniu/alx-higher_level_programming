#!/usr/bin/python3
"""
script that takes in arguments and displays all valuesin the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()

    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id"

    cursor.execute(query, (state_name + '%',))

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()
