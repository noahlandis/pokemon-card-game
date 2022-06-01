from pokedex import *

def test_create_parties():
    # setup
    pokedex = Pokedex()
    pokedex.load_pokemon("data/pokemon.csv")
    expected_length = 6
    # invoke
    party_1, party_2 = pokedex.create_parties()
    # analyze
    assert len(party_1) == 6
    assert len(party_2) == 6
