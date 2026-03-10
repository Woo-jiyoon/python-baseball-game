from dataclasses import dataclass

import utils
from validators import validate_baseball_numbers

@dataclass
class GameResult:
    strike: int = 0
    ball: int = 0

    @property
    def is_victory(self) -> bool:
        return self.strike == 3

class Computer:
    def __init__(self) -> None:
        self._answer: list[int] = utils.generate_unique_random_numbers()

    @property
    def answer(self) -> list[int]:
        return self._answer

class Player:
    def __init__(self, numbers_str: str) -> None:
        validate_baseball_numbers(numbers_str)
        self._numbers: list[int] = utils.parse_string_to_integers(numbers_str)

    @property
    def numbers(self) -> list[int]:
        return self._numbers

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