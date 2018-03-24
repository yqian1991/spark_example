from sqlalchemy import Integer, Column, create_engine, ForeignKey
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None


class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child")


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))


def setup_once(dburl, echo, num):
    "setup once.  create an engine, insert fixture data"
    global engine
    engine = create_engine(dburl, echo=echo)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    sess = Session(engine)
    sess.add_all([
        Parent(children=[Child() for j in range(100)])
        for i in range(num)
    ])
    sess.commit()


def setup(dburl, echo, num):
    "setup per test.  create a new Session."
    global session
    session = Session(engine)
    # pre-connect so this part isn't profiled (if we choose)
    session.connection()


def test_lazyload(n):
    "load everything, no eager loading."

    for parent in session.query(Parent):
        parent.children


def test_joinedload(n):
    "load everything, joined eager loading."

    for parent in session.query(Parent).options(joinedload("children")):
        parent.children


def test_subqueryload(n):
    "load everything, subquery eager loading."

    for parent in session.query(Parent).options(subqueryload("children")):
        parent.children

if __name__ == '__main__':
    Profiler.main()