// itsuki set 2
for (let j = 0; j < 3; j++) {
    ws.damagecheck(1);
    ws.damagecheck(4);
    ws.damagecheck(tr.triggerdamage());
  }
  ws.mill(1);
  
  // origami and aki (and niji kanata)
  for (let j = 0; j < 3; j++) {
    ws.check({ amount: 1, keepcx: 1 });
    ws.check({ amount: 1, keepcx: 1 });
    ws.check({ amount: 1, keepcx: 1 });
    const amount = ws.mill(4);
    for (let i = 0; i < amount; i++) {
      ws.damagecheck(1);
    }
    ws.damagecheck(tr.triggerdamage());
  }
  ws.mill(1);
  
  // hawkeye double captain
  for (let j = 0; j < 2; j++) {
    ws.damagecheck(1);
    ws.damagecheck(tr.triggerdamage());
  }
  let currentsoul = 3;
  for (let j = 0; j < 2; j++) {
    currentsoul = tr.triggerdamage(currentsoul);
    ws.damagecheck(1);
    ws.damagecheck(1);
    ws.damagecheck(currentsoul);
  }
  ws.mill(1);
  
  // shork
  for (let j = 0; j < 3; j++) {
    ws.damagecheck(2);
    ws.damagecheck(tr.triggerdamage(0));
    ws.damagecheck(tr.triggerdamage(0));
    ws.damagecheck(tr.triggerdamage(3));
  }
  ws.mill(1);
  
  // cinderella at 2/2
  for (let j = 0; j < 3; j++) {
    ws.mill(24);
    ws.damagecheck(tr.triggerdamage());
  }
  ws.mill(1);
  
  // special week uma musume, only works with 25+ cards
  for (let j = 0; j < 3; j++) {
    const temp = ws.mill(3);
    if (temp === 1 || temp === 2) {
      ws.sticks(1, 1);
      ws.sticks(1, 0);
    }
    if (temp === 0) {
      ws.sticks(1, 0);
    }
    if (temp === 3) {
      ws.sticks(1, 1);
    }
    ws.damagecheck(tr.triggerdamage());
  }
  ws.mill(1);