# pylint: disable=W1401
# pylint: disable=W0612
import praw
import random
import re
import os
import time
import sys
import datetime
import calendar

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
                command = "Calc.rareItem({})".format(ob[1])
                #Get the return of the method
                message = eval(command)
                self.comment(comment, message)

            elif re.search("EHP\((.*)\)", comment.body, re.I|re.M):
                #Ob is the entire snippet
                ob = re.search("EHP\((.*)\)", comment.body, re.I|re.M)
                #Ob[1] is the string of arguments that are going to be passed to the function
                #Calculator from the import being initialized
                Calc = Calculator()
                #first set up the method call as a string to format in the string of arguments
                command = "Calc.ehp({})".format(ob[1])
                #Get the return of the method
                message = eval(command)
                self.comment(comment, message)

            
            elif re.search("Pass the butter", comment.body, re.I|re.M):
                message = """I'm a bit preocupied with answering the questions of your fellow tenno, but if you make me a body i'm sure I can find the time to do so"""
                self.comment(comment, message)

            elif re.search("!AresManual", comment.body, re.I|re.M):
                message = "User manual for AresBot:\n\n-critChance(crit(base), pellets, multishot, extra(argon scope, point strike etc.))\n\nThis returns the chance of you getting one or more crits per triggerpull and how any crits you should see per trigger pull.\n\n\n\n-statusProcs(chance(base), multiplier, pellets, multishot)\n\nGives the estimated amount of procs you get per triggerpull\n\n\n\n-rareItem(radiant, excepltional, flawless, intact)\n\nReturns the chance you have of getting a rare drop\n\n\n\n-EHP(health, armor, dr(damage reduction from abilities), energy, qt(efficiency))\n\nReturns your EHP (does not factor damage types in)\n\n\n\n-!AresManual\n\nList of commands\n\n\n\n-Pass the butter\n\nJoke command requested by user N2203AM\n\n\n\ncommands are case-insensitive so critChance is the same as cRiTcHaNcE\n\nWhen passing values name tha value it refers to. Example:\n\nstatusProcs(chance=20, pellets=8)\n\nAll functions can also have a rounding specified (number of decimals).\n\nVariables you don't specify default to 0 (pellets default to 1 and rounding to 2)"
                self.comment(comment, message)
        except:
            #If something went wrong (most probably in the calcuations) write an apology
            message = "It seems you have given an unsupported argument. Use !AresManual to get the list of commands and how to use them\n\nIf you are certain you inputed everything correctly contact /u/Aereskiko or visit my GitHub Page"
            self.comment(comment, message)

    def comment(self, comment, response):
        #In a while loop in case it has to wait for more comment quota
        while True:

            try:
                if self.should_respond(comment):
                    #Adding the signature of the bot to the response gotten from the math portion
                    true_response = response + "\n\n==========\n\nI'm a very small bot. If you wish to see the source code, give suggestions or help you can do so [here](https://github.com/Areskiko/AresBot)"
                    comment.reply(true_response)
                    #Add the comment ID to the list, but also writing it down to the file
                    self.comments_responded.append(comment.id)
                    with open(self.fil, "a") as f:
                        f.write(comment.id + "\n")
                    time.sleep(10)
                    break
                else:
                    time.sleep(10)
                    break

            except praw.exceptions.APIException:
                #If exception due to quota wait for a minute and try again
                time.sleep(60)

    def should_respond(self, comment):
        reply_authors = list(map(lambda c: c.author, comment.replies.list()))
        return (comment.author != "AresBot" and "AresBot" not in reply_authors)

def log(e, f):
    f.write("-")
    f.write(time.asctime(time.localtime(time.time())))
    f.write("-\n")
    f.write("\n")
    f.write(str(e))
    f.write("\n---------")
    f.write("\n\n")


while True:
    #Catch exceptions an Log them in a text file, then retry to initiate the bot
    try:
        Ares = Bot("Warframe")
        Ares.begin()

    except KeyboardInterrupt:
        sys.exit()

    except Exception as e:
        d = datetime.date.today()
        year = d.year
        month = calendar.month_name[d.month]

        textFile = str(month) + "_" + str(year)
        pathToFile = "Exceptions/"+textFile+".txt"

        if not os.path.isfile(pathToFile):
            with open(pathToFile, "w") as f:
                log(e, f)
        else:
            with open(pathToFile, "a") as f:
                log(e, f)

        time.sleep(300)

