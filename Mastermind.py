#Michael Kitzan
#CS 140
#File Name: Mastermind.py
#Explanation: Plays a fully functioning game of 'Mastermind' with four different difficulties
#             Prints out an accurate error list based off player input

from random import *
from os import *

def main():
    """Main menu function, player chooses difficulty."""
    system('cls')
    system('title Mastermind: Main')
    print("Game Start")
    print("Choose Difficulty: Easy, Medium, Hard, or Expert")
    print("Or enter Help for instructions")
    difficulty = input()
    difficulty = difficulty[:4].upper()
    difi(difficulty)

def loseType():
    """Lose function which asks for a new game."""
    print("You maxed your attempts")
    print("Play again? Yes or No")
    answer = input()
    answer = answer[:3].upper()
    if answer == ("YES"):
        main()
    if answer == ("NO"):
        exit()

def winType():
    """Win function which asks for a new game."""
    print("Congratulations, you win!")
    print("Play again? Yes or No")
    answer = input()
    answer = answer[:3].upper()
    if answer == ("YES"):
        main()
    if answer == ("NO"):
        exit()

def difi(allDifficulty):
    """Selects the character set that the opponent will draw from, and that the
    player's guess will be compared to. Also has the 'Help' menu."""
    difficultyEasy = ['G', 'Y', 'R', 'P', 'B', 'W']
    difficultyMedium = ['G', 'Y', 'R', 'P', 'B', 'W', 'C']
    difficultyHard = ['G', 'Y', 'R', 'P', 'B', 'W', 'G', 'Y', 'R', 'P', 'B', 'W']
    difficultyExpert = ['G', 'Y', 'R', 'P', 'B', 'W', 'C', 'G', 'Y', 'R', 'P', 'B', 'W', 'C']
    if allDifficulty == ("HELP"):
        system('cls')
        system('title Mastermind: Instructions')
        print("Objective: Player must guess the four colors of the computer's code within")
        print("twelve attempts")
        print()
        print("Easy Colors: G(reen), Y(ellow), R(ed), P(urple), B(lue), W(hite)")
        print("Medium Colors: G(reen), Y(ellow), R(ed), P(urple), B(lue), W(hite), C(lear)")
        print("Hard Colors: Same colors as easy, except two of the same color can appear in")
        print("             opponent's code")
        print("Expert Colors: Same colors as medium, except two of the same color can appear")
        print("               in opponent's code")
        print()
        print("Guess Notation: Inital of color with no spaces inbetween, not case sensitive")
        print("Program will automatically read the first four characters of your guess")
        print("Example: gwcr")
        print()
        print("At the guess terminal you can enter 'change' to go back and change difficulties")
        print("At the guess terminal you can enter 'exit' to close the game")
        print()
        print("After an error message the program will return to the start, and the opponent")
        print("will have a new code")
        print() 
        input()
        main()
    if allDifficulty in ("EASY"):
        system('title Mastermind: Easy')
        difType = 1
        startGame(difficultyEasy, difType)
    if allDifficulty == ("MEDI"):
        system('title Mastermind: Medium')
        difType = 2
        startGame(difficultyMedium, difType)
    if allDifficulty == ("HARD"):
        system('title Mastermind: Hard')
        difType = 3
        startGame(difficultyHard, difType)
    if allDifficulty == ("EXPE"):
        system('title Mastermind: Expert')
        difType = 4
        startGame(difficultyExpert, difType)


def startGame(setList, difType):
    """Beginning of the game randomizes and selects the opponent’s code, so when
    player returns after an error they have to guess on a new code."""
    system('cls')
    shuffle(setList)
    opponent = [setList[0], setList[1], setList[2], setList[3]]
    print("Start Guessing:")
    #print(opponent)
    print()
    count = 0
    guess = input()
    guess = guess[:4].upper()
    checkError(guess, opponent, setList, count, difType)

def checkError(guess, opponent, setList, count, difType):
    """Runs through the players guess to determine if there any errors, and returns
    an error list if so."""
    if guess == ("CHAN"):
        main()
    if guess == ("EXIT"):
        exit()
    mult = 0
    nonValid = set([])
    lenGuess = len(guess)
    check1 = False
    check2 = False
    check3 = False
    check4 = False
    tick = False
    if lenGuess != 4:
        check1 = True
        tick = True
    for i in range(lenGuess):
        if guess[i] not in setList:
            check2 = True
            tick = True
    if difType in (1, 2):
        for i in range(lenGuess):
            for j in range(i+1, lenGuess):
                if guess[i] == guess[j]:
                    check3 = True
                    tick = True
    if difType in (3, 4):
        for i in range(lenGuess):
            for j in range(i+1, lenGuess):
                if guess[i] == guess[j]:
                    mult += 1
                    if mult > 2:
                        trip = guess[i]
                        check4 = True
                        tick = True
    if tick == True:
        print("Error List:")
        if check1 == True:
            if lenGuess != 4:
                print("Guess is not four characters")
        if check2 == True:
            mult = 0
            for i in range(lenGuess):
                if guess[i] not in setList:
                    nonValid.add(guess[i])
            for k in nonValid:
                print(k, "is not a valid character")
        if check3 == True:
            nonValid = set([])
            for i in range(lenGuess):
                for j in range(i+1, lenGuess):
                    if guess[i] == guess[j]:
                        nonValid.add(guess[i])
            for k in nonValid:
                print(k, "appears multpile times")
        if check4 == True:
            print(trip, "appears too many times")
        input()
        startGame(setList, difType)
    else:
        coreGame(guess, opponent, setList, count, difType)
    #All that just to get the 'Error List:' reading to format as it does

def coreGame(guess, opponent, setList, count, difType):
    """Determines the exact matches, and if there are similar colors between the
    guess and the opponents code. Checks the difficulty, and adjusts for the possibility
    of the opponents code having multiples."""
    count += 1
    tally = 0
    for i in range(4):
        if guess[i] == opponent[i]:
            tally += 1
    check = 0
    close = 0
    if difType in (3, 4): 
        for i in range(4):
            if guess[i] in opponent:
                close += 1
        for k in range(4):
            for m in range(k+1, 4):
                if guess[k] == guess[m]:
                    if guess[m] in opponent:
                        check += 1
        feed = close - tally - check
        extra1 = False
        extra2 = False
        for i in range(4):
            for j in range(i+1, 4):
                if guess[i] == guess[j]:
                    extra1 = True
        for i in range(4):
            for j in range(i+1, 4):
                if opponent[i] == opponent[j]:
                    extra2 = True
        if (extra1 and extra2) == True:
            feed = close - tally
    else:
        for i in range(4):
            if guess[i] in opponent:
                close += 1
        feed = close - tally
    print("Match: ", tally, "/ 4")
    print("Close: ", feed, "/ 4")
    print("Attempt: ", count, "/ 12")
    print()
    if tally == 4:
        winType()
    if count == 12:
        loseType()
    guess = input()
    guess = guess[:4].upper()
    checkError(guess, opponent, setList, count, difType)

main()