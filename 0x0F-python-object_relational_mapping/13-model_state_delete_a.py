#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""
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

    new_session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session='fetch')

    new_session.flush()
    new_session.commit()
