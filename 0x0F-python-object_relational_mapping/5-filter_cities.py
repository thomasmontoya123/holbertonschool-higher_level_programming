#!/usr/bin/python3
'''lists all cities from the database hbtn_0e_4_usa'''
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities"
                " JOIN states  ON cities.state_id = states.id"
                " WHERE states.name = %(name)s ORDER BY cities.id ;",
                {"name": argv[4]})

    result = cur.fetchall()

    for position, row in enumerate(result):
        if position != 0:
            print(', ', end='')
        print(row[0], end='')
    print

    cur.close()
    db.close()
