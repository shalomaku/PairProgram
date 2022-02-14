import pytest
from app.game import Game

@pytest.fixture
def g():
    return Game()
