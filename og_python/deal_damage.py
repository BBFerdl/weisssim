import random

class DefenderDeck:
    def __init__(self, clock=0, clockcx=0, level=3, deck=20, cx=8, wr=0, wrcx=0, solutiondeck=0, solutiondeckcx=0):
        self.clock = clock
        self.clockcx = clockcx
        self.level = level
        self.deck = deck
        self.cx = cx
        self.wr = wr
        self.wrcx = wrcx
        self.solutiondeck = solutiondeck
        self.solutiondeckcx = solutiondeckcx
        
    def mill(self, amount):
        countcx = 0
        for i in range(amount):
            if self.solutiondeck == 0:
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
            else:
                self.solutiondeck -= 1
                self.wr += 1
                if self.solutiondeckcx > 0:
                    self.solutiondeckcx -= 1
                    self.cx -= 1
                    self.wrcx += 1
                    countcx +=1
        return countcx
    
    def mill_specific(self, amount, millcx):
        for i in range(amount):
            if self.deck == 0:
                self.refresh()
            self.deck -= 1
            if millcx:
                self.cx -= 1
                self.wr += 1 
                self.wrcx += 1
            else:
                self.wr += 1
    
    def check(self, amount, keepcx=0):
            amount -= self.solutiondeck
            for i in range(amount):
                if self.deck > 0:
                    rnumber = random.uniform(0, 1)
                    rtracker = self.cx/self.deck 
                    if keepcx == 1:
                        if rtracker > rnumber: #is cx
                            self.deck -= 1
                            self.cx -= 1
                            self.solutiondeck += 1
                            self.solutiondeckcx += 1
                        else:
                            self.mill_specific(amount = 1, millcx = 0)
                    else:
                        if rtracker > rnumber: #is char
                            self.mill_specific(amount = 1, millcx = 1)
                        else:
                            self.deck -= 1
                            self.solutiondeck += 1
        
    def topkek(self, amount, wrreliant):
        for i in range(amount):
            if wrreliant:
                if self.wr > self.wrcx:
                    self.solutiondeck += 1
                    self.wr -= 1
            else:
                self.solutiondeck += 1
                
    def shuffleback(self, amount, wrreliant):
        if wrreliant:
            if self.wr - self.wrcx < amount:
                amount = self.wr - self.wrcx
        self.deck += amount                
            
    def damagecheck(self, soul):
        for i in range(soul):
            if self.solutiondeck == 0:
                if self.deck == 0:
                    self.refresh()
                rnumber = random.uniform(0, 1)
                rtracker = self.cx/self.deck
                self.deck -= 1
                if rtracker > rnumber:
                    self.cx -= 1
                    self.wr += i + 1
                    self.wrcx += 1 
                    break
                else:
                    if i == soul - 1:
                        self.sticks(soul,0)
                        return True
            else:
                self.solutiondeck -= 1
                if self.solutiondeckcx > 0:
                    self.solutiondeckcx -= 1
                    self.cx -= 1
                    self.wr += i + 1
                    self.wrcx += 1 
                    break
                else:
                    if i == soul - 1:
                        self.sticks(soul,0)
                        return True
                    
                    
        
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
            
