# pylint: disable=W1401
import requests
import re

def getSource(item):
    url = "http://warframe.wikia.com/wiki/" + str(item)
    r = requests.get(url)
    return (r.content)

def findCrit(page):
    #Turn the byte-like page into a string and remove tabs and lewlines
    page = str(page)
    page = page.replace(r"\t", "")
    page = page.replace(r"\n", "")

    #Check to see if the weapon has a charged mode, if so cut away the page before that point. This makes it so that we get the charged values
    ChargeSearch = re.search('<h2 class="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background">Charged Shot</h2>', page)
    if ChargeSearch:
        page = page[ChargeSearch.start():]


    #Search for the general area where the critical chance value is stored due to wikia.com (or the ones making the warframe wikia) likes to not name values
    critchanceAreaMatch ='<a href="/wiki/Critical_Hit#Critical_Hit_Chance" title="Critical Hit">Crit Chance</a></h3><div class="pi-data-value pi-font">(\d*)%</div></div><div class="pi-item pi-data pi-item-spacing pi-border-color"><h3 class="pi-data-label pi-secondary-font"><a href="/wiki/Critical_Hit#Critical_Damage_Multiplier"'
    ChanceAreaSearch = re.search(critchanceAreaMatch, page)
    chance = ChanceAreaSearch.group(1)

    '''
    Get Critical multiplier. Not sure why I made it, but might be usefull later

    CritMultiplierAreaMatch = '<a href="/wiki/Critical_Hit#Critical_Damage_Multiplier" title="Critical Hit">Crit Multiplier</a></h3><div class="pi-data-value pi-font">\d*\.\d*x</div></div><div class="pi-item pi-data pi-item-spacing pi-border-color"><h3 class="pi-data-label pi-secondary-font"><a href="/wiki/Status_Chance"'
    MultiplierAreaSearch = re.search(CritMultiplierAreaMatch, page)
    MultiplierArea = MultiplierAreaSearch.group(0)

    MultiplierSearch = re.search("(\d*)\.(\d*)x", MultiplierArea)
    multiplier = float(str(MultiplierSearch.group(1)) + "." + str(MultiplierSearch.group(2)))
    '''

    return chance

def findStatus(page):
    #Turn the byte-like page into a string and remove tabs and lewlines
    page = str(page)
    page = page.replace(r"\t", "")
    page = page.replace(r"\n", "")

    #Check to see if the weapon has a charged mode, if so cut away the page before that point. This makes it so that we get the charged values
    ChargeSearch = re.search('<h2 class="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background">Charged Shot</h2>', page)
    if ChargeSearch:
        page = page[ChargeSearch.start():]


    #Search for the general area where the critical chance value is stored due to wikia.com (or the ones making the warframe wikia) likes to not name values
    stausChanceAreaMatch ='<a href="/wiki/Status_Chance" title="Status Chance" class="mw-redirect">Status Chance</a></h3><div class="pi-data-value pi-font">(\d*)%</div>'
    ChanceAreaSearch = re.search(stausChanceAreaMatch, page)
    chance = ChanceAreaSearch.group(1)

    return chance

def findPellets(page):
    #Turn the byte-like page into a string and remove tabs and lewlines
    page = str(page)
    page = page.replace(r"\t", "")
    page = page.replace(r"\n", "")

    #Check to see if the weapon has a charged mode, if so cut away the page before that point. This makes it so that we get the charged values
    ChargeSearch = re.search('<h2 class="pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background">Charged Shot</h2>', page)
    if ChargeSearch:
        page = page[ChargeSearch.start():]


    #Search for the general area where the critical chance value is stored due to wikia.com (or the ones making the warframe wikia) likes to not name values
    pelletsAreaMatch ='<div class="pi-item pi-data pi-item-spacing pi-border-color"><h3 class="pi-data-label pi-secondary-font"><a href="/wiki/Multishot" title="Multishot">Pellets</a></h3><div class="pi-data-value pi-font">(\d*)'
    pelletsAreaSearch = re.search(pelletsAreaMatch, page)
    if pelletsAreaSearch:
        pellets = pelletsAreaSearch.group(1)
    
    else:
        pellets = 1

    return pellets


def getStats(gun, mode):
    if mode == "crit":
        cc = findCrit(getSource(gun))
        pellets = findPellets(getSource(gun))
        return cc, pellets

    elif mode == "status":
        sc = findStatus(getSource(gun))
        pellets = findPellets(getSource(gun))
        return sc, pellets

print(getStats("Tigris_Prime", "status"))