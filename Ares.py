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

from MathFrame import Calculator

class Bot():
    def __init__(self, sub):
        reddit = praw.Reddit('Ares')
        self.subreddit = reddit.subreddit(sub)

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
        for comment in self.subreddit.stream.comments():
            if comment.id not in self.comments_responded:
                if re.search("", comment.body, re.IGNORECASE):
                    self.descide(comment)

    def descide(self, comment):
        try:
            if re.search("critChance\((.*)\)", comment.body, re.I|re.M):
                ob = re.search("critChance\((.*)\)", comment.body, re.I|re.M)
                print(ob[1])
                Calc = Calculator()
                command = "Calc.critChance({})".format(ob[1])
                message = eval(command)
                self.comment(comment, message)

            elif re.search("statusProcs\((.*)\)", comment.body, re.I|re.M):
                ob = re.search("statusProcs\((.*)\)", comment.body, re.I|re.M)
                Calc = Calculator()
                command = "Calc.statusProcs({})".format(ob[1])
                message = eval(command)
                self.comment(comment, message)

            elif re.search("rareItem\((.*)\)", comment.body, re.I|re.M):
                ob = re.search("rareItem\((.*)\)", comment.body, re.I|re.M)
                Calc = Calculator()
                command = "Calc.rareChance({})".format(ob[1])
                message = eval(command)
                self.comment(comment, message)
        except:
            message = "I'm sorry, I don't understand what you mean.\nYou might have mistyped or filled in the values in a problematic way\nMy commands are:\n\n -critchance([critchance of your weapon], [number of bullets per shot], [multishot chance]\n\n -statusprocs([unmodded statuschance], [how many % +stauts chance the weapon has (i.e. 240 for 4 dualstat mods)], [number of bullets per shot], [multishot chance])\n\n -rareitem([number of radiant relics the squad intends to use], [number of flawless relics], [exceptinal relics], [intact relics]\n\n If you are certain you inputet everything correctly contact /u/Aereskiko or visit mu GitHub Page"

    def comment(self, comment, response):
        while True:

            try:
                true_response = response + "\n\n==========\n\nI'm a very small bot. If you wish to see the source code, give sudgestions or help you can do so [here](https://github.com/Areskiko/AresBot)"
                comment.reply(true_response)

                self.comments_responded.append(comment.id)
                with open(self.fil, "a") as f:
                    f.write(comment.id + "\n")

                break

            except praw.exceptions.APIException:
                time.sleep(60)


Ares = Bot("Warframe")
Ares.begin()