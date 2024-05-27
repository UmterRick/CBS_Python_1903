import pytest


def test_cards_list_size():
    x = 53
    assert x == 52, "Wrong card list"


def test_cards_list_size_2():
    x = 52

    assert x == 52, "Wrong card list"


def test_player_data(test_player):
    print(test_player)
    assert test_player["score"] == 0
