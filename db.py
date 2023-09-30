
2
3
4
5
6
7
8
9
10
11
12
13
14
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()
RDB_PATH = 'sqlite:///db.sqlite3'
ECHO_LOG = True
 
engine = create_engine(
   RDB_PATH, echo=ECHO_LOG
)
 
Session = sessionmaker(bind=engine)
session = Session()