# pylint: disable=W1401
# pylint: disable=W0612
# pylint: disable=E0401
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
from Brain import MathBot

os.chdir(".")
                                                                                                                                              

while True:
    mBot = MathBot()
    text = input(":")
    result = mBot.start(text)
    print(result)