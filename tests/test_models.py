import pytest
from unittest.mock import patch
from baseball.models import Computer, Player, Referee, GameResult

# _answer 직접 접근 대신 patch를 사용하여 캡슐화 유지
@patch('baseball.utils.generate_unique_random_numbers')
def test_referee_logic(mock_generate):
    # 난수 생성 함수가 호출되면 [1, 2, 3]을 반환하도록 설정
    mock_generate.return_value = [1, 2, 3] 
    computer = Computer()

    # Player 생성 시 불변 튜플((1, 2, 3)) 주입
    assert Referee.judge(computer, Player(numbers=(1, 2, 3))).strike == 3
    assert Referee.judge(computer, Player(numbers=(1, 2, 3))).ball == 0

    assert Referee.judge(computer, Player(numbers=(3, 1, 2))).strike == 0
    assert Referee.judge(computer, Player(numbers=(3, 1, 2))).ball == 3

    assert Referee.judge(computer, Player(numbers=(1, 3, 4))).strike == 1
    assert Referee.judge(computer, Player(numbers=(1, 3, 4))).ball == 1

    assert Referee.judge(computer, Player(numbers=(4, 5, 6))).strike == 0
    assert Referee.judge(computer, Player(numbers=(4, 5, 6))).ball == 0

def test_game_result_properties():
    # 새로 추가된 GameResult의 속성성들이 잘 동작하는지 테스트
    victory_result = GameResult(strike=3, ball=0)
    assert victory_result.is_victory is True
    assert victory_result.is_nothing is False
    
    nothing_result = GameResult(strike=0, ball=0)
    assert nothing_result.is_victory is False
    assert nothing_result.is_nothing is True