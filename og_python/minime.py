import random
from deal_damage import DefenderDeck
from my_deck import AttackerDeck
import time

start_time = time.time()
counts = {}
baselevel = 3
baseclock = 0
configuration = [20,25,30]
cxconfiguration = [6,8]
for simu2 in range(len(cxconfiguration)):
    for simu in range(len(configuration)):
        attempts = 10000
        counts = {}
        for i in range(attempts):
            ws = DefenderDeck(deck=configuration[simu], cx=cxconfiguration[simu2], wr=0, wrcx=0, level=baselevel, clock=baseclock)
            #ws = DefenderDeck(deck=10, cx=3, wr=16, wrcx=4, level=baselevel, clock=baseclock) cinderella
            #tr = AttackerDeck(deck = 25, trigger = 19) shork
            tr = AttackerDeck(deck = 20, trigger = 6)
            for j in range(3):
                ws.damagecheck(1)
                ws.damagecheck(4)
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
