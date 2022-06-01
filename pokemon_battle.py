from pokedex import *

def battle(party_1:set, party_2:set):
    round = 1
    while len(party_1) > 0 and len(party_2) > 0:
        print("Round:",round)
        print("Party 1:", party_1)
        print("Party 2:", party_2)
        # remove fighters from each set
        party_1_fighter = party_1.pop()
        party_2_fighter = party_2.pop()
        # draw
        if party_1_fighter == party_2_fighter:
            print(party_1_fighter, "and", party_2_fighter, "battle to a draw")
            party_1.add(party_1_fighter)
            party_2.add(party_2_fighter)
        # determine winner and winning party
        else:
            if party_1_fighter > party_2_fighter:
                winner = party_1_fighter
                loser = party_2_fighter
                winning_party = party_1
                losing_party = party_2
            else:
                winner = party_2_fighter
                loser = party_1_fighter
                winning_party = party_2
                losing_party = party_1
            # display results and reduce loser's health by winner's damage points
            print(winner, "has won the round over", loser)
            winning_party.add(winner)
            loser.lose_round(winner.get_damage_points())
            if loser.is_fainted():
                print(loser, "has fainted and is out of the battle")
            else:
                losing_party.add(loser)
        input("Press Enter for the next round...")
        print()
        round += 1

    if len(party_1) > 0:
        party_1 = winning_party
    else:
        party_2 = winning_party
    print("Winning Party:", winning_party)

            

                

    

def main():
    pokedex = Pokedex()
    pokedex.load_pokemon("data/pokemon.csv")
    party_1, party_2 = pokedex.create_parties()
    battle(party_1, party_2)

main()