from game import Player, Job


version ="v0.3"

play=False
while(play):
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



job1=Job

job1.assign_job_to_Player(2,2,"2000-10-10")
print(job1.list_of_avaible_jobs())

#kasia0= Player("Kasia","jakasTam", "thawar@gm0ail.com")

#create_DB('economicGameDB.db')

#create_new_job("First job in Butchery",2800,8)