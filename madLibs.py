import sys
import os

# MAD LIBS OBJECTIVES
# The user inputs an adjective, noun, adverb, or verb, depending on the what the program asks for.
# After entering 8 words, the program prints out a story with the adjectives, nouns, adverbs, and
# verbs the user inputted.

# The program should also check to make sure the user inputs the correct part of speech according to
# what the program is asking for.

# If the user does not input anything (aka just presses enter), then the program will come up with a random
# adjective, noun, etc to put in the space.

class Story :
    __orderOfParts = [""]
    __inputsEntered = [""]
    __story = [""]

    def __init__ (self, orderOfParts, inputsEntered):
        self.__orderOfParts = orderOfParts
        self.__inputsEntered = inputsEntered

    def getOrderOfParts(self, specificIndex = None):
        if specificIndex is None :
            return self.__orderOfParts
        else:
            return self.__orderOfParts[specificIndex]

    def getInputsEntered(self, specificIndex = None):
        if specificIndex is None :
            return self.__inputsEntered
        else:
            return self.__inputsEntered[specificIndex]

    def setNextInput(self, specificInput):
        self.__inputsEntered.append(specificInput)

    def stringStory(self, story):
        if len(self.getInputsEntered()) != len(self.getOrderOfParts()) :
            return "The story isn't ready yet!"
        else :
            #print out the story with the appropriate input
            return ""




def welcomeMessage(speech) :
    return "Welcome to the Mad Libs Generator! Enter an {} to start your story!".format('hello')


print(welcomeMessage())


