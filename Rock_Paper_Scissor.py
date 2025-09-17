import random
'''
0 = rock
1 = paper
-1 = scissor
'''

computer = random.choice([0,1,-1])
youstr = input("Enter your choice : ")
youdict = {"r" : 0,"p" : 1, "s" : -1}
reversedict = {0: "rock", 1: "paper" , -1: "scissor"}

you = youdict[youstr]

print(f"your choice : {reversedict[you]}\ncomputer choice : {reversedict[computer]}")

if(computer == you):
    print("Its a draw\nTry again ")

else:
    if(computer == 0 and you == 1):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Lose!")
    elif(computer == 1 and you == -1):
        print("You Win!")
    elif(computer == 1 and you == 0):
        print("You Lose!")
    elif(computer == -1 and you == 0):
        print("You Win!")
    elif(computer == -1 and you == 1):
        print("You Lose!")
    else:
        print("Something went wrong")