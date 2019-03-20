from sqlalchemy import create_engine

from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlougithub')

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repositories'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(64), index=True)
    update_time = Column(Date)
    commits = Column(Integer, index=True)
    branches = Column(Integer, index=True)
    releases = Column(Integer, index=True)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
