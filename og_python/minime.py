import random
from deal_damage import DefenderDeck
from my_deck import AttackerDeck
import time

start_time = time.time()

counts = {}
baselevel = 3
baseclock = 0
configuration = [30, 25, 20]
cxconfiguration = [8, 6]
for simu2 in range(len(cxconfiguration)):
    for simu in range(len(configuration)):
        attempts = 10000000
        counts = {}
        for i in range(attempts):
            ws = DefenderDeck(deck=configuration[simu], cx=cxconfiguration[simu2], wr=0, wrcx=0, level=baselevel, clock=baseclock)
            #ws = DefenderDeck(deck=10, cx=3, wr=16, wrcx=4, level=baselevel, clock=baseclock) cinderella
            #tr = AttackerDeck(deck = 25, trigger = 19) shork
            tr = AttackerDeck(deck = 20, trigger = 6)
            #special week uma musume 
            for k in range(3):
                millcount = 3
                fromdeck = False
                if millcount >= ws.deck:
                    millcount = ws.deck
                    fromdeck = True
                hit = ws.mill(millcount)
                if hit == 1 or hit == 2:
                    ws.sticks(soul=1,cx=1)
                    ws.sticks(soul=1,cx=0)
                if hit == 0:
                    ws.sticks(soul=1,cx=0)
                if hit == 3:
                    ws.sticks(soul=1,cx=1)
                if fromdeck == True and hit > 0:
                    ws.deck -= 1
                    ws.cx -= 1
                if fromdeck == True and hit < 3:
                    ws.deck -= 1
                if fromdeck == False and hit > 0:
                    ws.wr -= 1
                    ws.wrcx -= 1
                if fromdeck == False and hit < 3:
                    ws.wr -= 1        
                ws.damagecheck(tr.triggerdamage())     
            ws.mill(1)
            combo = (ws.level, ws.clock)
            # check if the combination already exists in the dictionary
            if combo in counts:
                counts[combo] += 1
            else:
                counts[combo] = 1
            #print (f'deck {ws.deck}, cx {ws.cx}, damage {ws.level}/{ws.clock}, waiting room {ws.wr}/{ws.wrcx}')

        #print
        aggregate_count = attempts
        print(f'{configuration[simu]}/{cxconfiguration[simu2]}')
        for combo, count in sorted(counts.items(), key=lambda x: (x[0][0], x[0][1])):
            
            percentage = aggregate_count / attempts * 100
            aggregate_count -= count
            if combo[0] < 5: #and combo[1] > 0) or (combo[0] == 4 and combo[1] == 0): # restrict damages printed
                print(f"{combo}: {percentage:.2f}% and [{count}]x")
 
        end_time = time.time()

        print(f"Execution time: {int((end_time - start_time)/60)}m {int((end_time - start_time)%60)}s \n")
