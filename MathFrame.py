#I apologize for ugly math, but IDE's don't let you write propper math expressions
# pylint: disable=W0612
class KombinatoryCalculator(object):
    """Calculator to calculate kombinations and probability."""
    def __init__(self, result):
        """Initializes the calculator."""
        self.result = result
        
    def factorial(self, n):
        """Calculates the factorial of a given number. """
        z = 1
        x = 1
        for i in range(n):
            x = z * x
            z += 1
            i = i
        self.result = x
        return self.result

    def nCr(self, n, r):
        """Calculates the nCr."""
        nr = n-r
        self.result = (self.factorial(n)) / (self.factorial(r)*self.factorial(nr))
        return self.result

    def Bino(self, n, x, p):
        """Calculates the Binomial coefficient."""
        #Rarely used on its own but looped over in bino over
        #** means ^ in human-speak
        self.result = self.nCr(n, x) * p**(x) * (1-p)**(n-x)
        return self.result

    def Bino_over(self, n, x, p):
        """Calculates the Binomial coefficient of the given number and all above."""
        total = 0
        number = n-x
        #Loops over the normal Bino
        for i in range(number + 1):
            y = x + i
            total += self.Bino(n, y, p)
        self.result = total
        return self.result

class Calculator(object):
    def __init__(self):
        self.komb = KombinatoryCalculator(0)

    def critChance(self, crit=0, pellets=1, multishot=0):
        oCc = crit
        #A = crit, B = extra shot

        #Convert given stats to decimal chance
        cc = crit/100
        multi = multishot/100
        if cc > 1:
            extra, cc = str(cc).split(".")
            cc = "0."+cc
            cc=float(cc)

        #Splits the number into berfore and after the . so 17.6 would give 17 and 6, this is to factor in the chance of getting an extra shot
        multi = multi + 1
        bullets = str(float(pellets*multi))
        front, back = bullets.split(".")

        #Runs a binomical distribution for both the extra pellet and with only the guaranteed ones
        modPellets = int(pellets*int(front))
        #pAnB is the chance of A given not B
        pAnB = self.komb.Bino_over(modPellets, 1, cc)
        #pAgB is the chance of A given B
        pAgB = self.komb.Bino_over(modPellets+1,1,cc)
        pB = float("0."+str(back))
        #pnB is probability of not B
        pnB = (1 - float("0."+str(back)))
        #Using the formla for total chance we get the actual chance of getting one or more crits
        pA = pAgB * pB + pAnB * pnB
        
        #Ability to handle critlevels over 100% curtesy of Ethel173
        if oCc < 100:
            message = "You have a " + str(pA*100) + "% chance of getting one or more crits per trigger pull"
        else:
            message = "Seeing that your starting crit chance was over 100% you are guaranteed to get crits on everything. However You have a " + str(pA*100) + "% chance of getting one or more crits of higher type per trigger pull"
        return message

    def statusProcs(self, chance=0, multiplier=0, pellets=1, multishot=0):
        #A = proc, B = extra shot

        #Convert given stats to decimal chance
        sc = chance/100
        sm = multiplier/100
        multi = multishot/100

        #Splits the number into berfore and after the . so 17.6 would give 17 and 6, this is to factor in the chance of getting an extra shot
        multi = multi + 1
        bullets = str(float(pellets*multi))
        front, back = bullets.split(".")
        
        #caps chances over 100% as that breaks the math
        chance = sc*(1+sm)
        if chance > 1:
            chance = 1

        #cPc is status chance per pellet
        cPp = 1-(1-chance)**(1/pellets)
        #pAnB is probability of A given not B
        pAnB = int(front) * cPp
        #pAgB is probability of A given B
        pAgB = (int(front)+1) * cPp
        #pB is the probability of B
        pB = float("0."+str(back))
        #pnB is probability of not B
        pnB = (1 - float("0."+str(back)))
        #pA is the total probability of A
        pA = pAgB * pB + pAnB * pnB
        
        message = ("Due to multishot you'll either fire " + front + " pellets, or " + str(int(front)+1) + " pellets with a " + str(int(float("0."+str(back))*100)) + "% chance of getting the extra shot.\nThat means that you have an estimated " + str(int(pAnB)) + " or " + str(int(pAgB)) + " guaranteed status procs per trigger pull respectively.\nThis gives an overall " + str(pA) + " status procs per trigger pull")
        return message

    def rareChance(self, radiant=0, flawless=0, exceptional=0, intact=0):
        tot = 0.0
        #For every relic run the chance of getting one or more rares from the selection of relics
        if radiant > 0:
            tot += self.komb.Bino_over(radiant, 1, 0.1)
        if flawless > 0:
            tot += self.komb.Bino_over(flawless, 1, 0.06)
        if exceptional > 0:
            tot += self.komb.Bino_over(exceptional, 1, 0.04)
        if intact > 0:
            tot += self.komb.Bino_over(intact, 1, 0.02)
            
        message = "You have a " + str(tot*100) + "% chance of getting one or more rare drops"
        return message

    def armor(self, health=0, armor=0, dr=0):
        dr = dr/100
        armorReduction = (armor) / (armor+300)
        dr += armorReduction
        EHP = (health) / (1-dr)

        message = "Based on an armor value of " + str(armor) + " and a health value of " + str(health) + " you have an damage reduction of " + str(dr) + " and a total EHP of " + str(EHP) + ". Keep in mind that enemies might have damagetypes that increase or decrease the damage agains you. But in terms of raw EHP this should be correct"
        return message

if __name__ == "__main__":
    calc = Calculator()
    string = "calc."+input(":")
    exec(string)
