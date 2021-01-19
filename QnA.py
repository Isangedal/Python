questions = ["What's 0 / 0?", "Do you like cats?",
             "Do you like dogs?", "What is 9+10?", "Which is better? Discord or Skype?", "Is Fortnite dead?", "From 1-10 how cringy is tiktok?", "Fill in the blank: Haha game go ____", "What does the 1st digit of all binary code signify?", "Which question are you on?", "What language is this: 25?"]

answers = ["NaN", "Yes", "Yes", "19", "Discord", "Yes", "10", "brrr", "Idk", "10", "Numbers"]

startLives = 3

wins = 0
losses = 0

modes = ["No-Death", "Normal", "Semi-Hardcore", "Hardcore", "Impossible"]

# Modes: 0 = No-Death, 1 = Normal, 2 = Semi-Hardcore, 3 = Hardcore, 4 = Perfection
# No-Death mode takes no lives
# Normal mode takes 1 life each incorrect answer
# Semi-Hardcore mode takes the number of the question you are on for each incorrent answer
# Hardcore mode takes the number of the question you are on + 1 for each incorrent answers
# Perfection mode sets your lives to 0 for each question you get wrong
mode = 1

lives = startLives

def endGame(w):
    global lives, wins, losses

    lives = startLives

    if w == 1:
        # You won
        print("You Won!")
        wins = wins + 1
        print(f"Wins: {str(wins)}")

        question(0)

    elif w == 0:
        #You lost
        print("You Lost!")
        losses = losses + 1
        print(f"Losses: {str(losses)}")

        question(0)

def debug(q):
    goto = int(input("\nWhich question would you like to go to?\n"))
    
    if goto <= len(questions):
        question(goto - 1)
    else:
        print(f"\nThere are only {str(len(questions))} questions!")
        question(q)

def question(q):
    global lives, mode

    if q >= len(questions):
        endGame(1)

    answerInput = input(f"\n{questions[q]}\n")

    if answerInput.lower() == "debug()":
        debug(q)
        return
    elif answerInput.lower() == "mode list":
        print("Modes:\n")
        for mode in modes:
            print(f"{mode}\n")

        question(q)
        return
    elif answerInput.lower() == "mode check":
        print(f"Mode is currently {modes[mode]}")

        question(q)
        return

    elif answerInput.lower() == "mode change":
        if mode >= len(modes) - 1:
            mode = 0
        else:
            mode = mode + 1

        print(f"Mode set to {modes[mode]}")
        question(q)
        return

    if answerInput.lower() == answers[q].lower():
        # The answer is correct
        print("\nCorrect!")

        question(q+1)
    elif answerInput.lower() != answers[q].lower():
        # The answer is incorrect
        print("\nIncorrect!")

        if mode == 1:
            lives = lives - 1
        elif mode == 2:
            lives = lives - q
        elif mode == 3:
            lives = lives - q - 1
        elif mode == 4:
            lives = 0

        if lives < 0:
            lives = 0

        if mode != 0: 
            if lives != 1:
                print(f"You have {str(lives)} lives left!")
            elif lives == 1:
                print(f"You have 1 life left!")

        if lives == 0:
            endGame(0)

        question(q+1)

# Start the game
print("Welcome to quiz!")
question(0)
