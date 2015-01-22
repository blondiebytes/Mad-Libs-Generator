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

# Add a feature where the user could create a story?

class Story :
    __orderOfParts = [""]
    __inputsEntered = None
    __text = None

    def __init__ (self, orderOfParts, story):
        self.__orderOfParts = orderOfParts
        self.__story = story

    def getOrderOfParts(self, specificIndex = None):
        if specificIndex is None:
            return self.__orderOfParts
        else:
            return self.__orderOfParts[specificIndex]

    def getBasicStoryText(self):
        return self.__text

    def getInputsEntered(self, specificIndex = None):
        if specificIndex is None:
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
            return self.putStoryTogether()

    def putStoryTogether(self):
        basicStory = self.getBasicStoryText()
        inputs = self.getInputsEntered()
        for x in inputs:
            basicStory = basicStory.format(x)
        return basicStory


dayAtDisneyText = "Today, I went to the Disney World with my best friend. I saw a {} {} " \
                  "in a {} show at the Magic Kingdom and ate {} for dinner. The next day I ran {}" \
                  "to meet Mickey Mouse in his {} and that night I gazed at the {} fireworks shooting" \
                  "from the {}"
dayAtDisney = Story(["adjective", "noun", "adjective", "noun", "adverb", "noun", "adjective", "noun"], dayAtDisneyText)

# ------------------
# Yay, this is a thing!
string = "hello there {}"
string = string.format('hello')
print(string)
# ------------------



def welcomeMessage(speech) :
    return "Welcome to the Mad Libs Generator! Enter an {} to start your story!".format('hello')


print(welcomeMessage('speech'))


