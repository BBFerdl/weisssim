import { DefenderDeck } from './deal_damage.js';
import { AttackerDeck } from './my_deck.js';

let counts = {};
const baselevel = 3;
const baseclock = 0;
const configuration = [30, 25, 20];
const cxconfiguration = [8, 6];
for (let simu2 = 0; simu2 < cxconfiguration.length; simu2++) {
  for (let simu = 0; simu < configuration.length; simu++) {
    const attempts = 10000000;
    counts = {};
    for (let i = 0; i < attempts; i++) {
      const ws = new DefenderDeck({
        deck: configuration[simu],
        cx: cxconfiguration[simu2],
        wr: 0,
        wrcx: 0,
        level: baselevel,
        clock: baseclock,
      });
      const tr = new AttackerDeck({
        deck: 20,
        trigger: 6,
      });
      for (let k = 0; k < 3; k++) {
        let millcount = 3;
        let fromdeck = false;
        if (millcount >= ws.deck) {
          millcount = ws.deck;
          fromdeck = true;
        }
        const hit = ws.mill(millcount);
        if (hit === 1 || hit === 2) {
          ws.sticks({ soul: 1, cx: 1 });
          ws.sticks({ soul: 1, cx: 0 });
        }
        if (hit === 0) {
          ws.sticks({ soul: 1, cx: 0 });
        }
        if (hit === 3) {
          ws.sticks({ soul: 1, cx: 1 });
        }
        if (fromdeck === true && hit > 0) {
          ws.deck -= 1;
          ws.cx -= 1;
        }
        if (fromdeck === true && hit < 3) {
          ws.deck -= 1;
        }
        if (fromdeck === false && hit > 0) {
          ws.wr -= 1;
          ws.wrcx -= 1;
        }
        if (fromdeck === false && hit < 3) {
          ws.wr -= 1;
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
    for (const combo in counts) {
      const count = counts[combo];
      const percentage = (aggregate_count / attempts) * 100;
      aggregate_count -= count;
      const [level, clock] = combo.split(',');
      if (level < 5) {
        console.log(`${combo}: ${percentage.toFixed(2)}% and [${count}]x`);
      }
    }
    const end_time = Date.now();
    console.log(`Execution time: ${Math.floor((end_time - start_time) / 60000)}m ${Math.floor((end_time - start_time) / 1000) % 60}s \n`);
  }
}