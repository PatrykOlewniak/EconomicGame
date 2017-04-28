from sqlalchemy import Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class TimeOfJobsDB(Base):
    __tablename__='timeofjobs'
    jobID=Column(Integer, primary_key=True)
    startDate= Column(DateTime)
    endDate = Column(DateTime)


class PlayerDB(Base):
    __tablename__ = 'player'
    playerID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    startGameDate=Column(DateTime)


class PropertyDB(Base):
    __tablename__ = 'property'
    propertyID = Column(Integer, primary_key=True)
    propertyName = Column(String(250), nullable=False)
    value = Column(Integer, nullable=False)
    playerID = Column(Integer,nullable=True)
    purchaseDate=Column(DateTime)


class JobDB(Base):
    __tablename__='jobs'
    jobID=Column(Integer,nullable=True)
    playerID=Column(Integer, primary_key=True)
    jobName=Column(String(250), nullable=False)
    shift=Column(Integer,nullable=True)



def open_session():
    engine = create_engine('sqlite:///economicGameDB.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


def select_from_DB(itemToSearch,tableWhereToSearch):
    """
        Opens the session and insterts the item to DB.
    """

def insertert_to_DB(itemToAdd):
    session=open_session()
    session.add(itemToAdd)
    session.commit()

"""
    Creates the db with specific name.
    Method needs .db extension with the input name
"""
def create_DB(name):
    engine = create_engine('sqlite:///%s'%name)
    Base.metadata.create_all(engine)

def create_new_job(_jobName,_shift):
    newJob=JobDB(jobName=_jobName,shift=_shift)
    insertert_to_DB(newJob)




