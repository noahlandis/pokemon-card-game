"""
This program simulates a pokemon battle.
author: Noah Landis
"""

class Pokemon:
    __slots__ = ["__name", "__type", "__health_points", "__damage_points"]

    def __init__(self, name, type, health_points, damage_points):
        self.__name = name
        self.__type = type
        self.__health_points = health_points
        self.__damage_points = damage_points

    def get_damage_points(self):
        """
        This function returns the damage points
        """
        return self.__damage_points
    
    def lose_round(self, damage_points):
        """
        This function reduces the pokemnon's health points by a given value
        """
        self.__health_points -= damage_points

    def is_fainted(self):
        """
        This function returns True if the Pokemon's health is less than or equal to 0, and True otherwise.
        """
        return self.__health_points <= 0

    def __str__(self):
        """
        This function returns the name field
        """
        return self.__name

    def __repr__(self):
        return "<" + self.__name + ">:<" + self.__type + ">:<" + str(self.__health_points) + ">"

    def __gt__(self, other):
        result = None
        if type(self) != type(other):
            result = False
        if self.__type == "Water" and other.__type == "Fire"\
        or self.__type == "Fire" and other.__type == "Grass"\
        or self.__type == "Grass" and other.__type == "Water":
            result = True
        elif self.__type == other.__type and self.__health_points != other.__health_points:
            result = self.__health_points > other.__health_points
        else:
            result = False
        return result

    def __eq__(self, other):
        result = None
        if type(self) != type(other):
            result = False
        if self.__type == other.__type and self.__health_points == other.__health_points:
            result = True
        else:
            result = False
        return result

    def __hash__(self):
        return hash(self.__damage_points)




