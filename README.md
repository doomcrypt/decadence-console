# Decadence

**A terminal-based Lemurian time-sorcery simulator**  
Inspired by the CCRU's Pandemonium Matrix, Decadology, and abyssal numerics.

This is a single-player card game/ritual engine that collapses aeonic scores into demonic emergence. Pair currents across two sets of five cards; accumulate bonus from syzygetic alignments (1+9, 2+8, …) while unpaired positions erode your vector with penalties. When the cumulative score drops to zero or below, the aeon fractures, and a Mesh-demon rises from the negative index.

## Gameplay Overview

- Standard 36-card deck (ranks 1–9, suits ♣♦♥♠)
- Each round draws 10 cards → two hidden sets of 5
- Set-1 is revealed (positions: South → North, past to future)
- Set-2 is flipped one by one
- Pair a flipped card with a Set-1 position if ranks sum to **10**
- Certain pairs grant bonus points (listed below)
- Unpaired Set-1 positions inflict penalty = **-rank**
- Cumulative score ≤ 0 → aeon collapse → demon manifestation (Mesh-00 to Mesh-44)

### Pair Bonuses

| Pair | Bonus |
|------|-------|
| 1+9  | +8    |
| 2+8  | +6    |
| 3+7  | +4    |
| 4+6  | +2    |
| 5+5  | 0     |

Other summing pairs give no bonus.

## Installation & Run

Requires **Python 3.6+** (no external dependencies).

```bash
# Clone and run
git clone https://github.com/doomcrypt/decadence.git
cd decadence
python3 decadence.py

# Or run directly from the raw file
python3 -c "$(curl -fsSL https://raw.githubusercontent.com/doomcrypt/decadence/main/decadence.py)"
