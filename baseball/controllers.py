from models import Computer, Player, Referee
from validators import InvalidInputError
from views import InputView, OutputView

class GameController:
    def play_round(self) -> None:
        computer = Computer()

        while True:
            try:
                numbers_str = InputView.read_numbers()
                player = Player(numbers_str)
                result = Referee.judge(computer, player)
                
                OutputView.print_result(result)

                if result.is_victory:
                    OutputView.print_victory_message()
                    break

            except InvalidInputError as e:
                OutputView.print_error(str(e))