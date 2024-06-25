#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./<script_name>.py <username> <password> <database_name>")
        exit(1)
    
    u_name = argv[1]
    psw = argv[2]
    base = argv[3]

    try:
        # Connecting to MySQL database
        print("Connecting to database...")
        db = MySQLdb.connect(host="localhost", user=u_name,
                             passwd=psw, db=base, port=3306)
        print("Connected to database")
    except MySQLdb.Error as err:
        print(f"Error: {err}")
        exit(1)

    try:
        # Creating cursor object
        print("Creating cursor...")
        cur = db.cursor()

        # Executing MySQL Query
        print("Executing query...")
        cur.execute("SELECT * FROM states ORDER BY id")

        # Obtaining Query Result & prints the result in rows
        print("Fetching rows...")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as err:
        print(f"Error: {err}")

    finally:
        # Clean Up
        print("Closing cursor and database connection...")
        cur.close()
        db.close()
