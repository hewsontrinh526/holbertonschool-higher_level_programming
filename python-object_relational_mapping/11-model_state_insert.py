#!/usr/bin/python3
"""
Scripts that adds the State object "Louisiana" to the database hbtn_0e_6_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("INSERT INTO states (name) VALUES ('Louisiana');")
    print("{}".format(cursor.lastrowid))
    cursor.close()
    database.close()
