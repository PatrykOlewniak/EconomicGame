from game import Player, Job
from database import create_DB

class Playground:
    def init_message(self):
        version ="v0.3"
        play=False
        while(play):
            answer1 = input ("Hello! Are you a new Player?\n")
            if (answer1.lower()=="yes"):
                print ("YOU SHOULD BE BORN HERE!")
                return 1
            else:
                name = input("Would you like to tell me your name?\n")
                print(('Great! Nice to meet you %s, tell me now your surname. ')%(name,))
                surname = input()
                mail = input("and your mail? \n")
                print("Welcome %s %s in EconomicGame %s ! "%(name,surname,version))
                return 0


Patryk = Player("Patryk","Olewniak","Thavar", "thawar@gmail.com")
Kasia= Player("Kasia", "Kasinska", "Kasiulek883","K@sia@gmail.com")
Kasia.born_in_DB()
#Patryk.born_in_DB()
print (Patryk.get_balance_value_from_DB())
#print(Patryk.get_ID_of_Player())
#Patryk.set_random_first_job()


#job1.assign_job_to_Player(2,2,"2000-10-10")
#print(job1.list_of_avaible_jobs())

#kasia0= Player("Kasia","jakasTam", "thawar@gm0ail.com")

#create_DB('economicGameDB.db')

#Job.create_new_job("First job in Office",2600,7)