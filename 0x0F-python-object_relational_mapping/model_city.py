#!/usr/bin/python3
'''city module'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class City(Base):
    __tablename__ = 'cities'
    __table_args__ = {'mysql_engine': 'InnoDB', 'mysql_charset': 'latin1'}
    id = Column(Integer(), primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
