#!/usr/bin/python3

"""Lists all states from the datahase hbtn_0e_0_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    con = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = con.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = c.fetchall()
    for row in query_rows:
        print(row)
    c.close()
    con.close()
