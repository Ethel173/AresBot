#I apologize for ugly math, but IDE's don't let you write propper math expressions
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

    def critChance(self, cc, pellets, multi):
        #A = crit, B = extra shot

        #Convert given stats to decimal chance
        cc = cc/100
        multi = multi/100

        #pAgB means probability of A given B
        pAgB = self.komb.Bino_over(2, 1, cc)
        #pB means probability of B
        pB = multi
        #pAnB means pobability of A given not B
        pAnB = self.komb.Bino_over(1, 1, cc)
        #pnB means probability of not B
        pnB = 1-multi
        #pA is the total probability of A
        pA = pAgB * pB + pAnB * pnB

        #Effectivey does the same calculation for every pellet
        chance = pA * pellets

        message = "You have a " + str(chance*100) + "% chance of getting one or more crits per trigger pull"
        return message

    def statusProcs(self, sc, sm, pellets, multi):
        #A = proc, B = extra shot

        #Convert given stats to decimal chance
        sc = sc/100
        sm = sm/100
        multi = multi/100

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

    def rareChance(self, radiant, flawless, exceptional, intact):
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
    

if __name__ == "__main__":
    calc = Calculator()
    string = "calc."+input(":")
    print(eval(string))
