#!/usr/bin/python3
"""lists all State objects that contain the letter a"""
import sys
from model_state import Base, State
import sqlalchemy as db
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)
    new_session = session()

    result = new_session.query(State).\
        filter(State.name.like('%a%')).order_by(State.id)

    if result is None:
        print("Nothing")

    for row in result:
        print("{}: {}".format(row.id, row.name))
