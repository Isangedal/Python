import random
import os

card_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
card_colors = ["Red", "Blue", "Green", "Yellow"]
card_specials = ["Wildcard", "+4"]
card_specials_c = ["Skip", "Reverse", "+2"]

hand = []
table = card_colors[random.randint(0, len(card_colors) - 1)] + " " + card_numbers[random.randint(0, len(card_numbers) - 1)]

def start():
    global table

    os.system('cls')

    if len(hand) != 7:
        #isSpecial = random.randint(1, 4)
        isSpecial = random.randint(1, 6)

        if isSpecial == 4:
            hand.append(card_specials[random.randint(0, len(card_specials) - 1)])
        elif isSpecial == 3:
            hand.append(card_colors[random.randint(0, len(card_colors) - 1)] + " " + card_specials_c[random.randint(0, len(card_specials_c) - 1)])
        else:
            hand.append(card_colors[random.randint(0, len(card_colors) - 1)] + " " + card_numbers[random.randint(0, len(card_numbers) - 1)])
            
        start()

    else:
        placeCard()

def placeCard():
    global table

    os.system('cls')

    print(f"Card on table: {table}\n\n")

    print("Cards:")
    for card in hand:
        print(card)

    selectCard = input("\nWhat card do you want to place?\n")
    
    if selectCard == "give()":
        os.system('cls')
        give = input("Which card do you want?\n")
        giveSplit = give.split()

        # Yellow 4
        # ["Yellow", "4"]
        # ["+4"]

        if len(giveSplit) == 2:
            if giveSplit[0] in card_colors:
                if giveSplit[1] in card_numbers or giveSplit[1] in card_specials_c:
                    hand.append(give)
                    input(f"You have been given a {give}\n")
                    placeCard()
                    return
        if give in card_specials:
            hand.append(give)
            input(f"You have been given a {give}\n")
            placeCard()
            return
        else:
            input(f"Invalid Card!")
            placeCard()
            return
        
    elif selectCard == "table()":
        os.system('cls')
        inTable = input("Which card do you want?\n")
        tableSplit = inTable.split()

        if len(tableSplit) == 2:
            if tableSplit[0] in card_colors:
                if tableSplit[1] in card_numbers or tableSplit[1] in card_specials_c:
                    table = inTable
                    input(f"Table changed to {table}\n")
                    placeCard()
                    return
        if inTable in card_specials:
            table = inTable
            input(f"Table changed to {table}\n")
            placeCard()
            return
        else:
            input(f"Invalid Card!")
            placeCard()
            return
    elif selectCard == "redraw()":
        os.system('cls')
        sure = input("Are you sure you want to re draw all your cards? (Y / N)\n")
        if sure.lower() == "y":
            hand.clear()
            start()
            return
        else:
            input("Cancelled!")
            placeCard()
            return
    elif selectCard == "exit":
        os.system('cls')
        sure = input("Are you sure you want to exit? (Y / N)\n")
        if sure.lower() == "y":
            os.system('exit')
            return
        else:
            input("Cancelled!")
            placeCard()
            return

    placedCard = None
    for card in hand:
        if selectCard.lower() == card.lower():
            placedCard = card
            break

    if placedCard == None:
        os.system('cls')
        input("Invalid card!\n")
        placeCard()
        return

    placedCardSplit = placedCard.split()
    tableSplit = table.split()

    isSpecial = False
    for special in card_specials:
        if placedCard == special:
            isSpecial = True
            break

    isCSpecial = False
    for special in card_specials_c:
        if placedCard == special:
            isCSpecial = True
            break

    successful = None

    # ["Yellow", "9"]

    # Rules
    if len(tableSplit) != 1:
        if not isSpecial:
            if isCSpecial:
                if placedCardSplit[0] == tableSplit[0]:
                    successful = True
                else:
                    successful = False
            else:
                if placedCardSplit[0] == tableSplit[0] or placedCardSplit[1] == tableSplit[1]:
                    successful = True
                else:
                    successful = False
        else:
            successful = True
    else:
        successful = True

    if successful:
        os.system('cls')
        hand.remove(placedCard)
        table = placedCard
        print(f"\nYou placed a {placedCard}\n")

        if len(hand) == 0:
            input("You Won!")
            start()
            return
    else:
        os.system('cls')
        input(f"\nCan not place a {placedCard} on a {table}.\n")

    placeCard()
    

start()