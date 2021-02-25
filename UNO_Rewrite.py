import random, os, sys # Imports

cards = {"Colors": ["Red", "Green", "Blue", "Yellow"], "Specials": ["Wildcard", "+4"], "SpecialsC": ["Skip", "Reverse", "+2"]} # Combination of cards

# Settings
players = 2 # Number of players
minPlayers = 2 # Minimum players allowed
maxPlayers = 15 # Maximum players allowed
maxDrawnCards = 3 # How many cards can be drawn per round

table = f"{cards.get('Colors')[random.randint(0, len(cards.get('Colors')) - 1)]} {random.randint(1, 9)}" # Card on table
hands = {} # Hands of all the players

# Chances - First value is 'less than'. Second value is 'more than'
normal_card_chance = [5, 0] # Chances of a normal card being drawn from 0 to 10.
special_card_chance = [10, 9] # Chances of a special card being drawn. See 'cards' variable.
specialc_card_chance = [8, 6] # Chances of a colored special being drawn. See 'cards' variable.

table_wc_val = None # Used to determine +4 and Wildcard colors
direction = "cw" # The direction of the game. 'cw' = 'Clockwise', 'ccw' = 'Counter Clockwise'

def draw_card(p, n): # Function for drawing cards. 'p' = The player number, 'n' = The number of cards to draw.
    drawn = 0 # How many cards have been drawn so far
    while drawn < n: # While you have drawn less than how many you should draw based on 'n'
        cardType = random.randint(0, 10) # Determines the card you get. See *_card_chance above

        if cardType <= normal_card_chance[0] and cardType >= normal_card_chance[1]: # Normal card chance
            hands[p].append(f"{cards.get('Colors')[random.randint(0, len(cards.get('Colors')) - 1)]} {random.randint(1, 9)}") # Apply the normal card to 'p''s hand
        elif cardType <= special_card_chance[0] and cardType >= special_card_chance[1]: # Special card chance
            hands[p].append(cards.get('Specials')[random.randint(0, len(cards.get('Specials')) - 1)]) # Apply the special card to 'p''s hand
        elif cardType <= specialc_card_chance[0] and cardType >= specialc_card_chance[1]: # Colored Special card chance
            hands[p].append(f"{cards.get('Colors')[random.randint(0, len(cards.get('Colors')) - 1)]} {cards.get('SpecialsC')[random.randint(0, len(cards.get('SpecialsC')) - 1)]}") # Apply the colored special card to 'p''s hand
        
        drawn += 1 # Add 1 to 'drawn'

def play_card(p, conf, dtt): # Called when the player should play a card. 'p' = The player number, 'conf' = True | False - Determines if it should prompt the other users to look away, 'dtt' = Drawn this turn. Used to determine if the user can draw more cards
    # Keep this here or crash?
    global players
    global table
    global table_wc_val
    global direction
    
    nextConf = True # Determines the next 'conf'
    if conf: # Checks if 'conf' is true
        input(f"Player {p}'s turn, other players, look away.\n") # Prompts the other players to look away
    os.system('cls') # Clears the console

    nextp = None # The next player
    if direction == "cw": # Checks if the direction is 'clockwise'
        nextp = p + 1 # Add the player number + 1 to 'nextp'
        if nextp > players: # Checks if 'nextp' is more than the number of players
            nextp = 1 # Sets 'nextp' to 1
    elif direction == "ccw": # Checks if the direction is 'counter clockwise'
        nextp = p - 1 # Add the player number - 1 to 'nextp'
        if nextp < 1: # Checks if 'nextp' is less than 1
            nextp = players # Set 'nextp' to the number of players

    hasToPass = False # Used to determine if the player has to pass. Only used with +2 and +4
    canDraw = True # Used to determine if the player can draw.

    tableSplit = table.split() # Split the table into an array so it's easier to work with
    
    if tableSplit[0] == "+4": # Checks if the card on the table is '+4'
        if len(tableSplit) < 3: # Checks if the length of 'tableSplit' is less than 3. Ex. 'tableSplit' = ["+4", "(Red)"] = 2 < 3, Ex 2. 'tableSplit' = ["+4", "(Red)", "(Used)"] = 3 which is not less than 3
            draw_card(p, 4) # Makes the player draw 4 cards
            table = f"{table} (Used)" # Adds '(Used)' to the card
            hasToPass = True # Makes the player have to pass
    elif tableSplit[1] == "+2": # Checks if the card on the table is '... +2' ('tableSplit' = ["Yellow", "+2"]) tableSplit[1] = "+2"
        if len(tableSplit) < 3: # Checks if the length of 'tableSplit' is less than 3.
            draw_card(p, 2) # Makes the player draw 2 cards
            table = f"{table} (Used)" # Adds '(Used)' to the card
            hasToPass = True # Makes the player have to pass

    drawThisTurn = dtt # Makes 'drawThisTurn' = dtt. See above for 'dtt'
    if drawThisTurn >= maxDrawnCards: # Checks to see if 'drawThisTurn' is more or equals to 'maxDrawnCards'.
        canDraw = False # Makes the player unable to draw more cards.

    print(f"Card on table: {table}\n") # Explains what is on the table
    print(f"Player {p}:\n\nCards:") # Shows more info
    for card in hands[p]: # Goes through the hands of the player and store one at a time in 'card'
        print(card) # Prints the card on the screen

    if hasToPass: # If you have to pass
        input("\nPress enter to continue") # Print "Press enter to continue"
        os.system('cls') # Clear the screen
        play_card(nextp, True, 0) # Makes the player have their turn again

    print("\n") # Print a new line
    for i in range(1, players + 1): # Goes through all the players by number and store the number in 'i'
        print(f"Player {i} has {len(hands[i])} cards left.") # Print out how many cards each player has left
    selectedCard = input("\nWhat card do you want to place?\nType \"draw\" to draw 1 card\nType \"pass\" to pass your turn\n") # Asks you what you want to place

    placedCard = None # Init the variable 'placedCard'
    for card in hands[p]: # Goes through all the cards in the players hand
        if selectedCard.lower() == card.lower(): # Checks if the 'selectedCard' is equals to the 'card' variable.
            placedCard = card # Set 'placedCard' to be equal to 'card'
            break # Break out of the loop

    cheats = True # If you want cheats enabled or not

    if cheats: # If you have cheats enabled
        if selectedCard == "L?vool": # If the "card" you "placed" is equals to "L?vool" which translates to "Hello"
            os.system('cls') # Clears the screen
            input("o?ma!sp! - cards\ns?em? - win\ns!ee!v - give\n") # Prints out the different cheat codes
            play_card(p, False, drawThisTurn)
        if selectedCard == "o?ma!sp!": # If the "card" you "placed" is equals to "o?ma!sp!" which translates to "cards"
            os.system('cls') # Clears the screen
            plr = 1 # Sets the variable 'plr' to 1
            while plr <= players: # While 'plr' is less than the number of players
                print(f"----Player {plr}----") # Print out "----Player (Player number)----"
                for card in hands[plr]: # Goes through 'plr''s hand
                    print(card) # Print the card
                plr += 1 # Add 1 to 'plr'
                print("----------------\n") # Print "----------------"
            input() # Stops and only continues when the player hits enter
            play_card(p, False, drawThisTurn) # Makes the player have their turn again
        if selectedCard == "s?em?": # If the "card" you "placed" is equals to "s?em?" which translates to "win"
            hands[p] = ["+4"]
            play_card(p, False, drawThisTurn)
        if selectedCard == "s!ee!v": # If the "card" you "placed" is equals to "s!ee!v" which translates to "give"
            os.system('cls') # Clears the screen
            give = input("Which card do you want?\n") # Asks the player which card they would want
            giveSplit = give.split() # Splits the request into an array so it's easier to work with

            if len(giveSplit) == 2: # If the length of the request is equal to 2
                if giveSplit[0] in cards["Colors"]: # If the requested color is in the colors
                    if giveSplit[1] in range(1,9) or giveSplit[1] in cards["SpecialsC"]: # If the second part of the request is a number from 1-9 or it's in specialsc
                        hands[p].append(give) # Give the player the card
                        play_card(p, False, drawThisTurn) # Makes the player have their turn again
                        return # Returns
            elif give in cards["Specials"]: # Else if the request is in specials
                hands[p].append(give) # Give the player the card
                play_card(p, False, drawThisTurn) # Makes the player have their turn again
                return # Returns
            else: # Else 
                input("Invalid Card!") # Print out "Invalid Card!"
                play_card(p, False, drawThisTurn) # Makes the player have their turn again
                return # Returns

    if selectedCard == "exit": # If the "card" the player "placed" is equals to "exit"
        confirmation = input("Are you sure you want to exit? Your progress will not be saved. ( Y / N )\n") # Asks the player for confirmation
        if confirmation.lower() == "y": # If the player responds with "y"
            exit() # Exits the program
        elif confirmation.lower() == "n": # If the player responds with "n"
            play_card(p, False, drawThisTurn) # Makes the player have their turn again
        else: # Else
            input("Please select: Y / N\n") # Prints "Please select: Y / N"
            play_card(p, False, drawThisTurn) # Makes the player have their turn again
    if selectedCard == "draw": # If the "card" the player "placed" is equals to "draw"
        if canDraw: # If the player can draw
            drawThisTurn += 1 # Adds 1 to 'drawThisTurn'
            draw_card(p, 1) # Draw 1 card
            play_card(p, False, drawThisTurn) # Makes the player have their turn again
        else: # Else
            input(f"You can not draw more than {maxDrawnCards} cards per turn.") # Print "You can not draw more than ('maxDrawnCards') cards per turn"
            play_card(p, False, drawThisTurn) # Makes the player have their turn again
    if selectedCard == "pass": # If the "card" the player "placed" is equals to "pass"
        os.system('cls') # Clears the screen
        print(f"Player {p} has passed.") # Print "Player (player number) has passed"
        play_card(nextp, nextConf, 0) # Next player's turn

    if placedCard == None: # If you don't place a card
        os.system('cls') # Clears the screen
        input("Invalid card!\n") # Prints "Invalid card!"
        play_card(p, False, drawThisTurn) # Makes the player have their turn again
        return # Returns

    placedCardSplit = placedCard.split() # Makes 'placedCard' into an array so it's easier to work with

    isSpecial = False # Init 'isSpecial'
    if placedCard in cards.get("Specials"): # Checks if the card placed is in specials
        isSpecial = True # Set 'isSpecial' to True
    isCSpecial = False # Init 'isCSpecial'
    if len(placedCardSplit) > 1 and placedCardSplit[1] in cards.get("SpecialsC"): # Checks if the card placed is in colored specials
        isCSpecial = True # Set 'isCSpecial' to True

    successful = None # Init 'successful'

    if len(tableSplit) != 1: # If the length of 'tableSplit' is not equals to 1
        if not isSpecial: # If 'isSpecial' is equal to False
            if isCSpecial: # If 'isCSpecial' is equal to True
                if placedCardSplit[1] == "Skip": # If the placed card second value is "Skip". Ex. "Yellow Skip". placedCardSplit[0] = "Yellow", placedCardSplit[1] = "Skip"
                    if players == 2: # If the number of players is 2
                        nextp = p # Set the next player to be this player
                        nextConf = False # Sets the next "look away" confirmation to show up to False
                    elif nextp >= players: # Else if the nextp player is more or equal to the number of players
                        nextp = 1 # Set the next player to be 1
                    else: # Else
                        if direction == "cw": # If the direction is 'clockwise'
                            nextp += 1 # Add 1 to 'nextp'
                        elif direction == "ccw": # If the direction is 'counter clockwise'
                            nextp -= 1 # Subtract 1 from 'nextp'
                    successful = True # Set 'successful' to True
                elif placedCardSplit[1] == "Reverse": # # If the placed card second value is "Reverse". Ex. "Green Reverse". placedCardSplit[0] = "Green", placedCardSplit[1] = "Reverse"
                    if direction == "cw": # If the direction is 'clockwise'
                        direction = "ccw" # Set the direction to be 'counter clockwise'
                        nextp = p - 1 # Set the next player to be the current player number - 1
                        if players == 2: # If the number of players is equal to 2
                            nextp = p # Set the next player to be the current player
                            nextConf = False # Sets the next "look away" confirmation to show up to False
                        if nextp < 1: # If the next player is less than 1
                            nextp = players # Sets the next player to be equal to the amount of players
                    elif direction == "ccw": # If the direction is 'counter clockwise'
                        direction = "cw" # Set the direction to be 'clockwise'
                        nextp = p + 1 # Set the next player to be the current player number + 1
                        if players == 2: # If the amount of players is equal to 2
                            nextp = p # Set the next player to be equal to the current player
                            nextConf = False # Sets the next "look away" confirmation to show up to False
                        if nextp > players: # If the next player number is more than the amount of players
                            nextp = 1 # Set the next player number to be equal to 1
                    successful = True # Set 'successful' to be True
                elif placedCardSplit[0] == tableSplit[0]: # Else if the colors match
                    successful = True # Set 'successful' to be True
                elif placedCardSplit[1] == tableSplit[1]: # Else if the symbols match
                    successful = True # Set 'successful' to be True
                elif placedCardSplit[0] == table_wc_val: # Else if the card the player placed is equal to the Wildcard or +4 chosen color
                    successful = True # Set 'successful' to be True
                else: # Else
                    successful = False # Set 'successful' to be False
            else: # Else
                if tableSplit[0] == "Wildcard": # If the card on the table is a Wildcard
                    if placedCardSplit[0] == table_wc_val or placedCardSplit[0] == tableSplit[0]: # If the color of the placed card matches the Wildcard
                        successful = True # Set 'successful' to be True
                elif tableSplit[0] == "+4": # Else if the card on the table is a +4
                    if placedCardSplit[0] == table_wc_val or placedCardSplit[0] == tableSplit[0]: # If the color of the placed card matches the +4
                        successful = True # Set 'successful' to be True
                else: # Else
                    if placedCardSplit[1] == tableSplit[1] or placedCardSplit[0] == tableSplit[0]: # If the color or the number matches
                        successful = True # Set 'successful' to be True
                    else: # Else
                        successful = False # Set 'successful' to be False
        else: # Else
            if placedCard == "Wildcard": # If the placed card is a Wildcard
                color = input("Select your color: Red / Green / Blue / Yellow\n") # Ask the player which color they would like
                if color.lower() == "red": # If the player chose "red"
                    placedCard = "Wildcard (Red)" # Set the card's name to be "Wildcard (Red)"
                    table_wc_val = "Red" # Set 'table_wc_val' to be "Red" to be used above
                elif color.lower() == "green": # If the player chose "green"
                    placedCard = "Wildcard (Green)" # Set the card's name to be "Wildcard (Green)"
                    table_wc_val = "Green" # Set 'table_wc_val' to be "Green" to be used above
                elif color.lower() == "blue": # If the player chose "blue"
                    placedCard = "Wildcard (Blue)" # Set the card's name to be "Wildcard (Blue)"
                    table_wc_val = "Blue" # Set 'table_wc_val' to be "Blue" to be used above
                elif color.lower() == "yellow": # If the player chose "Yellow"
                    placedCard = "Wildcard (Yellow)" # Set the card's name to be "Wildcard (Yellow)"
                    table_wc_val = "Yellow" # Set 'table_wc_val' to be "Yellow" to be used above
                else: # Else
                    input("Please select a color") # Asks the player to select a color
                    play_card(p, False, drawThisTurn) # Makes the player have their turn again

                successful = True # Set 'successful' to be True
            else: # Else
                color = input("Select your color: Red / Green / Blue / Yellow\n")
                if color.lower() == "red": # If the player chose "red"
                    placedCard = "+4 (Red)" # Set the card's name to be "Wildcard (Red)"
                    table_wc_val = "Red" # Set 'table_wc_val' to be "Red" to be used above
                elif color.lower() == "green": # If the player chose "green"
                    placedCard = "+4 (Green)" # Set the card's name to be "Wildcard (Green)"
                    table_wc_val = "Green" # Set 'table_wc_val' to be "Green" to be used above
                elif color.lower() == "blue": # If the player chose "blue"
                    placedCard = "+4 (Blue)" # Set the card's name to be "Wildcard (Blue)"
                    table_wc_val = "Blue" # Set 'table_wc_val' to be "Blue" to be used above
                elif color.lower() == "yellow": # If the player chose "yellow"
                    placedCard = "+4 (Yellow)" # Set the card's name to be "Wildcard (Yellow)"
                    table_wc_val = "Yellow" # Set 'table_wc_val' to be "Yellow" to be used above
                else: # Else
                    input("Please select a color\n") # Asks the player to select a color
                    play_card(p, False, drawThisTurn) # Makes the player have their turn again

                successful = True # Set 'successful' to be True
    else: # Else
        successful = True # Set 'successful' to be True

    if successful: # If 'successful' is True
        os.system('cls') # Clear the screen
        table = placedCard # Sets the card on the table to be equal to the card placed
        print(f"\nYou placed a {placedCard}\n") # Print "You placed a (card placed)"
        if (placedCardSplit[0] == "Wildcard" or placedCardSplit[0] == "+4"): # If you placed a Wildcard or a +4
            hands[p].remove(placedCardSplit[0]) # Remove the Wildcard or the +4
        else: # Else
            hands[p].remove(placedCard) # Remove the card placed

        if len(hands[p]) == 0: # If you have no cards left in your hand
            input(f"Player {p} won!") # Print "Player (player number) won!"
            exit() # Exits the game
        
        play_card(nextp, nextConf, 0) # Next player's turn
    else: # Else
        os.system('cls') # Clears the screen
        input(f"\nCan not place a {placedCard} on a {table}\n") # Print "Can not place a (card placed) on a (card on table )"
        play_card(p, False, drawThisTurn) # Makes the player have their turn again

def match_start(p): # Match start function. 'p' = Player number
    # Keep this here or crash?
    global hands
    global cards
    global players

    if players < minPlayers: # If the player amount is less than 'minPlayers'
        raise Exception(f'You can not have less than {minPlayers} players') # Crash the game with a custom error message
    if players > maxPlayers: # If the player amount is more than 'maxPlayers'
        raise Exception(f'You can not have more than {maxPlayers} players') # Crash the game with a custom error message

    if p > players: # If the current player number is more than the amount of players
        play_card(1, True, 0) # Player 1 plays the first card
        return # Returns

    hands[p] = ["null"] # Set hand to "null" to avoid an error
    draw_card(p, 7) # Give the current player 7 cards to begin
    del(hands.get(p)[0]) # Delete the "null" card added above

    match_start(p+1) # Do this again for the next player
    
if len(sys.argv) >= 2: # If the game is opened with command prompt and there are more than or equal to 2 arguments. (py UNO_Rewrite.py) = 1 argument
    if sys.argv[1] == "-p": # If the second argument is "-p"
        if len(sys.argv) >= 4 and sys.argv[3] == "-f": # If the arguments is more than or equal to 4 and argument 4 is equal to "-f". (py UNO_Rewrite.py -p (player number) -f) = 4
            maxPlayers = int(sys.argv[2]) # Set 'maxPlayers' to be the third argument. (player number)
        players = int(sys.argv[2]) # Set the amount of players to be the third argument.

match_start(1) # Start the game