import pytest


@pytest.fixture()
def test_player():
    return {"name": "Player", "score": 0, "record": 100}
