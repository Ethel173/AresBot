# AresBot

The Bot can be accessed on https://www.reddit.com/r/Warframe/, as a standalone command-line application or you can easily get it as a discord bot.

If you want to run any version from source you'll need to have the folder specific to what type you need AND the deps folder. Both of these folders ought to be in the same parent folder. Ane .exe file does not need the deps folder or anything else. If you want to compile the source code into a .exe yourself you can do so with PyInstaller and the .spec file that comes in the folder.

If you want to make use of the discord bot you will also need to add a text file in the discord discord directory called TOKEN.txt this file must only contain the token that discord gives you upon creating a new bot.

The available commands for the bot are as follows:



  critChance(weapon, crit, pellets, multishot, mods, rounding)
Returns the chance of you getting a critical hit and the average critical hits per trigger event.

Use: All values are optional. weapon defaults to none. crit, multishot and mods default to 0, pellets default to 1 and rounding defaults to 2. the inclusion of a weapon will overwrite crit and pellets, the weapon name must be encased by single or double quotes. Crit reffers to the base critchance of the weapon, pellets reffers to the base ammount of pellets, multishot reffers to the multishot status and mods reffers to critchance mods. All percentages are to be given without "0." so in essence pointstrike would be mods=150. If you have multiple mods you can either sum them up, so PS and ArgonScope would be mods=285 or you could supply them with a + in between so mods=150+135.



  statusProcs(weapon, status, pellets, multishot, mods, rounding)
Returns the chance of you getting a status proc and the average amount of procs per trigger event.

Use: All values are optional. weapon defaults to none. status, multishot and mods default to 0, pellets default to 1 and rounding defaults to 2. the inclusion of a weapon will overwrite status and pellets, the weapon name must be encased by single or double quotes. status reffers to the base statuschance of the weapon, pellets reffers to the base ammount of pellets, multishot reffers to the multishot status and mods reffers to critchance mods. All percentages are to be given without "0." so in essence a dualstat mods would be mods=60. If you have multiple mods you can either sum them up, so two dual stat mods would be mods=120 or you could supply them with a + in between so mods=60+60.



  rareItem(radiant, flawless, exceptional, intact, rounding)
Returns the chance you have for getting a rare after running a set amount of relics

Use: All values are optional and all values except for rounding defaults to 0, while rounding defaults to 2. You simply supply the amount of relics you want to run of each type.

  ehp(health, armor, shields, dr, rounding, energy, qt)
Returns your ehp

Use: all values are optional. All values except for rounding default to 0, while rounding defaults to 2. health, armor and shields are the values listed in the arsenal. dr reffers to damage resistance (wether it is from ability or specter), energy is your energy level and is used in conjunction with quick thinking, qt is the efficency of quick thinking so a maxed quick thinking would give qt=240




On top of this you can use Aresmanual for a extensive manual (although this one is better) while Arescommands just gives you a quick list of commands. 

All commands are case-insensitive. The stats provided when specifyng a weapon are pulled from wikia.warframe.com


