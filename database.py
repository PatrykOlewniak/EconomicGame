from sqlalchemy import Column, Integer, String,DateTime, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



Base = declarative_base()


class TimeOfJobsDB(Base):
    __tablename__='timeofjobs'
    jobID=Column(Integer, primary_key=True)
    playerID = Column(Integer, nullable=True)
    startDate= Column(DateTime)
    endDate = Column(DateTime)


class PlayerDB(Base):
    __tablename__ = 'player'
    playerID = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    startGameDate = Column(DateTime)


class PropertyDB(Base):
    __tablename__ = 'property'
    propertyID = Column(Integer, primary_key=True)
    propertyName = Column(String(250), nullable=False)
    value = Column(Integer, nullable=False)
    playerID = Column(Integer, nullable=True)
    purchaseDate=Column(DateTime)


class JobDB(Base):
    __tablename__='jobs'
    jobID = Column(Integer,nullable=True,primary_key=True)
    jobName = Column(String(250), nullable=False)
    salary = Column(Integer,nullable=True)
    shift = Column(Integer,nullable=True)



def open_session():
    engine = create_engine('sqlite:///economicGameDB.db')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session



def select_from_DB(itemToSearch,tableWhereToSearch):
    """
    Opens the session and insterts the item to DB.
    Takes first argument - itemToSearch - defines that what we want to find
    second argument is about where we want to find it.
    """
    session = open_session()
    s = select([itemToSearch.tableWhereToSearch])
    #s= select([PlayerDB.name])
    result = session.execute(s)
    for row in result:
        print(row)



def insert_to_DB(itemToAdd):
    session = open_session()
    session.add(itemToAdd)
    session.commit()

def create_DB(name):
    """
        Creates the db with specific name.
        Method needs .db extension with the input name
    """
    engine = create_engine('sqlite:///%s'%name)
    Base.metadata.create_all(engine)

def create_new_job(jobName,salary, shift):
    newJob=JobDB(jobName=jobName,salary = salary, shift = shift)
    insert_to_DB(newJob)


def list_of_avaible_jobs(minSalary=0,maxSalary=999999):
    """
    Function wich show list of avaible jobs with selected salary
    
    :param minSalary: first arg of range (includes)
    :param maxSalary: last arg in range (includes)
    :return: list of tuples (jobIB,name,salary,shift) 
    """

    jobList=[]
    session = open_session()
    s = select([JobDB]).where(JobDB.salary.between(minSalary,maxSalary))
    # s= select([PlayerDB.nme])
    result = session.execute(s)

    for row in result:
        jobList.append(row)
    return jobList







