# import libraries
import random
import types
import math
import time
import os
import textwrap
from datetime import datetime
# Declare global constant variables
MENU_ITEMS = {
    "inputMsg": "Choose: ",
    "errorMsg": "Please choose option 1, 2, or 3 only",
    "optionList": ["Play game", "Show all scores", "Quit"]
}
REPLAY_GAME_ITEMS = {
    "inputMsg": "Do you want to play again ? (Y/N)  ",
    "errorMsg": "Please enter y or n only",
    "optionList": ["y", "n"]
}

SAVE_GAME_SCORE_ITEMS = {
    "inputMsg": "Do you want to save score ? (Y/N)  ",
    "errorMsg": "Please enter y or n only",
    "optionList": ["y", "n"]
}

SCORE_FILE_NAME = "score.txt"
# display text in center of screen


def centerText(text, width, char=" "):
    return text.center(width, char)

# calculate column length to display list beautifully


def calcColLength(text, width):
    if (len(text) > width):
        text = textwrap.wrap(text, width)
    if (len(text) < width):
        text = text + " " * (width - len(text))
    return text

# custom sleep function


def custom_sleep_milliseconds(milliseconds):
    if (milliseconds == 0):
        return
    seconds = milliseconds / 1000.0
    start_time = time.time()
    while time.time() - start_time < seconds:
        pass

# clear console screen


def clearScreen(milliseconds=0):
    custom_sleep_milliseconds(milliseconds)
    os.system('cls')

# display countdown timer


def countDown(t):
    clearScreen()
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(centerText(timer, 50))
        custom_sleep_milliseconds(1300)
        clearScreen()
        t -= 1

# display waiting screen with 5 dots


def waitingScreen(msg="Waiting"):
    t = 1
    print(msg, end="", flush=True)
    while (t <= 5):
        print(".", end="", flush=True)
        custom_sleep_milliseconds(1000)
        t += 1

# check if n is an interger string


def isInteger(n):
    if (type(n) == int):
        return True
    if (n[0] == "-"):
        return n.strip("-").strip().isdigit()
    if (len(n) >= 1):
        return n.strip().isdigit()


# check if n is an integer with correct length
def checkIntegerLength(n, length):
    return len(str(n)) == length

# check if fn is a function


def isFunction(fn):
    if (not isinstance(fn, types.FunctionType)):
        raise ValueError("Please pass a function as parameter")
    return True

# check if choice available in choices


def isValidChoice(choice, choices):
    return choice in choices

# check if file exists


def isFile(filePath):
    return os.path.isfile(filePath)

# read file


def readFile(fileName):
    try:
        with open(fileName, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        print("File not found")
        return None

# write to a file, with mode = append


def writeFile(fileName, content):
    try:
        with open(fileName, "a") as f:
            f.write(content)
    except FileNotFoundError:
        print("File not found")
        return None

# get user input as integer, but no space or blank input or input <= 0 allowed


def getIntInput(msg="Input item: "):
    n = input(msg)
    while not isInteger(n) or int(n) <= 0:
        print("Please enter a number > 0")
        n = input(msg)
    return int(n)

# get user input as string, but no space or blank input allowed


def getInput(msg="Input item: "):
    n = input(msg)
    while (len(n) == 0):
        print("Please enter something")
        n = input(msg)
    return n

# get user input to a list


def getInputList(listSize, fnInput):
    myList = []
    if (isFunction(fnInput)):
        for i in range(listSize):
            item = fnInput("Input item {}: ".format(i))
            myList.append(item)
        return myList

# get user input to choose an option from a list of choices


def getChoice(inputMsg, errorMsg, choices):
    choice = getInput(inputMsg).lower()
    while (not isValidChoice(choice, choices)):
        print(errorMsg)
        choice = getInput(inputMsg)
    return choice

# print list beautifully


def prettyPrintList(myList):
    if (len(myList) == 0):
        print("Empty list")
        return
    board = ""
    for i in myList:
        board += str(i)
        if (i != myList[-1]):
            board += "  |  "
    print(centerText(board, 50))

# compare two lists

def compareLists(firstList, secondList):
    if (len(set(firstList)) != len(set(secondList))):
        return False

    return firstList == secondList

# generate a random number with start and end


def generateRandNumber(start, end):
    return random.randint(start, end)

# generate random list with no duplicate items


def generateRandList(listSize, start, end, itemLength):
    myList = []
    while (len(myList) < listSize):
        item = generateRandNumber(start, end)
        if (checkIntegerLength(item, itemLength)):
            if (item in myList):
                continue
            myList.append(item)
    return myList


# print game menu
def printMenu():
    for idx, item in enumerate(MENU_ITEMS.get('optionList')):
        print("{}. {}".format(idx+1, item))

# print leaderboard score from file


def printLeaderboard():
    headerCol = ["#", "name", "score", "date"]
    if (not isFile(SCORE_FILE_NAME)):
        print(centerText(" No score yet ", 70, "#"))
        return
    readthefile = readFile("score.txt")
    for i in readthefile:
        temp = i.strip("\n")
        splitTemp = temp.split(",")
        splitTemp[1] = int(splitTemp[1])
        splitTemp[2] = splitTemp[2].strip()
        readthefile[readthefile.index(i)] = splitTemp
    print(centerText("#", 100, "#"))
    print(centerText("Leaderboard", 70))
    print("-"*100)

    for i in headerCol:
        print(calcColLength(i.capitalize(), 20), end=" ")
    print()
    for idx, data in enumerate(readthefile):
        print("{0} {1} {2} {3}".format(
            calcColLength(str(idx + 1), 20),
            calcColLength(data[0], 20),
            calcColLength(str(data[1]), 20),
            calcColLength(str(data[2]), 20)
        ))
    print(centerText("#", 100, "#"))

# get user name from keyboard


def getUserName():
    name = getInput("Enter your name: ")
    return name

# get user input to choose menu item


def chooseMenuItem(inputMsg, errorMsg, choices):
    convertChoices = [str(i+1) for i in choices]
    choice = getChoice(inputMsg, errorMsg, convertChoices)
    return choice

# get user input to choose whether to replay game or not


def chooseReplayGame(inputMsg, errorMsg, choices):
    choice = getChoice(inputMsg, errorMsg, choices)
    if (choice == "y"):
        return 1
    return -1

# get user input to choose whether to save score or not


def chooseSaveGameScore(inputMsg, errorMsg, choices):
    choice = getChoice(inputMsg, errorMsg, choices)
    if (choice == "y"):
        return 1
    return -1

# get user input to choose whether to go back to menu or not


def goBackToMenu():
    choice = getChoice(
        "Which action you wanna do ?\n1. Go back to menu\n2. Exit\n", "", ["1", "2"])
    if (choice == "1"):
        return True
    return False

# Main function to play one round of game, decide which round you win and which round you lost
def playOneRound(currentRound, totalRound):
    i = currentRound
    print("{}Round {}{}".format(" ", i, " ").center(50, "="))
    gameList = generateRandList(
        totalRound, math.pow(10, i-1), math.pow(10, i), i)
    prettyPrintList(gameList)
    custom_sleep_milliseconds(i*1300)
    clearScreen()
    print("Enter your guess: ")
    userList = getInputList(totalRound, getIntInput)
    return [gameList, userList]

# Main function to play game with input for totalRound and check if win or lóe
def play():
    totalRound = getIntInput("Enter number of round you want to play: ")
    for i in range(totalRound+1):
        if (i > 0):
            clearScreen()
            gameList, userList = playOneRound(i, totalRound)
            if (not compareLists(gameList, userList)):
                i -= 1
                break
            waitingScreen("Checking")
            custom_sleep_milliseconds(900)
            print()
            print(centerText("==> Correct !", 30))
            if (i != totalRound):
                waitingScreen("Moving to next round")
    print()
    return [i, totalRound]

# Function to save score to a file
# Data to save: username, score, date


def saveGameScore(score):
    choice = chooseSaveGameScore(SAVE_GAME_SCORE_ITEMS.get(
        'inputMsg'), SAVE_GAME_SCORE_ITEMS.get("erroMsg"), SAVE_GAME_SCORE_ITEMS.get("optionList"))
    if (choice == 1):
        userName = getUserName()
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        userScoreData = "{}{},{},{}".format("\n", userName, score, dt_string)
        if (not isFile(SCORE_FILE_NAME) or readFile(SCORE_FILE_NAME) is None):
            userScoreData = "{}{},{},{}".format("", userName, score, dt_string)
        writeFile(SCORE_FILE_NAME, userScoreData)
        waitingScreen("Saving")
        print("\nYour score is saved")
    return

# Function to run game with screen and function to play game


def startGame():
    countDown(4)
    print(centerText("Welcome to memory game", 50))
    score, totalRound = play()
    gameData = [score, totalRound]
    return gameData

# Main function:
# Choose 1 => Play game
# Choose 2 => Show all scores
# Choose 3 => Do nothing and just quit


def main():
    showMenu = True
    while (True):
        clearScreen()
        if (showMenu):
            printMenu()
            menuAction = chooseMenuItem(MENU_ITEMS.get('inputMsg'), MENU_ITEMS.get(
                'errorMsg'), range(len(MENU_ITEMS.get('optionList'))))
        if (menuAction == "1"):
            score, totalRound = startGame()
            if (score == totalRound):
                print("You win")
            else:
                print("You lose")
            clearScreen(1500)
            replayChoice = chooseReplayGame(REPLAY_GAME_ITEMS.get(
                'inputMsg'), REPLAY_GAME_ITEMS.get("erroMsg"), REPLAY_GAME_ITEMS.get("optionList"))
            if (replayChoice != 1):
                saveGameScore(score)
                if (not goBackToMenu()):
                    waitingScreen("Bye Bye")
                    break
                waitingScreen()
            showMenu = False
            continue
        if (menuAction == "2"):
            clearScreen()
            waitingScreen()
            clearScreen()
            printLeaderboard()
            if (not goBackToMenu()):
                waitingScreen("Bye Bye")
                break
            showMenu = True
            continue
        if (menuAction == "3"):
            print("Bye bye")
        break


main()
