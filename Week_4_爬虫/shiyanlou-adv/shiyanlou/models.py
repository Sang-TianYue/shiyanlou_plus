from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy import Date

engine = create_engine('mysql+mysqldb://root@localhost:3306/shiyanlou?charset=utf8')

Base = declarative_base()

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), index=True)
    description = Column(String(1024))
    type = Column(String(64), index=True)
    students = Column(Integer)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(64), index=True)
    join_date = Column(Date)
    type = Column(String(64))
    level = Column(Integer, index=True)
    status = Column(String(64), index=True)
    school_job = Column(String(64))
    learn_courses_num = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
