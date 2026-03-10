import pytest
from unittest.mock import patch

from baseball import utils
from baseball.models import Computer, Player, Referee
from baseball.validators import InvalidInputError, validate_retry_command, validate_baseball_numbers

def test_generate_unique_random_numbers():
    numbers = utils.generate_unique_random_numbers()
    assert len(numbers) == 3
    assert len(set(numbers)) == 3
    assert all(1 <= n <= 9 for n in numbers)

def test_player_input_validation():
    # Validator를 직접 테스트하도록 분리
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("12")
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("abc")
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("112")
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("012")

def test_retry_command_validation():
    validate_retry_command("1")
    validate_retry_command("2")
    
    with pytest.raises(InvalidInputError):
        validate_retry_command("3")
    with pytest.raises(InvalidInputError):
        validate_retry_command("a")

# _answer 직접 접근 대신 patch를 사용하여 캡슐화 유지
@patch('baseball.utils.generate_unique_random_numbers')
def test_referee_logic(mock_generate):
    # 난수 생성 함수가 호출되면 [1, 2, 3]을 반환하도록 설정
    mock_generate.return_value = [1, 2, 3] 
    computer = Computer()

    # Player 생성 시 문자열("123") 대신 불변 튜플((1, 2, 3)) 주입
    assert Referee.judge(computer, Player(numbers=(1, 2, 3))).strike == 3
    assert Referee.judge(computer, Player(numbers=(1, 2, 3))).ball == 0

    assert Referee.judge(computer, Player(numbers=(3, 1, 2))).strike == 0
    assert Referee.judge(computer, Player(numbers=(3, 1, 2))).ball == 3

    assert Referee.judge(computer, Player(numbers=(1, 3, 4))).strike == 1
    assert Referee.judge(computer, Player(numbers=(1, 3, 4))).ball == 1

    assert Referee.judge(computer, Player(numbers=(4, 5, 6))).strike == 0
    assert Referee.judge(computer, Player(numbers=(4, 5, 6))).ball == 0