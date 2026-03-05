import pytest

import utils
from models import Computer, Player, Referee
from validators import InvalidInputError, validate_retry_command

def test_generate_unique_random_numbers():
    numbers = utils.generate_unique_random_numbers()
    assert len(numbers) == 3
    assert len(set(numbers)) == 3
    assert all(1 <= n <= 9 for n in numbers)

def test_player_input_validation():
    with pytest.raises(InvalidInputError):
        Player("12")
    with pytest.raises(InvalidInputError):
        Player("abc")
    with pytest.raises(InvalidInputError):
        Player("112")
    with pytest.raises(InvalidInputError):
        Player("012")

def test_retry_command_validation():
    validate_retry_command("1")
    validate_retry_command("2")
    
    with pytest.raises(InvalidInputError):
        validate_retry_command("3")
    with pytest.raises(InvalidInputError):
        validate_retry_command("a")

def test_referee_logic():
    computer = Computer()
    computer._answer = [1, 2, 3]  

    assert Referee.judge(computer, Player("123")).strike == 3
    assert Referee.judge(computer, Player("123")).ball == 0

    assert Referee.judge(computer, Player("312")).strike == 0
    assert Referee.judge(computer, Player("312")).ball == 3

    assert Referee.judge(computer, Player("134")).strike == 1
    assert Referee.judge(computer, Player("134")).ball == 1

    assert Referee.judge(computer, Player("456")).strike == 0
    assert Referee.judge(computer, Player("456")).ball == 0