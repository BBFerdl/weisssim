import random

class WeissSchwarz:
    def __init__(self, clock=0, clockcx=0, level=3, deck=20, cx=8, wr=0, wrcx=0):
        self.clock = clock
        self.clockcx = clockcx
        self.level = level
        self.deck = deck
        self.cx = cx
        self.wr = wr
        self.wrcx = wrcx
        
    def mill(self, amount):
        countcx = 0
        for i in range(amount):
            if self.deck == 0:
                self.refresh()
            rnumber = random.uniform(0, 1)
            rtracker = self.cx/self.deck
            if rtracker >= rnumber:
                self.deck -= 1 
                self.cx -= 1
                self.wr += 1 
                self.wrcx += 1
                countcx += 1
            else:
                self.deck -= 1
                self.wr += 1
        return countcx
    
    def damagecheck(self, soul):
        for i in range(soul):
            if self.deck == 0:
                self.refresh()
            rnumber = random.uniform(0, 1)
            rtracker = self.cx/self.deck
            if rtracker >= rnumber:
                self.deck -= 1
                self.cx -= 1
                self.wr += i + 1
                self.wrcx += 1 
                break
            else:
                self.deck -= 1
                if i == soul - 1:
                    self.sticks(soul,0)
                    
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
            
ws = WeissSchwarz(clock=0, level=3, deck=20, cx=8, wr=0, wrcx=0, clockcx=0)

for j in range(20):
    ws.damagecheck(3)
    print (f'refresh deck {ws.deck}, cx {ws.cx}, damage {ws.level}/{ws.clock}, waiting room {ws.wr}/{ws.wrcx}')
