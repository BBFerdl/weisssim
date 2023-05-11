''' 
    #itsuki set 2
    for j in range(3):
        ws.damagecheck(1)
        ws.damagecheck(4)
        ws.damagecheck(tr.triggerdamage())
    ws.mill(1)
    #origami and aki (and niji kanata)
    for j in range(3):
        ws.check(amount = 1, keepcx = 1)
        ws.check(amount = 1, keepcx = 1)
        ws.check(amount = 1, keepcx = 1)
        amount = ws.mill(4)
        for i in range(amount):
            ws.damagecheck(1)
        ws.damagecheck(tr.triggerdamage())
    ws.mill(1)
    #hawkeye double captain
    for j in range(2):
        ws.damagecheck(1)
        ws.damagecheck(tr.triggerdamage())
    currentsoul = 3
    for j in range(2):
        currentsoul = tr.triggerdamage(currentsoul)
        ws.damagecheck(1)
        ws.damagecheck(1)
        ws.damagecheck(currentsoul)
    ws.mill(1)'''
    
    '''#shork
    for j in range(3):
        ws.damagecheck(2)
        ws.damagecheck(tr.triggerdamage(0))
        ws.damagecheck(tr.triggerdamage(0))
        ws.damagecheck(tr.triggerdamage(3))
    ws.mill(1)'''
    ''' #cinderella at 2/2
    
    for j in range(3):
        ws.mill(24)
        ws.damagecheck(tr.triggerdamage())
    ws.mill(1)            '''
    '''
    #special week uma musume, only works with 25+ cards
    for j in range(3):
        temp = ws.mill(3)
        if temp == 1 or temp == 2:
            ws.sticks(soul=1,cx=1)
            ws.sticks(soul=1,cx=0)
        if temp == 0:
            ws.sticks(soul=1,cx=0)
        if temp == 3:
            ws.sticks(soul=1,cx=1)
        ws.damagecheck(tr.triggerdamage())
    ws.mill(1)''' 
