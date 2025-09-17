try:
    print("Choose what you want to perform :\n" \
    "1. Weight\n" \
    "2. Length\n" \
    "3. Temperature")

    cal = input().strip().lower()

    if(cal == "1" or cal == "2" or cal =="3"):
        print("Dont write the number plz type the line next to that number")

    elif(cal == "length"):
            print("Choose which conversion you want \n" \
            "1. km to m\n" \
            "2. km to cm\n" \
            "3. m to cm\n" \
            "4. cm to m\n" \
            "5. cm to km\n" \
            "6. m to km\n")

            length = input().strip().lower()
            if(length == "km to m"):
                km = int(input("Enter the km you want to convert : "))
                print(km*1000)

            elif(length == "km to cm"):
                km = int(input("Enter the km you want to convert : "))
                print(km*100000)

            elif(length == "m to cm"):
                m = int(input("Enter the m you want to convert : "))
                print(m*100)

            elif(length == "m to km"):
                m = int(input("Enter the m you want to convert : "))
                print(m/1000)

            elif(length == "cm to m"):
                cm = int(input("Enter the cm you want to convert : "))
                print(cm/100)

            elif(length == "cm to km"):
                cm = int(input("Enter the cm you want to convert : "))
                print(cm/100000)

            elif(length == "1" or length == "2" or length == "3" or length== "4" or length == "5" or length == "6"):
                print("Dont write the number plz type the line next to that number")

    elif(cal == "weight"):
            print("Enter which conversion you want \n" \
            "1. kg to g\n" \
            "2. kg to mg\n" \
            "3. g to mg\n" \
            "4. g to kg\n" \
            "5. mg to g\n" \
            "6. mg to kg\n")

            weight = input().strip().lower()
            if(weight == "kg to g"):
                kg = int(input("Enter the kg you want to convert : "))
                print(kg*1000)

            elif(weight == "kg to mg"):
                kg = int(input("Enter the kg you want to convert : "))
                print(kg*1000000)

            elif(weight == "g to mg"):
                g = int(input("Enter the g you want to convert : "))
                print(g*1000)

            elif(weight == "g to kg"):
                g = int(input("Enter the g you want to convert : "))
                print(g/1000)

            elif(weight == "mg to g"):
                mg = int(input("Enter the mg you want to convert : "))
                print(mg/1000)

            elif(weight == "mg to kg"):
                mg = int(input("Enter the mg you want to convert : "))
                print(mg/1000000)

            elif(weight == "1" or weight == "2" or weight == "3" or weight == "4" or weight == "5" or weight == "6"):
                print("Dont write the number plz type the line next to that number")

    elif(cal == "temperature"):
            print("Enter the convertion you want :\n " \
            "1. c to f\n" \
            "2. f to c\n")

            temperature = input().strip().lower()
            if(temperature == "c to f"):
                Celsius = float(input("Enter the temperature in celsius : "))
                print((Celsius*1.8)+32)

            elif(temperature == "f to c"):
                Fahrenheit = float(input("Enter the temperature in fahrenheit : "))
                print((Fahrenheit - 32) * 5/9)

            elif(temperature == "1" or temperature == "2"):
                print("Dont write the number plz type the line next to that number")    

    else:
        print("Write something dont leave it blank or dont write something anonymous")

except ValueError:
     print("Sorry for the ERROR ``")
