from pokemon import *
import csv
import random

class Pokedex:
    __slots__ = ["__pokemon_list"]

    NAME_FIELD = 0
    TYPE_FIELD = 1
    HP_FIELD = 2
    DP_FIELD = 3

    def __init__(self):
       self.__pokemon_list = []

    def load_pokemon(self, filename):
        """
        Creates a list  of pokemon
        """
        with open(filename) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for record in csv_reader:
                self.__pokemon_list.append(Pokemon(record[Pokedex.NAME_FIELD], record[Pokedex.TYPE_FIELD], 
                int(record[Pokedex.HP_FIELD]), int(record[Pokedex.DP_FIELD])))
            return self.__pokemon_list
    
    def create_parties(self):
        """
        Creates two pokemon sets with six pokemon each
        """
        party_1 = set()
        party_2 = set()
        random.shuffle(self.__pokemon_list)
        while len(party_1) < 6:
            party_1.add(self.__pokemon_list[random.randint(0, len(self.__pokemon_list) - 1)])
        while len(party_2) < 6:
            party_2.add(self.__pokemon_list[random.randint(0, len(self.__pokemon_list) - 1)])
        return party_1, party_2





    
