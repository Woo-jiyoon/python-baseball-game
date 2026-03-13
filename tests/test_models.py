from baseball.models import Computer, Player, Referee

def test_referee_logic():

    computer = Computer(answer=(1, 2, 3))

    # Player 생성 시 불변 튜플((1, 2, 3)) 주입
    assert Referee.judge(computer, Player(numbers=(1, 2, 3))).strike == 3
    assert Referee.judge(computer, Player(numbers=(1, 2, 3))).ball == 0

    assert Referee.judge(computer, Player(numbers=(3, 1, 2))).strike == 0
    assert Referee.judge(computer, Player(numbers=(3, 1, 2))).ball == 3

    assert Referee.judge(computer, Player(numbers=(1, 3, 4))).strike == 1
    assert Referee.judge(computer, Player(numbers=(1, 3, 4))).ball == 1

    assert Referee.judge(computer, Player(numbers=(4, 5, 6))).strike == 0
    assert Referee.judge(computer, Player(numbers=(4, 5, 6))).ball == 0