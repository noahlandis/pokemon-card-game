from pokemon import *

def test_get_damage_points():
    # setup
    charizard = Pokemon("Charizard", "Fire", 50, 15)
    expected = 15
    # invoke
    result = charizard.get_damage_points()
    # analyze
    assert expected == result


def test_is_fainted_true():
    # setup
    charizard = Pokemon("Charizard", "Fire", 0, 15)
    expected = True
    # invoke
    result = charizard.is_fainted()
    # analyze
    assert expected == result


def test_is_fainted_false():
    # setup
    charizard = Pokemon("Charizard", "Fire", 50, 15)
    expected = False
    # invoke
    result = charizard.is_fainted()
    # analyze
    assert expected == result

def test_str_():
    # setup
    charizard = Pokemon("Charizard", "Fire", 50, 15)
    expected = "Charizard"
    # invoke
    result = charizard.__str__()
    # analyze
    assert expected == result

def test_repr_():
    # setup
    charizard = Pokemon("Charizard", "Fire", 50, 15)
    expected = "<Charizard>:<Fire>:<50>"
    # invoke
    result = charizard.__repr__()
    # analyze
    assert expected == result

def test_water_douses_fire():
    # setup
    charizard = Pokemon("Charizard", "Fire", 50, 15)
    quagsire = Pokemon("Quagsire", "Water", 26, 6)
    expected = True
    # invoke
    result = quagsire > charizard
    # analyze
    assert expected == result


def test_fire_burns_grass():
    # setup
    charizard = Pokemon("Charizard", "Fire", 50, 15)
    breloom = Pokemon("Breloom", "Grass", 31, 6)
    expected = True
    # invoke
    result = charizard > breloom
    # analyze
    assert expected == result

def test_grass_consumes_water():
    # setup
    quagsire = Pokemon("Quagsire", "Water", 26, 6)
    breloom = Pokemon("Breloom", "Grass", 31, 6)
    expected = True
    # invoke
    result = breloom > quagsire
    # analyze
    assert expected == result

def test_equal_type_unequal_health():
    # setup
    water_type_1 = Pokemon("Water Type 1", "Water", 32, 6)
    water_type_2 = Pokemon("Water Type 2", "Water", 31, 6)
    expected = True
    # invoke
    result = water_type_1 > water_type_2
    # analyze
    assert expected == result

def test_equal_type_equal_health():
    # setup
    water_type_1 = Pokemon("Water Type 1", "Water", 32, 6)
    water_type_2 = Pokemon("Water Type 2", "Water", 32, 6)
    expected = True
    # invoke
    result = water_type_1 == water_type_2
    # analyze
    assert expected == result