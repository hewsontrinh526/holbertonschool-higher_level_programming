#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
"""
import MySQLdb
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                               passwd=sys.argv[2], db=sys.argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT id FROM states WHERE name LIKE %s ORDER BY id;",
                   ('Louisiana',))
    rows = cursor.fetchall()
    if not rows:
        new_state = State(name="Louisiana")
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]))
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(new_state)
        session.commit()
        print(new_state.id)
        session.close()
    else:
        for row in rows:
            print("{}".format(row[0]))
    cursor.close()
    database.close()
