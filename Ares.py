ares_quotes= \
[
"I'm sorry, I don't know what you want",
]

# pylint: disable=W1401
# pylint: disable=W0612
import praw
import random
import re
import os
import time
import sys

#Custom math module
from MathFrame import Calculator

class Bot():
    def __init__(self, sub):
        #Selecting the subreddit and starting... stuff...
        reddit = praw.Reddit('Ares')
        self.subreddit = reddit.subreddit(sub)

        #Current way of keeping track of respnded messages, will change soon, but as of now it reads and writes to a file
        #All the comment ID's that it has ressponded to
        self.fil = "responded.txt" 

        if not os.path.isfile(self.fil):
            self.comments_responded = []
            with open(self.fil, "w") as f:
                pass

        else:
            with open(self.fil, "r") as f:
                self.comments_responded = f.read()
                self.comments_responded = self.comments_responded.split("\n")
                self.comments_responded = list(filter(None, self.comments_responded))


    def begin(self):
        #Checks all the most recent comments
        for comment in self.subreddit.stream.comments():
            #Checks if it has been responded to, method wil change soon
            if comment.id not in self.comments_responded:
                #Optional call-word, currently no aditional call-word is necessary 
                if re.search("", comment.body, re.IGNORECASE):
                    self.descide(comment)

    def descide(self, comment):
        try:
            #Searhing every comment for the call-functions
            if re.search("critChance\((.*)\)", comment.body, re.I|re.M):
                #Ob is the entire snippet
                ob = re.search("critChance\((.*)\)", comment.body, re.I|re.M)
                #Ob[1] is the string of arguments that are going to be passed to the function
                #Calculator from the import being initialized
                Calc = Calculator()
                #first set up the method call as a string to format in the string of arguments
                command = "Calc.critChance({})".format(ob[1])
                #Get the return of the method
                message = eval(command)
                self.comment(comment, message)

            elif re.search("statusProcs\((.*)\)", comment.body, re.I|re.M):
                #Ob is the entire snippet
                ob = re.search("statusProcs\((.*)\)", comment.body, re.I|re.M)
                #Ob[1] is the string of arguments that are going to be passed to the function
                #Calculator from the import being initialized
                Calc = Calculator()
                #first set up the method call as a string to format in the string of arguments
                command = "Calc.statusProcs({})".format(ob[1])
                #Get the return of the method
                message = eval(command)
                self.comment(comment, message)

            elif re.search("rareItem\((.*)\)", comment.body, re.I|re.M):
                #Ob is the entire snippet
                ob = re.search("rareItem\((.*)\)", comment.body, re.I|re.M)
                #Ob[1] is the string of arguments that are going to be passed to the function
                #Calculator from the import being initialized
                Calc = Calculator()
                #first set up the method call as a string to format in the string of arguments
                command = "Calc.rareChance({})".format(ob[1])
                #Get the return of the method
                message = eval(command)
                self.comment(comment, message)
        except:
            #If something went wrong (most probably in the calcuations) write an apology
            message = "I'm sorry, I don't understand what you mean.\nYou might have mistyped or filled in the values in a problematic way\nMy commands are:\n\n -critchance([critchance of your weapon], [number of bullets per shot], [multishot chance]\n\n -statusprocs([unmodded statuschance], [how many % +stauts chance the weapon has (i.e. 240 for 4 dualstat mods)], [number of bullets per shot], [multishot chance])\n\n -rareitem([number of radiant relics the squad intends to use], [number of flawless relics], [exceptinal relics], [intact relics]\n\n If you are certain you inputed everything correctly contact /u/Aereskiko or visit my GitHub Page"

    def comment(self, comment, response):
        #In a while loop in case it has to wait for more comment quota
        while True:

            try:
                #Adding the signature of the bot to the response gotten from the math portion
                true_response = response + "\n\n==========\n\nI'm a very small bot. If you wish to see the source code, give suggestions or help you can do so [here](https://github.com/Areskiko/AresBot)"
                comment.reply(true_response)
                #Add the comment ID to the list, but also writing it down to the file
                self.comments_responded.append(comment.id)
                with open(self.fil, "a") as f:
                    f.write(comment.id + "\n")

                break

            except praw.exceptions.APIException:
                #If exception due to quota wait for a minute and try again
                print("Waiting")
                time.sleep(60)
            except Exception as e:
                print(str(e))
                with open("error_messages.txt", "r") as f:
                    f.append(str(e))



Ares = Bot("Warframe")
Ares.begin()