import sys
import random
import os

# MAD LIBS OBJECTIVES
# The user inputs an adjective, noun, or adverb depending on the what the program asks for.
# After entering any number of words (depending on the Mad Lib)*, the program prints out a story with the adjectives,
# nouns, and adverbs the user inputted. (DONE)

# The program should also check to make sure the user inputs the correct part of speech according
# to what the program is asking for. (DONE)

# If the user does not input anything (aka just presses enter), then the program will
# come up with a random adjective, noun, etc to put in the space. (DONE)

# * This program allows for Mad Libs of different lengths to be completed (DONE)

# Adjectives Data Source: http://www.enchantedlearning.com/wordlist/adjectives.shtml
# Adverb Data Source: http://www.momswhothink.com/reading/list-of-adverbs.html#Adverbs List
# Noun Data Source: http://www.talkenglish.com/Vocabulary/Top-1500-Nouns.aspx

# TO DO:
# Feature where user creates a story

class MadLib :
    __orderOfParts = [""]
    __text = [""]
    __inputsEntered = []
    __index = 0

    #Initalizers | Getters & Setters
    #---------------------------------
    def __init__ (self, orderOfParts, story):
        self.__orderOfParts = orderOfParts
        self.__text = story

    #__orderOfParts | Getters & Setters
    def getNextOrderOfParts(self):
        oldIndex = self.getIndex()
        if oldIndex >= len(self.getAllOrderOfParts()):
            return "out"
        else :
            self.incrementIndex()
            return self.getAllOrderOfParts()[oldIndex]

    def getAllOrderOfParts(self):
        return self.__orderOfParts

    #__text | Getters & Setters
    def getBasicStoryText(self):
        return self.__text

    #__inputsEntered | Getters & Setters
    def getInputsEntered(self, index=None):
        if index is None:
            return self.__inputsEntered
        else:
            return self.__inputsEntered[index]

    def setNextInput(self, user):
        # The range takes out /n
        self.__inputsEntered.append(user[:-1])

    #__index | Getters & Setters
    def getIndex(self):
        return self.__index

    def incrementIndex(self):
        self.__index = self.__index + 1

    #Stringing the Story Together
    #-----------------------------
    def stringStory(self):
        if len(self.getInputsEntered()) != len(self.getAllOrderOfParts()):
            return "The story isn't ready yet!"
        else :
            #print out the story with the appropriate input
            return self.putStoryTogether()

    def putStoryTogether(self):
        basicStory = self.getBasicStoryText()
        inputs = self.getInputsEntered()
        finishedStory = ""
        i = 0
        for section in basicStory :
            section = section.format(inputs[i])
            finishedStory = finishedStory + section
            i += 1
        return finishedStory


# Check User Input: if right type of speech
def checkUserInput(speech, userInput) :
    userInput = userInput.lower()
    speechFile = open("{}.txt".format(speech), 'r')
    currentLine = speechFile.readline()
    # Find a better way to store the data so the program doesn't
    # have to go through every entry in the worst case scenario
    # Try to go from O(n) to O(log(n)) or O(1)
    while currentLine != "":
        if currentLine != userInput:
            currentLine = speechFile.readline()
        else:
            speechFile.close()
            return True
    speechFile.close()
    return False

def lengthOfFile(speech):
    speechFile = open("{}.txt".format(speech), 'r')
    with speechFile as f:
        # _ for throwaway variable
        return sum(1 for _ in f)

def randomInput(speech) :
    speechFile = open("{}.txt".format(speech), 'r')
    lengthOfSpeechFile = lengthOfFile(speech)
    #random(0,length of speech file)
    specificLine = random.randrange(0, lengthOfSpeechFile)
    allLines = speechFile.readlines()
    # use index to find a word in speech file
    return allLines[specificLine]



# Example of a Mad Lib
# TO DO: Create a database with many Mad Libs and have the program choose one at random
dayAtDisneyText = ["\nToday, I went to the Disney World with my best friend. I saw a {}",
                   " {} \nin a",
                   " {} show at the Magic Kingdom and ate",
                   " {} for dinner. The next day\nI ran",
                   " {} to meet Mickey Mouse in his",
                   " {} and that night I gazed at \nthe",
                   " {} fireworks shooting",
                   " from the {}."]

dayAtDisney = MadLib(["adjective", "noun", "adjective", "noun", "adverb", "noun", "adjective", "noun"],
                    dayAtDisneyText)


# UI Messages
def welcomeMessage(speech):
    return "Welcome to the Mad Libs Generator! Enter an {} to start your story!".format\
        (speech)

def nextMessage(speech):
    #Add something like if starts with vowel, use an versus a
    return "Enter a {} to continue.".format(speech)

def badInputMessage(speech):
    return "I'm sorry. That is not a {}.".format(speech)

def emptyMessage(speech):
    return "You didn't put anything in so we filled in something else for you --> {}".format(speech)

def endMessage():
    return "Congratulations! You finished your story!"


# WHAT WE RUN:
# -----------------------
# PART I:
firstPartOfSpeech = dayAtDisney.getNextOrderOfParts()
print(welcomeMessage(firstPartOfSpeech))
inputOne = sys.stdin.readline()
while not (checkUserInput(firstPartOfSpeech, inputOne)):
    print(badInputMessage(firstPartOfSpeech))
    inputOne = sys.stdin.readline()
#Check to make sure it matches up to the correct part of speech
dayAtDisney.setNextInput(inputOne)

# PART II:
i = len(dayAtDisney.getAllOrderOfParts()) - 1
for x in range(0, i):
    nextPartOfSpeech = dayAtDisney.getNextOrderOfParts()
    print(nextMessage(nextPartOfSpeech))
    nextInput = sys.stdin.readline()
    #Check to make sure User Input matches up to the correct Part of Speech
    while not (checkUserInput(nextPartOfSpeech, nextInput)):
        if nextInput == "\n":
            nextInput = randomInput(nextPartOfSpeech)
            print(emptyMessage(nextInput))
        else:
            print(badInputMessage(nextPartOfSpeech))
            nextInput = sys.stdin.readline()
    dayAtDisney.setNextInput(nextInput)
   # print(dayAtDisney.getAllOrderOfParts())
   # print(dayAtDisney.getInputsEntered())

# PART III:
print('\n')
print(endMessage())
print(dayAtDisney.stringStory())




