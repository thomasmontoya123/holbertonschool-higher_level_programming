#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
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

    new_state = State(name='Louisiana')
    new_session.add(new_state)
    new_session.flush()
    new_session.commit()

    result = new_session.query(State).\
        filter(State.name == 'Louisiana').first()

    print(result.id)
