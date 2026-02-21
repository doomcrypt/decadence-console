import random
from constants import demons, pair_scores

positions = [
    "South (Deep Past)",
    "Memories & Dreams",
    "West (Destructive Influences)",
    "East (Creative Influences)",
    "North (Far Future)"
]

def create_deck():
    ranks = list(range(1, 10))
    suits = ['♣', '♦', '♥', '♠']
    return [(rank, suit) for rank in ranks for suit in suits]

def display_card(card):
    return f"{card[0]}{card[1]}"

def display_set(cards, pos_list, unpaired=None):
    if unpaired is None:
        unpaired = [True] * len(cards)
    for i, (card, pos) in enumerate(zip(cards, pos_list)):
        status = " (unpaired)" if unpaired[i] else " (paired)"
        print(f"{pos}: {display_card(card)}{status}")

def find_possible_pairs(flipped, set1_cards, unpaired):
    possibles = []
    for i, card in enumerate(set1_cards):
        if unpaired[i] and (flipped[0] + card[0] == 10):
            possibles.append(i)
    return possibles

def play_round(deck):
    if len(deck) < 10:
        print("Deck exhausted. Aeon ends.")
        return 0, deck

    set1 = [deck.pop() for _ in range(5)]
    set2 = [deck.pop() for _ in range(5)]
    unpaired = [True] * 5
    bonus = 0

    print("\nSet-1 (face-up):")
    display_set(set1, positions, unpaired)

    print("\nFlipping Set-2 one by one...")
    for flipped in set2:
        print(f"\nFlipped: {display_card(flipped)}")
        possibles = find_possible_pairs(flipped, set1, unpaired)
        if not possibles:
            print("No possible pairs.")
            continue

        print("Possible pairs from Set-1:")
        for idx in possibles:
            print(f"  {idx}: {positions[idx]} – {display_card(set1[idx])}")

        while True:
            try:
                choice_str = input("Choose index to pair (or -1 to skip): ").strip()
                choice = int(choice_str)
                if choice == -1:
                    break
                if choice in possibles:
                    unpaired[choice] = False
                    pair_key = tuple(sorted([flipped[0], set1[choice][0]]))
                    pair_bonus = pair_scores.get(pair_key, 0)
                    bonus += pair_bonus
                    print(f"Paired! +{pair_bonus}")
                    break
                else:
                    print("Invalid choice — try again.")
            except ValueError:
                print("Please enter a number.")

    penalty = sum(-set1[i][0] for i in range(5) if unpaired[i])
    round_score = bonus + penalty

    print(f"\nRound score: {round_score:+}  (bonus {bonus:+}, penalty {penalty:+})")
    display_set(set1, positions, unpaired)
    return round_score, deck

def main():
    print("Decadence — CCRU Lemurian Time-Sorcery Simulator")
    print("------------------------------------------------\n")

    deck = create_deck()
    random.shuffle(deck)
    cumulative = 0
    round_num = 1

    while True:
        print(f"——— Round {round_num}  (cards left: {len(deck)}) ———")
        round_score, deck = play_round(deck)
        cumulative += round_score
        print(f"Current Aeon total: {cumulative:+}\n")

        if cumulative <= 0 or len(deck) < 10:
            break
        round_num += 1
        input("Press Enter to continue to next round...")

    if cumulative > 0:
        print("POSITIVE AEON — angelic vector remains open.")
        print("(Angelic Index interpretation not yet implemented)")
    else:
        mesh = abs(cumulative) if cumulative < 0 else 0
        if mesh > 44:
            print("Catastrophic negativity — outside documented Pandemonium (Gt-45 zone).")
        else:
            demon = demons[mesh]
            print(f"\nAEON COLLAPSE — DEMONIC EMERGENCE")
            print(f"Mesh-{mesh:02d} : {demon['name']}")
            print(f"     Type : {demon['type']}")
            print(f"Attributes : {demon['attributes']}")

if __name__ == "__main__":
    main()
