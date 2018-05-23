ares_quotes= \
[
"I don't know what to say to that",
"How could i posibly help with that?",
"I think you expect to much of me",
"I'll do it later",
"Just give me five more minutes!"
"I don't want to"
"Have you tried lemonade? Lemonade always works"
"I'll have you know that i won't stupe down to such low levels"
"Figure it out yourself"
"Go ask marvin"
"No",
"I don't want to"
]

import praw
import random
import re
import os
import time
import sys
reddit = praw.Reddit('Ares')
subreddit = reddit.subreddit("pythonforengineers")

    

if not os.path.isfile("responded.txt"):
    comments_responded = []
else:
    with open("responded.txt", "r") as f:
        comments_responded = f.read()
        comments_responded = comments_responded.split("\n")
        comments_responded = list(filter(None, comments_responded))

for comment in subreddit.stream.comments():
    if comment.id not in comments_responded:
        if re.search("Ares", comment.body, re.IGNORECASE):
            ares_reply = random.choice(ares_quotes)
            while True:
                try:
                    comment.reply(ares_reply)
                    comments_responded.append(comment.id)
                    with open("responded.txt", "w") as f:
                        f.write(comment.id + "\n")
                    break
                except praw.exceptions.APIException:
                    time.sleep(600)

