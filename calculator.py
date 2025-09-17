try:
    num1 = int(input("Enter the number 1 : "))
    num2 = int(input("Enter the number 2 : "))

    print("choose the calculation you want to perform \n" \
    "1. ADD \n" \
    "2. SUBSTRACT\n"
    "3. MULTIPLY\n" \
    "4. DIVIDE\n" \
    "5. REMAINDER\n")

    cal = input().strip().lower()

    if(cal == "add"):
        print(num1+num2)

    elif(cal =="substract"):
        print(num1-num2)

    elif(cal == "multiply"):
        print(num1*num2)

    elif(cal == "divide"):
        if(num2 == 0):
            print("Infinity ")
        else:
            print(num1/num2)
    
    elif(cal == "remainder"):
        if(num2 == 0):
            print("That's not Fair sir")
        else:
            print(num1%num2)

    else:
        print("Invalid operation")

except ValueError:
    print("ERROR ``")
