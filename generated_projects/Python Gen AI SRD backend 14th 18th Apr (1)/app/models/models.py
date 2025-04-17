from sqlalchemy import Column, Integer, String
from app.database import Base

class Leaves(Base):
    __tablename__ = 'leaves'
    {'name': 'id', 'type': 'integer', 'primary_key': True} = Column(String)
    {'name': 'start_date', 'type': 'date'} = Column(String)
    {'name': 'end_date', 'type': 'date'} = Column(String)
    {'name': 'reason', 'type': 'string'} = Column(String)
    {'name': 'status', 'type': 'string'} = Column(String)

class Pods(Base):
    __tablename__ = 'pods'
    {'name': 'id', 'type': 'integer', 'primary_key': True} = Column(String)
    {'name': 'name', 'type': 'string'} = Column(String)

class Pod_members(Base):
    __tablename__ = 'pod_members'
    {'name': 'id', 'type': 'integer', 'primary_key': True} = Column(String)
    {'name': 'pod_id', 'type': 'integer', 'foreign_key': True} = Column(String)
    {'name': 'user_id', 'type': 'integer', 'foreign_key': True} = Column(String)

class Users(Base):
    __tablename__ = 'users'
    {'name': 'id', 'type': 'integer', 'primary_key': True} = Column(String)
    {'name': 'email', 'type': 'string'} = Column(String)
    {'name': 'password', 'type': 'string'} = Column(String)
    {'name': 'role', 'type': 'string'} = Column(String)

