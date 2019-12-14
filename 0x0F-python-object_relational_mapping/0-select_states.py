#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa '''


if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="127.0.0.1", user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("select * from states order by states.id")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()
