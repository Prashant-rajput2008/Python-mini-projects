import random

a = random.randint(1,150)
n = -1
Guesses = 1


while(n != a):
    n = int(input("Guess the number Prashant : "))

    if(n > 150):
        print("Sir ye game 1 se 150 tak hi number guess karne ki hai!! Please iss limit ke hi number chuniye")

    elif(n+40 < a):
        print("Itna Chota Number!! 🙄🙄")
        Guesses += 1
        

    elif(n-40 > a):
        print("Itna Bada Number!! 😱😱")
        Guesses += 1


    elif(n>a):
        print("Prashant ji please chota number daaliye")
        Guesses +=1

    elif(n<a):
        print("Prashant ji please bada number daaliye")
        Guesses +=1


    else:
        print(f"You Guess the number {n} correctly in {Guesses} attempt")    
