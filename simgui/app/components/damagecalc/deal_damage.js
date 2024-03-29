class DefenderDeck {
    constructor(clock=0, clockcx=0, level=3, deck=20, cx=8, wr=0, wrcx=0, solutiondeck=0, solutiondeckcx=0) {
        this.clock = 0;
        this.clockcx = clockcx;
        this.level = level;
        this.deck = deck;
        this.cx = cx;
        this.wr = wr;
        this.wrcx = wrcx;
        this.solutiondeck = solutiondeck;
        this.solutiondeckcx = solutiondeckcx;
    }

    mill(amount) {
        let countcx = 0;
        for (let i = 0; i < amount; i++) {
          if (this.solutiondeck === 0) {
            if (this.deck === 0) {
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
          } else {
            this.solutiondeck -= 1;
            this.wr += 1;
            if (this.solutiondeckcx > 0) {
              this.solutiondeckcx -= 1;
              this.cx -= 1;
              this.wrcx += 1;
              countcx += 1;
            }
          }
        }
        return countcx;
      }
    
      mill_specific(amount, millcx) {
        for (let i = 0; i < amount; i++) {
          if (this.deck === 0) {
            this.refresh();
          }
          this.deck -= 1;
          if (millcx) {
            this.cx -= 1;
            this.wr += 1;
            this.wrcx += 1;
          } else {
            this.wr += 1;
          }
        }
      }
    
      check(amount, keepcx) {
        amount -= this.solutiondeck;
        for (let i = 0; i < amount; i++) {
          if (this.deck > 0) {
            const rnumber = Math.random();
            const rtracker = this.cx / this.deck;
            if (keepcx === 1) {
              if (rtracker > rnumber) {
                this.deck -= 1;
                this.cx -= 1;
                this.solutiondeck += 1;
                this.solutiondeckcx += 1;
              } else {
                this.mill_specific(1, 0);
              }
            } else {
              if (rtracker > rnumber) {
                this.mill_specific(1, 1);
              } else {
                this.deck -= 1;
                this.solutiondeck += 1;
              }
            }
          }
        }
      }
    
      topkek(amount, wrreliant) {
        for (let i = 0; i < amount; i++) {
          if (wrreliant) {
            if (this.wr > this.wrcx) {
              this.solutiondeck += 1;
              this.wr -= 1;
            }
          } else {
            this.solutiondeck += 1;
          }
        }
      }
    
      shuffleback(amount, wrreliant) {
        if (wrreliant) {
          if (this.wr - this.wrcx < amount) {
            amount = this.wr - this.wrcx;
          }
        }
        this.deck += amount;
      }

    damagecheck(soul) {
        for (let i = 0; i < soul; i++) {
            if (this.solutiondeck === 0) {
                if (this.deck === 0) {
                    this.refresh();
                }
                let rnumber = Math.random();
                let rtracker = this.cx / this.deck;
                this.deck -= 1;
                if (rtracker > rnumber) {
                    this.cx -= 1;
                    this.wr += i + 1;
                    this.wrcx += 1;
                    break;
                }
                else {
                    if (i === soul - 1) {
                        this.sticks(soul, 0);
                        return true;
                    }
                }
            }
            else {
                this.solutiondeck -= 1;
                if (this.solutiondeckcx > 0) {
                    this.solutiondeckcx -= 1;
                    this.cx -= 1;
                    this.wr += i + 1;
                    this.wrcx += 1;
                    break;
                }
                else {
                    if (i === soul - 1) {
                        this.sticks(soul, 0);
                        return true;
                    }
                }
            }
        }
    }

    sticks(soul, cx) {
        this.clock += soul;
        this.clockcx += cx;
        if (this.clock > 6) {
            this.clock = this.clock % 7;
            this.wr += 6;
            this.level = parseInt(parseInt(this.level) + 1);
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
        let rnumber = Math.random();
        let rtracker = this.cx / this.deck;
        this.deck -= 1;
        if (rnumber >= rtracker) {
            this.sticks(1, 1);
        }
        else {
            this.cx -= 1;
            this.sticks(1, 0);
        }
    }
    
    // Rest of the class functions go here
}
export default DefenderDeck;