ares_quotes= \
[
"I'm sorry, I don't know what you want",
]

import praw
import random
import re
import os
import time
import sys

from wikiSearcher import crawler

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
                if re.search("Ares", comment.body, re.IGNORECASE):
                    self.descide(comment)

    def descide(self, comment):
        if not comment.body.find('/') == -1:
            start = comment.body.find('/')

            if not comment.body.find('\\') == -1:
                stop = comment.body.find('\\')

                expression = comment.body[(start+1):stop]
                response = self.math(expression)
                self.comment(comment, response)

        elif re.search("search '(.*)'", comment.body):

            obj = re.search("search '(.*)'", comment.body)
            searchAble = obj.group(1)

            if re.search("\[(.*)wikia\]", searchAble):

                wiki = re.search("\[(.*)\]", searchAble)
                wiki = wiki.group(1)
                TheWiki = "http://" + wiki + ".com/wiki/" 
                searchAble = searchAble.replace("["+wiki+"]", "")
                self.TheWiki = TheWiki
                myC = crawler(wiki=TheWiki)
            else:
                self.TheWiki = "https://www.wikipedia.org/wiki/"
                myC = crawler()
            reply = myC.search(searchAble)

            self.comment(comment, reply)

        else:
            ares_reply = random.choice(ares_quotes)
            self.comment(comment, ares_reply)

    def comment(self, comment, response):
        while True:

            try:
                if not "wikia" in self.TheWiki:
                    true_response = "I found this:\n\n" + response + "\n\n--------------\n\nI'm a very small bot. If you wish to see the source code, give sudgestions or help you can do so [here](https://github.com/Areskiko/AresBot)"
                else:
                    true_response = response + "\n\n--------------\n\nI'm a very small bot. If you wish to see the source code, give sudgestions or help you can do so [here](https://github.com/Areskiko/AresBot)"
                comment.reply(true_response)

                self.comments_responded.append(comment.id)
                with open(self.fil, "a") as f:
                    f.write(comment.id + "\n")

                break

            except praw.exceptions.APIException:
                time.sleep(60)

    def math(self, expression):
        expression = expression.replace("^", "**")
        x=eval(expression)
        return x

Ares = Bot("Warframe")
Ares.begin()