# pylint: disable=W1401
# pylint: disable=W0612
# pylint: disable=E0401
import calendar
import datetime
import os
import random
import re
import sys
import time
import discord



#Custom math module
sys.path.append("../deps/")
from MathFrame import Calculator
os.chdir(".")
                                                                                                                                              
class MathBot():
    def __init__(self):
        pass

    def begin(self, comment):
        comment = comment
        if re.match("", comment, re.IGNORECASE):
            result = self.descide(comment)
            return result
        else:
            return "No command found"

    def descide(self, comment):
        try:
            message=""
            commentText = comment
            foundCommand = False

            #Formatting the comment to use correct casing
            insensitive_crit = re.compile(re.escape('critChance'), re.IGNORECASE)
            commentText = insensitive_crit.sub('critChance', commentText)

            insensitive_status = re.compile(re.escape('statusProcs'), re.IGNORECASE)
            commentText = insensitive_status.sub('statusProcs', commentText)
            
            insensitive_item = re.compile(re.escape('rareItem'), re.IGNORECASE)
            commentText = insensitive_item.sub('rareItem', commentText)
            
            insensitive_ehp = re.compile(re.escape('ehp'), re.IGNORECASE)
            commentText = insensitive_ehp.sub('ehp', commentText)
            
            insensitive_manual = re.compile(re.escape('AresManual'), re.IGNORECASE)
            commentText = insensitive_manual.sub('AresManual', commentText)
            
            insensitive_commands = re.compile(re.escape('AresCommands'), re.IGNORECASE)
            commentText = insensitive_commands.sub('AresCommands', commentText)

            for i in range(5):
                #Searhing every comment for the call-functions
                if re.search("critChance\((.*?)\)", commentText, re.I|re.M):
                    
                    #Ob is the entire snippet
                    ob = re.search("critChance\((.*?)\)", commentText, re.I|re.M)
                    #Ob[1] is the string of arguments that are going to be passed to the function
                    #Calculator from the import being initialized
                    Calc = Calculator()
                    #first set up the method call as a string to format in the string of arguments
                    func = "critChance({})".format(ob[1])
                    command = "Calc."+func
                    #Get the return of the method
                    try:    
                        message = " \n\n" + str(ob[0]) + ":\n\n" + eval(command) + message + " \n\n"
                        commentText = commentText.replace(func, "")
                        foundCommand = True
                    except Exception:
                        message = " \n\n" + str(ob[0]) + ":\n\n" + "\n\nIt seems you have given some inputs that are not accepted. Please reffer to the manual" + message + " \n\n"
                        foundCommand = True
                        commentText = commentText.replace(func, "")

                #Searhing every comment for the call-functions
                elif re.search("statusProcs\((.*?)\)", commentText, re.I|re.M):
                    
                    #Ob is the entire snippet
                    ob = re.search("statusProcs\((.*?)\)", commentText, re.I|re.M)
                    #Ob[1] is the string of arguments that are going to be passed to the function
                    #Calculator from the import being initialized
                    Calc = Calculator()
                    #first set up the method call as a string to format in the string of arguments
                    func = "statusProcs({})".format(ob[1])
                    command = "Calc."+func
                    #Get the return of the method
                    try:    
                        message = " \n\n" + str(ob[0]) + ":\n\n" + eval(command) + message + " \n\n"
                        commentText = commentText.replace(func, "")
                        foundCommand = True
                    except Exception:
                        message = " \n\n" + str(ob[0]) + ":\n\n" + "\n\nIt seems you have given some inputs that are not accepted. Please reffer to the manual" + message + " \n\n"
                        foundCommand = True
                        commentText = commentText.replace(func, "")



                elif re.search("rareItem\((.*?)\)", commentText, re.I|re.M):
                    
                    #Ob is the entire snippet
                    ob = re.search("rareItem\((.*?)\)", commentText, re.I|re.M)
                    #Ob[1] is the string of arguments that are going to be passed to the function
                    #Calculator from the import being initialized
                    Calc = Calculator()
                    #first set up the method call as a string to format in the string of arguments
                    func = "rareItem({})".format(ob[1])
                    command = "Calc."+func
                    #Get the return of the method
                    try:    
                        message = " \n\n" + str(ob[0]) + ":\n\n" + eval(command) + message + " \n\n"
                        commentText = commentText.replace(func, "")
                        foundCommand = True
                    except Exception:
                        message = " \n\n" + str(ob[0]) + ":\n\n" + "\n\nIt seems you have given some inputs that are not accepted. Please reffer to the manual" + message + " \n\n"
                        foundCommand = True
                        commentText = commentText.replace(func, "")


                elif re.search("ehp\((.*?)\)", commentText, re.I|re.M):
                    
                    #Ob is the entire snippet
                    ob = re.search("ehp\((.*?)\)", commentText, re.I|re.M)
                    #Ob[1] is the string of arguments that are going to be passed to the function
                    #Calculator from the import being initialized
                    Calc = Calculator()
                    #first set up the method call as a string to format in the string of arguments
                    func = "ehp({})".format(ob[1])
                    command = "Calc."+func
                    #Get the return of the method
                    try:    
                        message = " \n\n" + str(ob[0]) + ":\n\n" + eval(command) + message + " \n\n"
                        commentText = commentText.replace(func, "")
                        foundCommand = True
                    except Exception:
                        message = " \n\n" + str(ob[0]) + ":\n\n" + "\n\nIt seems you have given some inputs that are not accepted. Please reffer to the manual" + message + " \n\n"
                        foundCommand = True
                        commentText = commentText.replace(func, "")


                elif re.search("AresCommands", commentText, re.I|re.M):
                    message = "Commands:\n\ncritChance(weapon, crit, pelets, multishot, mods)\n\nsatusProcs(weapon, chance, mods, pellets, multishot)\n\nrareItem(radiant, flawless, exceptional, intact)\n\nehp(armor, health, dr, qt, energy)\n\nAresManual\n\nAresCommands\n\n" + message
                    commentText = commentText.replace("AresCommands", "")
                    foundCommand = True

                elif re.search("AresManual", commentText, re.I|re.M):
                    message = "User manual for AresBot:\n\n-critChance(weapon, crit(base), pellets, multishot, mods(argon scope(135), point strike(150) etc.))\n\nThis returns the chance of you getting one or more crits per triggerpull and how any crits you should see per trigger pull.\n\n\n\n-statusProcs(weapon, chance(base), mods, pellets, multishot)\n\nGives the estimated amount of procs you get per triggerpull\n\n\n\n-rareItem(radiant, excepltional, flawless, intact)\n\nReturns the chance you have of getting a rare drop\n\n\n\n-EHP(health, armor, dr(damage reduction from abilities), energy, qt(efficiency))\n\nReturns your EHP (does not factor damage types in)\n\n\n\n-AresManual\n\nExtensive manual for AresBot\n\n\n\n-AresCommands\n\nList of commands\n\n\n\nCommands are case-insensitive so critChance is the same as cRiTcHaNcE.\n\nWhen passing values name tha value it refers to. Example:\n\nstatusProcs(chance=20, pellets=8)\n\nWhen passing a weapon name encase the name in quotations (double or single, but has to be the same on both sides). Weapon-stats are pulled from the wikia and are therefore dependent on it being up to date\n\nAll functions can also have a rounding specified (number of decimals).\n\nAll values should be numeric except for the weapon which should be the name of the weapon encased in quotes. Names must be spelled correctly and capitalized coorectly ('Tigris Prime' instead of 'tigris prime')\n\nVariables you don't specify default to 0 (pellets default to 1 and rounding to 2)" + message + "\n\n"
                    commentText = commentText.replace("AresManual", "")
                    foundCommand = True

                else:
                    if foundCommand:
                        break
                    else:
                        pass
            if foundCommand:
                return message
            else:
                pass
            

        except Exception:
            #If something went wrong (most probably in the calcuations) write an apology
            message = "It seems you have given an unsupported argument. Use AresManual to get the list of commands and how to use them\n\nIf you are certain you inputed everything correctly contact /u/Aereskiko or visit my GitHub Page"
            return message

mBot = MathBot()

tokenFile = "token.txt"
with open(tokenFile, mode="r") as f:
    TOKEN = f.read()

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        text = message.content
        text = mBot.begin(text[1:])
        await client.send_message(message.channel, content = text)

client.run(TOKEN)