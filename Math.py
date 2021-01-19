def calc(string):
    splitString = string.split()

    if "+" in string:
        print(round(int(splitString[0]) + int(splitString[2])))
    elif "*" in string:
        print(round(int(splitString[0]) * int(splitString[2])))
    elif "/" in string:
        if int(splitString[0]) <= 0 or int(splitString[2]) <= 0:
            print("Can not devide by 0 or less")
        else:
            print(round(int(splitString[0]) / int(splitString[2])))
    elif "^" in string:
        print(round(int(splitString[0]) ** int(splitString[2])))
    elif "-" in string:
        print(round(int(splitString[0]) - int(splitString[2])))

    ask()

def ask():

    debug = True

    userInput = input("\nInput math question.\nFormat: number | + | - | * | / | ^ | number\nExample: 5 * 2\n\n")

    if len(userInput) > 17 and not debug:
        print(f"Reached max number (17): {len(userInput)}")
        ask()
        return
    
    calc(userInput)

    #if "+" in userInput:
    #    calc(userInput, "+")
    #elif "*" in userInput:
    #    calc(userInput, "*")
    #elif "/" in userInput:
    #    calc(userInput, "/")
    #elif "^" in userInput:
    #    calc(userInput, "^")
    #elif "-" in userInput:
    #    calc(userInput, "-")

ask()