import requests
import re

def getSource(item):
    url = "http://warframe.wikia.com/wiki/" + str(item)
    r = requests.get(url)
    return (r.content)

def findCrit(page):
    page = str(page)
    page = page.replace(r"\t", "")
    page = page.replace(r"\n", "")
    critchanceAreaMatch ='<a href="/wiki/Critical_Hit#Critical_Hit_Chance" title="Critical Hit">Crit Chance</a></h3><div class="pi-data-value pi-font">\d*%</div></div><div class="pi-item pi-data pi-item-spacing pi-border-color"><h3 class="pi-data-label pi-secondary-font"><a href="/wiki/Critical_Hit#Critical_Damage_Multiplier"'
    ChanceAreaSearch = re.search(critchanceAreaMatch, page)
    chanceArea = ChanceAreaSearch.group(0)

    ChanceSearch = re.search("(\d*)%", chanceArea)
    chance = ChanceSearch.group(1)


    CritMultiplierAreaMatch = '<a href="/wiki/Critical_Hit#Critical_Damage_Multiplier" title="Critical Hit">Crit Multiplier</a></h3><div class="pi-data-value pi-font">2.0x</div></div><div class="pi-item pi-data pi-item-spacing pi-border-color"><h3 class="pi-data-label pi-secondary-font"><a href="/wiki/Status_Chance"'
    MultiplierAreaSearch = re.search(CritMultiplierAreaMatch, page)
    MultiplierArea = MultiplierAreaSearch.group(0)

    MultiplierSearch = re.search("(\d*)\.(\d*)x", MultiplierArea)

    multiplier = float(str(MultiplierSearch.group(1)) + "." + str(MultiplierSearch.group(2)))

    return chance, multiplier

print(findCrit(getSource("Hek")))
