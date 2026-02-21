import random

# Full Pandemonium Matrix (Mesh-00 to Mesh-44)
demons = {
    0: {"name": "Lurgo (Legba)", "type": "Amphidemon of Openings", "attributes": "Terminal Initiator, Door of Doors, Spinal-voyage rites."},
    1: {"name": "Duoddod", "type": "Amphidemon of Abstract Addiction", "attributes": "Duplicitous Redoubler, Pineal-regression, digital exactitude."},
    2: {"name": "Doogu (The Blob)", "type": "Cyclic Chronodemon of Splitting-Waters", "attributes": "Original-Schism, primordial breath, ambivalent capture."},
    3: {"name": "Ixix (Yix)", "type": "Chaotic Xenodemon of Cosmic Indifference", "attributes": "Abductor, occult terrestrial history."},
    4: {"name": "Ixigool (Djinn of the Magi)", "type": "Amphidemon of Tridentity", "attributes": "Over-Ghoul, unimpeded ascent, ultimate implications."},
    5: {"name": "Ixidod (King Sid)", "type": "Amphidemon of Escape-velocity", "attributes": "Zombie-Maker, crises through excess, illusion of progress."},
    6: {"name": "Krako (Kru, Karak-oa)", "type": "Amphidemon of Burning-Hail", "attributes": "Croaking Curse, subsidence, heaviness of fatality."},
    7: {"name": "Sukugool (Old Skug)", "type": "Cyclic Chronodemon of Deluge and Implosion", "attributes": "Sucking-Ghoul, cycle of creation/destruction, submersion."},
    8: {"name": "Skoodu (Li'l Scud)", "type": "Cyclic Chronodemon of Switch-Crazes", "attributes": "Fashioner, historical time, passage through the deep."},
    9: {"name": "Skarkix (Sharky, Scar-head)", "type": "Amphidemon of Anti-evolution", "attributes": "Buzz-Cutter, hermetic abbreviations, apocalyptic rapture."},
    10: {"name": "Tokhatto (Old Toker, Top Cat)", "type": "Amphidemon of Talismania", "attributes": "Decimal Camouflage, number as destiny, Angel of the Cards."},
    11: {"name": "Tukkamu", "type": "Cyclic Chronodemon of Pathogenesis", "attributes": "Occulturation, optimal maturation, rapid deterioration."},
    12: {"name": "Kuttadid (Kitty)", "type": "Cyclic Chronodemon of Precarious States", "attributes": "Ticking Machines, maintaining balance, exhaustive vigilance."},
    13: {"name": "Tikkitix (Tickler)", "type": "Amphidemon of Vortical Delirium", "attributes": "Clicking Menaces, swirl-patterns, mysterious disappearances."},
    14: {"name": "Katak", "type": "Syzygetic Chronodemon of Cataclysmic Convergence", "attributes": "Desolator, tail-chasing, panic and religious fervor."},
    15: {"name": "Tchu (Tchanul)", "type": "Chaotic Xenodemon of Ultimate Outsideness", "attributes": "Source of Subnothingness, cosmic deletions."},
    16: {"name": "Djungo", "type": "Amphidemon of Subtle Involvements", "attributes": "Infiltrator, turbular fluids, surreptitious invasions."},
    17: {"name": "Djuddha (Judd Dread)", "type": "Amphidemon of Artificial Turbulence", "attributes": "Decentred Threat, machine-vortex, storm peripheries."},
    18: {"name": "Djynxx (Ching, The Jinn)", "type": "Syzygetic Xenodemon of Time-Lapse", "attributes": "Child Stealer, abstract cyclones, dust spirals."},
    19: {"name": "Tchakki (Chuckles)", "type": "Amphidemon of Combustion", "attributes": "Bag of Tricks, quenching accidents, conflagrations."},
    20: {"name": "Tchattuk (One Eyed Jack, Djatka)", "type": "Amphidemon of Unscreened Matrix", "attributes": "Pseudo-Basis, zero-gravity, cut-outs and UFO cover-ups."},
    21: {"name": "Puppo (The Pup)", "type": "Amphidemon of Larval Regression", "attributes": "Break-Outs, dissolving into slime, chthonic swallowings."},
    22: {"name": "Bubbamu (Bubs)", "type": "Cyclic Chronodemon of Relapse", "attributes": "After Babylon, hypersea, aquassassins."},
    23: {"name": "Oddubb (Odba)", "type": "Syzygetic Chronodemon of Swamp-Labyrinths", "attributes": "Broken Mirror, time loops, glamour."},
    24: {"name": "Pabbakis (Pabz)", "type": "Amphidemon of Crossroads", "attributes": "The Weaver, tangled paths, fateful decisions."},
    25: {"name": "Ababbatok (Abracadabra)", "type": "Cyclic Chronodemon of Suspended Decay", "attributes": "Frankensteinian experimentation, purifications."},
    26: {"name": "Papatakoo (Pataku)", "type": "Cyclic Chronodemon of Calendric Time", "attributes": "Ultimate success, rituals becoming nature."},
    27: {"name": "Bobobja (Bubbles, Beelzebub)", "type": "Amphidemon of Teeming Pestilence", "attributes": "Strange lights in the swamp, swarmachines."},
    28: {"name": "Minommo", "type": "Amphidemon of Submergance", "attributes": "Shamanic voyage, dream sorcery."},
    29: {"name": "Mur Mur (Murrumur, Mu(mu))", "type": "Syzygetic Chronodemon of the Deep Ones", "attributes": "Oceanic sensation, gilled-unlife."},
    30: {"name": "Nammamad", "type": "Cyclic Chronodemon of Subterranean Commerce", "attributes": "Voodoo in cyberspace, emergences."},
    31: {"name": "Mummumix (Mix-Up)", "type": "Amphidemon of Insidious Fog", "attributes": "Ocean storms, diseases from outer-space."},
    32: {"name": "Numko (Old Nuk)", "type": "Cyclic Chronodemon of Autochthony", "attributes": "Necrospeleology, vulcanism."},
    33: {"name": "Muntuk (Manta, Manitou)", "type": "Cyclic Chronodemon of Arid Seabeds", "attributes": "Ancient rivers, cloud-vaults."},
    34: {"name": "Mommoljo (Mama Jo)", "type": "Amphidemon of Xenogenesis", "attributes": "Cosmobacterial exogermination, extraterrestrial residues."},
    35: {"name": "Mombbo", "type": "Cyclic Chronodemon of Hybridity", "attributes": "Ophidian transmutation, surreptitious colonization."},
    36: {"name": "Uttunul", "type": "Syzygetic Xenodemon of Atonality", "attributes": "Crossing the iron-ocean, plutonics."},
    37: {"name": "Tutagool (Yettuk)", "type": "Amphidemon of Punctuality", "attributes": "The dark arts, rusting iron."},
    38: {"name": "Unnunddo (The False Nun)", "type": "Amphidemon of Endless Uncasing", "attributes": "Crypt-traffic, communication-grids."},
    39: {"name": "Ununuttix (Tick-Tock)", "type": "Chaotic Xenodemon of Absolute Coincidence", "attributes": "Numerical connection through absence."},
    40: {"name": "Ununak (Nuke)", "type": "Amphidemon of Convulsions", "attributes": "Secrets of the blacksmiths, subterranean impulses."},
    41: {"name": "Tukutu (Killer-Kate)", "type": "Amphidemon of Death-Strokes", "attributes": "Crash-signals, barkerian scarring."},
    42: {"name": "Unnutchi (Outch, T'ai Chi)", "type": "Chaotic Xenodemon of Coiling Outsideness", "attributes": "Asymmetric zygopoise, cybernetic anomalies."},
    43: {"name": "Nuttubab (Nut-Cracker)", "type": "Amphidemon of Metaloid Unlife", "attributes": "Lunacies, dragon-lines."},
    44: {"name": "Ummnu (Om, Omni, Amen, Omen)", "type": "Amphidemon of Earth-Screams", "attributes": "Crust-friction, anorganic tension."}
}

positions = [
    "South (Deep Past)",
    "Memories & Dreams",
    "West (Destructive Influences)",
    "East (Creative Influences)",
    "North (Far Future)"
]

pair_scores = {
    (1,9): 8, (9,1): 8,
    (2,8): 6, (8,2): 6,
    (3,7): 4, (7,3): 4,
    (4,6): 2, (6,4): 2,
    (5,5): 0
}

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
