#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
import sqlalchemy as db
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    connection = engine.connect()
    metadata = db.MetaData()
    states = db.Table('states', metadata, autoload=True, autoload_with=engine)

    query = db.select([states])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    for row in ResultSet:
        print("{}: {}".format(row[0], row[1]))
