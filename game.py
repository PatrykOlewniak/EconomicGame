from datetime import datetime, date
from database import *
import random


class Player:
    def __init__ (self, name, surname, nickname, mail):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.mail = mail

    def born_in_DB (self):
        """IntegrityError
        creates the new player in database with values took on init
        Player gain new job on begining. Random one from begining job list
        """
        new_player = PlayerDB(name=self.name,
                              surname=self.surname,
                              nickname=self.nickname,
                              email=self.mail,
                              startGameDate=datetime.now())
        insert_to_DB(new_player)

    def get_random_job (self):
        """
        Method shuffle one job from begining jobs (paid 2500-3200$)
        :return: jobID
        """
        basicJobList = Job.list_of_avaible_jobs(2500, 3200)
        randomJob = random.choice(basicJobList)
        return randomJob[0]

    def get_balance_value_from_DB(self):
        """
        Using session and query to get the value of balance in database
        :return: balance amount from PlayerDB.balance
        """
        query = select([PlayerDB.balance]).where(PlayerDB.nickname=="Thavar")
        session = open_session()
        result = session.execute(query)
        balanceDBValue=result.fetchone()[0]
        return balanceDBValue




class Job:
    def create_new_job (jobName, salary, shift):
        """
        Admin method - creates new job using ORM 
        :param salary: salary in $
        :param shift: shift in hours 8- full shift
        """
        newJob = JobDB(jobName=jobName, salary=salary, shift=shift)
        insert_to_DB(newJob)

    def list_of_avaible_jobs (minSalary=0, maxSalary=9999999):
        """
        Function wich show list of avaible jobs with selected salary
        Uses the open session method
        :param minSalary: first arg of range (includes)
        :param maxSalary: last arg in range (includes)
        :return: list of tuples (jobIB,name,salary,shift) 
        """
        jobList = []
        session = open_session()
        s = select([JobDB]).where(JobDB.salary.between(minSalary, maxSalary))
        result = session.execute(s)
        for row in result:
            jobList.append(row)
        return jobList

    def assign_job_to_Player (jobID, playerID, expirationDate, startDate=datetime.now()):
        """
        Admin Function which assign existed player with existed job 
        :param playerID
        :param expirationDate: format : YYYY-MM-DD
        :param startDate: default is now.
        """
        try:
            year, month, day = map(int, expirationDate.split('-'))
            expirationDateFormat = datetime(year, month, day)
            newTimeOfJobInstance = TimeOfJobsDB(jobID=jobID,
                                                playerID=playerID,
                                                endDate=expirationDateFormat,
                                                startDate=startDate)
            insert_to_DB(newTimeOfJobInstance)
        except IntegrityError:
            print("Sorry, can't do that.")
