from dataclasses import dataclass

from baseball import utils

@dataclass(frozen=True)
class GameResult:
    strike: int = 0
    ball: int = 0

    @property
    def is_victory(self) -> bool:
        return self.strike == 3

class Computer:
    def __init__(self) -> None:
        # 생성된 리스트를 변경 불가능한 튜플로 저장
        self._answer: tuple[int, ...] = tuple(utils.generate_unique_random_numbers())

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