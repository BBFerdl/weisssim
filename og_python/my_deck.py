import random

class AttackerDeck:
    def __init__(self, clock=0, clockcx=0, level=3, deck=20, cx=7, wr=0, wrcx=0, trigger=6):
        self.clock = clock
        self.clockcx = clockcx
        self.level = level
        self.deck = deck
        self.cx = cx
        self.wr = wr
        self.wrcx = wrcx
        self.trigger = trigger #(13*(deck20+wr0))/43=6 #quick hack before we can declare custom trigger amounts
        
    def mill(self, amount):
        countcx = 0
        for i in range(amount):
            if self.deck == 0:
                self.refresh()
            rnumber = random.uniform(0, 1)
            rtracker = self.cx/self.deck
            self.deck -= 1
            if rtracker > rnumber:
                self.cx -= 1
                self.wr += 1 
                self.wrcx += 1
                countcx += 1
            else:
                self.wr += 1
        return countcx
    
    def triggerdamage(self, triggers=1, soul=3):
        for i in range(triggers):
            if self.deck == 0:
                self.refresh()
            rnumber = random.uniform(0, 1)
            rtracker = self.trigger/self.deck
            self.deck -= 1
            if rtracker > rnumber:
                self.trigger -= 1
                soul += 1
        return soul
                    
    def sticks(self, soul, cx):
        self.clock += soul
        self.clockcx += cx
        if self.clock > 6:
            self.clock = self.clock%7
            self.wr += 6
            self.level += 1
            self.wrcx += self.clockcx
            self.clockcx = 0

    def refresh(self):
        self.deck += self.wr
        self.wr = 0
        self.cx = self.wrcx
        self.wrcx = 0
        self.refreshpenalty()

    def refreshpenalty(self):
        rnumber = random.uniform(0, 1)
        rtracker = self.cx/self.deck
        self.deck -= 1
        if rnumber >= rtracker:
            self.sticks(1,1)
        else:
            self.cx -= 1
            self.sticks(1,0)
            
