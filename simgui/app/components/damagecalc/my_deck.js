class AttackerDeck {
  constructor(clock=0, clockcx=0, level=3, deck=20, cx=7, wr=0, wrcx=0, trigger=6) {
    this.clock = clock;
    this.clockcx = clockcx;
    this.level = level;
    this.deck = deck;
    this.cx = cx;
    this.wr = wr;
    this.wrcx = wrcx;
    this.trigger = trigger; //(13*(deck20+wr0))/43=6 #quick hack before we can declare custom trigger amounts
  }

  mill(amount) {
    let countcx = 0;
    for (let i = 0; i < amount; i++) {
      if (this.deck == 0) {
        this.refresh();
      }
      const rnumber = Math.random();
      const rtracker = this.cx / this.deck;
      this.deck -= 1;
      if (rtracker > rnumber) {
        this.cx -= 1;
        this.wr += 1;
        this.wrcx += 1;
        countcx += 1;
      } else {
        this.wr += 1;
      }
    }
    return countcx;
  }

  triggerdamage(triggers=1, soul=3) {
    for (let i = 0; i < triggers; i++) {
      if (this.deck == 0) {
        this.refresh();
      }
      const rnumber = Math.random();
      const rtracker = this.trigger / this.deck;
      this.deck -= 1;
      if (rtracker > rnumber) {
        this.trigger -= 1;
        soul += 1;
      }
    }
    return soul;
  }

  sticks(soul, cx) {
    this.clock += soul;
    this.clockcx += cx;
    if (this.clock > 6) {
      this.clock = this.clock % 7;
      this.wr += 6;
      this.level += 1;
      this.wrcx += this.clockcx;
      this.clockcx = 0;
    }
  }

  refresh() {
    this.deck += this.wr;
    this.wr = 0;
    this.cx = this.wrcx;
    this.wrcx = 0;
    this.refreshpenalty();
  }

  refreshpenalty() {
    const rnumber = Math.random();
    const rtracker = this.cx / this.deck;
    this.deck -= 1;
    if (rnumber >= rtracker) {
      this.sticks(1, 1);
    } else {
      this.cx -= 1;
      this.sticks(1, 0);
    }
  }
}

export default AttackerDeck;