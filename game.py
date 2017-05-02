from datetime import datetime, date
from database import *
import random

from database import PlayerDB


class Player:
    def __init__ (self, name, surname, nickname, mail):
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.mail = mail
        self.id = id

    def born_in_DB (self):
        """
        creates the new player in database with values took on init
        Player gain new job on begining. Random one from begining job list
        """
        new_player = PlayerDB(name=self.name,
                              surname=self.surname,
                              nickname=self.nickname,
                              email=self.mail,
                              startGameDate=datetime.now())
        insert_to_DB(new_player)

    def get_ID_of_Player (self):
        query = select([PlayerDB.playerID]).where(PlayerDB.nickname == self.nickname)
        session = open_session()
        result = session.execute(query)
        playerDB_ID = result.fetchone()[0]
        return playerDB_ID

    def get_random_first_job (self):
        """
        Method shuffle one job from begining jobs (paid 2500-3200$)
        :return: jobID
        """
        basicJobList = Job.list_of_avaible_jobs(2500, 3200)
        if (len(basicJobList) > 0):
            randomJob = random.choice(basicJobList)
            return randomJob[0]
        else:
            raise ValueError('could not find any random jobs')

    def set_random_first_job (self):
        """
        sets random first job in table "timeofjobs" where creates
        the assignation job to the player 
        uses the two methods results as argument : get_random_firstjob()
        and get_ID_of_Player()
        """
        try:
            randomJobID = self.get_random_first_job()
            playerID = self.get_ID_of_Player()
            Job.assign_job_to_Player(randomJobID,
                                     playerID,
                                     expirationDate="2020-10-10",
                                     startDate=datetime.now())
        except ValueError:
            print("Can't set the random first job")

    def get_balance_value_from_DB (self):
        """
        Using session and query to get the value of balance in database
        :return: balance amount from PlayerDB.balance
        """
        query = select([PlayerDB.balance]).where(PlayerDB.nickname == "Thavar")
        session = open_session()
        result = session.execute(query)
        balanceDBValue = result.fetchone()[0]
        return balanceDBValue

    def get_list_of_player_jobs (self):
        """
        List o all player jobs from his game begining
        :return: Full list of player jobs. [jobID,startDate,endDate] 
        """
        jobList = []
        actualPlayerID = self.get_ID_of_Player()
        session = open_session()
        query = select([TimeOfJobsDB.jobID, TimeOfJobsDB.startDate, TimeOfJobsDB.endDate]).where(
            TimeOfJobsDB.jobID == actualPlayerID)
        result = session.execute(query)
        for k in result:
            jobList.append(k)
        return jobList


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
        :return: list of tuples (jobIB,name,salary,shift) if exist in range
        """
        jobList = []
        session = open_session()
        s = select([JobDB]).where(JobDB.salary.between(minSalary, maxSalary))
        result = session.execute(s)
        for row in result:
            jobList.append(row)
        return jobList

    def assign_job_to_Player (jobID,
                              playerID,
                              expirationDate,
                              startDate=datetime.now()):
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

    def get_salary_amount (jobID):
        """
        Select from DB and returns the salary amount for input jobID
        :return: salary amount (per month)
        """
        query = select([JobDB.salary]).where(JobDB.jobID == jobID)
        session = open_session()
        result = session.execute(query)
        salaryDBValue = result.fetchone()[0]
        return salaryDBValue

    def get_shift_time (jobID):
        """
        Select from DB and returns the shift value for input jobID
        :return: shift value (int)
        """
        query = select([JobDB.shift]).where(JobDB.jobID == jobID)
        session = open_session()
        result = session.execute(query)
        shiftDBValue = result.fetchone()[0]
        return shiftDBValue
