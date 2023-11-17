#!/usr/bin/python3
"""
 script that takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()

    state_name = sys.argv[4]

    query = """SELECT GROUP_CONCAT(cities.name SEPARATOR '. ')
               FROM cities
               JOIN states ON states.id = cities.state_id
               WHERE states.name LIKE %s
               ORDER BY cities.id"""

    cursor.execute(query, (state_name,))

    results = cursor.fetchone()

    if results:
        print(results[0])

    cursor.close()
    db.close()
