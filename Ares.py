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
reddit = praw.Reddit('Ares')
subreddit = reddit.subreddit("pythonforengineers")

fil = "responded.txt"    
if not os.path.isfile(fil):
    comments_responded = []
    with open(fil, "w") as f:
        pass
else:
    with open(fil, "r") as f:
        comments_responded = f.read()
        comments_responded = comments_responded.split("\n")
        comments_responded = list(filter(None, comments_responded))

for comment in subreddit.stream.comments():
    if comment.id not in comments_responded:
        if re.search("Ares", comment.body, re.IGNORECASE):
            if not comment.body.find('/') == -1:
                start = comment.body.find('/')
                if not comment.body.find('\\') == -1:
                    stop = comment.body.find('\\')
                    expression = comment.body[(start+1):stop]
                    expression = expression.replace("^", "**")
                    x=eval(expression)
                    while True:
                        try:
                            comment.reply(x)
                            comments_responded.append(comment.id)
                            with open(fil, "a") as f:
                                f.write(comment.id + "\n")
                            break
                        except praw.exceptions.APIException:
                            time.sleep(60)
                    

            
                
            else:
                ares_reply = random.choice(ares_quotes)
                while True:
                    try:
                        comment.reply(ares_reply)
                        comments_responded.append(comment.id)
                        with open(fil, "a") as f:
                            f.write(comment.id + "\n")
                        break
                    except praw.exceptions.APIException:
                        time.sleep(60)

