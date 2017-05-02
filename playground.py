from game import Player, Job
from database import create_DB, PlayerDB
from incomeCalculator import IncomeCalculations
from datetime import datetime


class Playground:
    def __init__ (self):
        self.balance = 0

    def init_message (self):
        version = "v0.3"
        identification = False

        while (not identification):
            answer1 = input("Hello! Are you a new Player?\n")
            if (answer1.lower() == "no"):
                playerNickname = input("So tell me your nickname \n")
                playerInfo = Player.get_player_evidence(_nickname=playerNickname)
                print("Welcome %s %s vel %s in EconomicGame %s ! " % (
                playerInfo[1], playerInfo[2], playerNickname, version))
                player1 = Player(playerInfo[1], playerInfo[2], playerNickname, playerInfo[3])
                balance = player1.total_Income()
                self.balance = balance
                print("Your balance = %s" % balance)
                identification = True


            elif (answer1.lower() == "yes"):
                name = input("Would you like to tell me your name?\n")
                print(('Great! Nice to meet you %s, tell me now your surname. ') % (name))
                surname = input()
                mail = input("and your mail? \n")
                nickname = input("last question : nickname?  \n")
                print("Welcome %s %s vel %s in EconomicGame %s ! " % (name, surname, nickname, version))
                newPlayer = Player(name, surname, nickname, mail)
                newPlayer.born_in_DB()
                newPlayer.set_random_first_job()
                identification = True

            else:
                print("Im not sure what can we do now. I will not ask again...")
                break

    def get_player_command (self):
        """
        ask the player what he want to do 
        and handle basic commands

        """
        command = input("What do you want to do now?\n"
                        "Avaible commends: \n"
                        "BALANCE \n"
                        "NEW JOB LIST\n"
                        "MYJOB\n"
                        )

        if (command == "BALANCE"):
            print(self.balance)

        elif (command == "NEW JOB LIST"):
            fullJobInfo = Job.list_of_avaible_jobs(2000, 3200)
            print(fullJobInfo)


if __name__ == "__main__":
    game1 = Playground()
    game1.init_message()
    game1.get_player_command()
