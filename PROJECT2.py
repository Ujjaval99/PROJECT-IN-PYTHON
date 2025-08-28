import random

n = random.randint(1,100)
a = -1
gusses = 1

while(a != n):
    a = int(input("enter the number: "))

    if(a>n):
        print("enter the lower number")
        gusses = gusses +1
    elif(a<n):
        print("enter higher number")
        gusses = gusses+1

print(f"you have gusses the number {n} correctly in {gusses} attemps")
