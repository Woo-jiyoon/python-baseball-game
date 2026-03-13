from dataclasses import dataclass

from baseball import utils

@dataclass(frozen=True)
class GameResult:
    strike: int = 0
    ball: int = 0

    @property
    def is_victory(self) -> bool:
        return self.strike == 3

    # 낫싱 상태를 모델 스스로 판단하도록 추가
    @property
    def is_nothing(self) -> bool:
        return self.strike == 0 and self.ball == 0

class Computer:
    # 스스로 난수를 만들지 않고 밖에서 만들어진 튜플만 받음
    def __init__(self, answer: tuple[int, ...]) -> None:
        self._answer = answer

    # 팩토리 메서드 : 게임에서 실제로 쓸 난수가 들어간 컴퓨터를 생성해 주는 생성기
    @classmethod
    def generate(cls) -> "Computer":
        numbers = tuple(utils.generate_unique_random_numbers())
        return cls(answer=numbers)

    @property
    def answer(self) -> tuple[int, ...]:
        return self._answer

@dataclass(frozen=True)
class Player:
    numbers: tuple[int, ...]

class Referee:
    @staticmethod
    def judge(computer: Computer, player: Player) -> GameResult:
        strike = 0
        ball = 0
        computer_numbers = computer.answer
        player_numbers = player.numbers

        for i, p_num in enumerate(player_numbers):
            if p_num == computer_numbers[i]:
                strike += 1
            elif p_num in computer_numbers:
                ball += 1

        return GameResult(strike=strike, ball=ball)