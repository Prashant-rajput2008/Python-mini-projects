import random

a = random.randint(1,10)
n = -1
Guesses = 1

while(n != a):
    n = int(input("Guess the number Prashant : "))
    if(n > 150):
        print("Sir ye game 1 se 150 tak hi number guess karne ki hai!! Please iss limit ke hi number chuniye")

    elif(n == a):
        print(f"You Guess the number {n} correctly in {Guesses} attempt")    

    else:
        print("Nope")
        Guesses +=  1