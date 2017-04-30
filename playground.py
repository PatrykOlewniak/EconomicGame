from game import Player
from database import list_of_avaible_jobs
version ="v0.3"


answer1 = input ("Hello! Are you a new Player?\n")
if (answer1.lower()=="yes"):
    print ("YOU SHOULD BE BORN HERE!")
else:
    name = input("Would you like to tell me your name?\n")
    print(('Great! Nice to meet you %s, tell me now your surname. ')%(name,))
    surname = input()
    mail = input("and your mail? \n")
    print("Welcome %s %s in EconomicGame %s ! "%(name,surname,version))

ania3=Player("Ania","Kundzia","an99iaa@gmail.com")
print (ania3.get_random_job())
