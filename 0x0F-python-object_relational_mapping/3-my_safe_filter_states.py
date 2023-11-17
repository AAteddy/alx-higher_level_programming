#!/usr/bin/python3
"""
Takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa.
Where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY states.id")
    rows = c.fetchall()
    for row in rows:
        if(sys.argv[4] == row[1]):
            print(row)
    c.close()
    db.close()
