import random
from deal_damage import DefenderDeck
from my_deck import AttackerDeck
import time

start_time = time.time()

counts = {}
baselevel = 3
baseclock = 0
attempts = 10000000
for i in range(attempts):
    ws = DefenderDeck(level=baselevel, clock=baseclock)
    tr = AttackerDeck()
    ws.damagecheck(1)
    ws.damagecheck(4)
    ws.damagecheck(tr.triggerdamage())
    ws.damagecheck(1)
    ws.damagecheck(4)
    ws.damagecheck(tr.triggerdamage())
    ws.damagecheck(1)
    ws.damagecheck(4)
    ws.damagecheck(tr.triggerdamage())
    combo = (ws.level, ws.clock)
    # check if the combination already exists in the dictionary
    if combo in counts:
        counts[combo] += 1
    else:
        counts[combo] = 1
    #print (f'deck {ws.deck}, cx {ws.cx}, damage {ws.level}/{ws.clock}, waiting room {ws.wr}/{ws.wrcx}')

#print
aggregate_count = attempts
for combo, count in sorted(counts.items(), key=lambda x: (x[0][0], x[0][1])):
    
    print(f"Combination {combo}: {aggregate_count/attempts*100} percent")
    aggregate_count -= count

end_time = time.time()

print(f"Execution time: {end_time - start_time} seconds")
