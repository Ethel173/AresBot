# pylint: disable=W1401
# pylint: disable=W0612
# pylint: disable=E0401
import praw
import random
import re
import os
import time
import sys
import datetime
import calendar

#Custom math module
sys.path.append("../deps/")
from MathFrame import Calculator
from Brain import MathBot as mBot

os.chdir(".")

class RedditBot():
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
                if re.match("", comment.body, re.IGNORECASE):
                    result = mBot().start(comment.body)
                    if result == None:
                        pass
                    else:
                        self.comment(comment, result)

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
        Ares = RedditBot("Warframe")
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

