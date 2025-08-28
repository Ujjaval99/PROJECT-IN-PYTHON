#snake,water,gun game
'''
 1 for snake 
-1 for water
 0 for gun
'''
import random
computer = random.choice([1,-1,0])
you = input("enter your choice: ")
youDict = {'s':1,'w':-1,'g':0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
younum = youDict[you]

print(f"your choice {reverseDict[younum]}\ncompute choice {reverseDict[computer]}")

if(computer == younum):
    print("draw")
elif(computer == -1 and younum == 1):
    print("you win!")
elif(computer == -1 and younum == 0):
    print("you lose!")
elif(computer == 1 and younum == 0):
    print("you win!")
elif(computer == 1 and younum == -1):
    print("you lose!")
elif(computer == 0 and younum == 1):
    print("you win!")
elif(computer == 0 and younum == -1):
    print("you lose!")
else:
    print("something wrong")





