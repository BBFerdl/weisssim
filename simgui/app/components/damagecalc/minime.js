import DefenderDeck from './deal_damage.js';
import AttackerDeck from './my_deck.js';

let counts = {};
const baselevel = 3;
const baseclock = 0;
const configuration = [30, 25, 20];
const cxconfiguration = [8, 6];

const start_time = Date.now();
for (let simu2 = 0; simu2 < cxconfiguration.length; simu2++) {
  for (let simu = 0; simu < configuration.length; simu++) {
    const attempts = 10000;
    counts = {};
    for (let i = 0; i < attempts; i++) {
      const ws = new DefenderDeck({
        deck: configuration[simu],
        cx: cxconfiguration[simu2],
        wr: 0,
        wrcx: 0,
        level: baselevel,
        clock: 0
      });
      const tr = new AttackerDeck({
        deck: 20,
        trigger: 6,
      });
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
  
      const combo = `${ws.level},${ws.clock}`;
      if (combo in counts) {
        counts[combo] += 1;
      } else {
        counts[combo] = 1;
      }
    }
    let aggregate_count = attempts;
    console.log(`${configuration[simu]}/${cxconfiguration[simu2]}`);
    let arr = [];
    for (const combo in counts) {
      arr.push(combo);
    }
    arr.sort();
    for(const combo of arr){
      const count = counts[combo];
      const percentage = (aggregate_count / attempts) * 100;
      aggregate_count -= count;
      const [level, clock] = combo.split(',');
      if (level < 5) {
        console.log(`${level}/${clock}:${percentage.toFixed(2)}% and [${count}]x`);
      }
    }
    const end_time = Date.now();
    console.log(`Execution time: ${Math.floor((end_time - start_time) / 60000)}m ${Math.floor((end_time - start_time) / 1000) % 60}s \n`);
  }
}