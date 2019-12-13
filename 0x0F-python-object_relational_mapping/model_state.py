#!/usr/bin/python3
'''state module'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'latin1'}
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)