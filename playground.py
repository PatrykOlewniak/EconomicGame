from game import Player, Job
from database import create_DB, PlayerDB
from incomeCalculator import IncomeCalculations
from datetime import datetime

class Playground:
    def init_message(self):
        version ="v0.3"
        identification=False

        while(not identification):
            answer1 = input ("Hello! Are you a new Player?\n")
            if (answer1.lower()=="no"):
                playerNickname= input ("So tell me your nickname \n")
                playerInfo=Player.get_player_evidence(_nickname=playerNickname)

                print("Welcome %s %s vel %s in EconomicGame %s ! " % (playerInfo[1], playerInfo[2], playerNickname, version))
                #balance=Player.get_balance_value_from_DB(playerNickname)
                #print("Your balance = %s"%balance)
                identification = True


            else:
                name = input("Would you like to tell me your name?\n")
                print(('Great! Nice to meet you %s, tell me now your surname. ')%(name))
                surname = input()
                mail = input("and your mail? \n")
                nickname = input("and your mail? \n")
                print("Welcome %s %s vel %s in EconomicGame %s ! "%(name,surname,nickname,version))
                identification = True

    def assign_nickname_to_Player(self,nickname):
        pass


game1=Playground()
game1.init_message()

"""
print (Player.get_player_evidence(_nickname="Thavar"))
Patryk = Player("Patryk","Olewniak","Thavar", "thawar@gmail.com")
#Kasia= Player("Kasia", "Kasinska", "Kasiulek883","K@sia@gmail.com")
#Kasia.born_in_DB()
#Patryk.born_in_DB()
print (Patryk.get_balance_value_from_DB())
print (Patryk.get_list_of_player_jobs())
print (Job.get_salary_amount(1))
print (Job.get_shift_time(1))
PatrykCalculations=IncomeCalculations()
print(PatrykCalculations.incomeInPeriod(Job.get_salary_amount(1),Job.get_shift_time(1),
               Patryk.get_list_of_player_jobs()[0][1],Patryk.get_list_of_player_jobs()[0][2]))
print (PatrykCalculations.secondsCountFromDateToDate(datetime(2000,10,10), datetime(2000,9,9)))
print (datetime(2000,8,10) - datetime(2000,9,9))
#print(Patryk.get_ID_of_Player())
#Patryk.set_random_first_job()


#job1.assign_job_to_Player(2,2,"2000-10-10")
#print(job1.list_of_avaible_jobs())

#kasia0= Player("Kasia","jakasTam", "thawar@gm0ail.com")

#create_DB('economicGameDB.db')

#Job.create_new_job("First job in Office",2600,7)
"""