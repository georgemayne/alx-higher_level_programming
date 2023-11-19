#!/usr/bin/python3

"""displays all values in the states table of hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = con.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    con.close()
