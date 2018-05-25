import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

import re
import os
from bs4 import BeautifulSoup

class crawler():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_driver = "C:\\WorkFolder\\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

    def search(self, term):
        self.driver.get("https://www.wikipedia.org/")
        self.driver.maximize_window()

        bar = self.driver.find_element_by_id("searchInput")
        bar.clear()
        bar.send_keys(term + "\n")

        page = requests.get(self.driver.current_url)
        soup = BeautifulSoup(page.content, "html.parser")

        everything = (soup.get_text())
        start = everything.find("From Wikipedia")
        stop = start+750
        removeNewline = re.sub(r'\n\s*\n', '\n\n', everything)
        Nrelevant = removeNewline[start:stop]
        result = Nrelevant + "\n...\nTo see the continuation go to {}".format(self.driver.current_url)

        return result


    

if __name__=="__main__":
    myC = crawler()
    result = myC.search("python")
    print(result)