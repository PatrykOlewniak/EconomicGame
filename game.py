from datetime import datetime
from database import *
import random



class Player:
    def __init__(self, name, surname, mail):
        self.name = name
        self.surname = surname
        self.mail = mail
        self.bornInDB() #do poprawienia wywolanie argumentow, bez potrzeby jak sa przy init
        print("The new player : CREATED !")

    """
    creates the new player in database with values took on init
    """
    def bornInDB(self):
        new_player = PlayerDB(name=self.name,surname=self.surname, email=self.mail,startGameDate=datetime.now())
        insert_to_DB(new_player)


    """
    Method shuffle one job from begining jobs (paid 2500-3200$)
    returns jobID
    """
    def get_random_job(self):
        basicJobList = list_of_avaible_jobs(2500,3200)
        randomJob = random.choice(basicJobList)
        return randomJob[0]

    def assign_new_job(self, jobID, playerID):
        pass








#kasia0= Player("Kasia","jakasTam", "thawar@gm0ail.com")

#create_DB('economicGameDB.db')

#create_new_job("First job in Butchery",2800,8)

class Job:
    def show_availble_jobs(self):
        pass