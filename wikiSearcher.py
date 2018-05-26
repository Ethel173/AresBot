import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

import re
import os
from bs4 import BeautifulSoup

class crawler():
    def __init__(self, wiki="https://www.wikipedia.org/wiki/"):
        self.wiki = wiki
    def search(self, term):
        term = term.replace(" ", "_")
        page = requests.get(self.wiki + term)
        soup = BeautifulSoup(page.content, "html.parser")

        everything = (soup.get_text())
        if self.wiki == "https://www.wikipedia.org/wiki/":
            start = everything.find("From Wikipedia")
            stop = start+750
            removeNewline = re.sub(r'\n\s*\n', '\n\n', everything)
            Nrelevant = removeNewline[start:stop]
            searchPlace = Nrelevant.find("search")
            lastRelevant = Nrelevant[(searchPlace+6):]
            result = lastRelevant + "\n...\nTo see the continuation go to {}".format(self.wiki + term)
        elif re.search("(.*).wikia.com/wiki/", self.wiki):
            result = "I'm sorry but I can't extract information from fandom wikies as the information is not stored on the html file\n\nHowever you can visit the page [here]({})".format(self.wiki + term)
        return result


    

if __name__=="__main__":
    myC = crawler()
    result = myC.search("python")
    print(result)