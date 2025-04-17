from sqlalchemy import Column, Integer, String
from app.database import Base

class Leaves(Base):
    __tablename__ = 'leaves'
    id = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    reason = Column(String)
    status = Column(String)
    user_id = Column(String)

class Pods(Base):
    __tablename__ = 'pods'
    id = Column(String)
    name = Column(String)
    members = Column(String)

class Pod_members(Base):
    __tablename__ = 'pod_members'
    id = Column(String)
    pod_id = Column(String)
    user_id = Column(String)
    role = Column(String)

class Users(Base):
    __tablename__ = 'users'
    id = Column(String)
    email = Column(String)
    password = Column(String)
    role = Column(String)

