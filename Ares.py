ares_quotes= \
[
"I don't know what to say to that",
"How could i posibly help with that?",
"I think you expect to much of me",
"I'll do it later",
"Just give me five more minutes!",
"I don't want to",
"Have you tried lemonade? Lemonade always works",
"I'll have you know that i won't stupe down to such low levels",
"Figure it out yourself",
"Go ask marvin",
"No",
"Why?",
r"¯\\_(ツ)_/¯",
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
        elif re.search("search '(.)'", comment.body, re.I):
            obj = re.search("search '(.)'", comment.body, re.I)
            myC = crawler()
            reply = myC.search(obj.group(1))
            self.comment(comment, reply)

        else:
            ares_reply = random.choice(ares_quotes)
            self.comment(comment, ares_reply)

    def comment(self, comment, response):
        while True:
            try:
                true_response = response + "\n\n--------------\n\nI'm a very small bot. If you wish to see the source, give sudgestions or help you can do so here: https://github.com/Areskiko/AresBot"
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