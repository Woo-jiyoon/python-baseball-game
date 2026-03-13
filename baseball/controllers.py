from baseball.models import Computer, Player, Referee
from baseball.validators import InvalidInputError, validate_baseball_numbers, validate_retry_command
from baseball.views import InputView, OutputView

class GameController:
    def play_round(self) -> bool:
        """한 라운드를 플레이하고 재시작 여부를 반환합니다."""
        computer = Computer()

        while True:
            try:
                numbers_str = InputView.read_numbers()
                
                # 검증과 파싱을 한 번에 처리
                parsed_numbers = tuple(validate_baseball_numbers(numbers_str))
                player = Player(numbers=parsed_numbers)
                
                result = Referee.judge(computer, player)
                OutputView.print_result(result)

                if result.is_victory:
                    OutputView.print_victory_message()
                    break

            except InvalidInputError as e:
                OutputView.print_error(str(e))
        
        while True:
            try:
                retry_command = InputView.read_retry_command()
                validate_retry_command(retry_command)
                return retry_command == "1"
            except InvalidInputError as e:
                OutputView.print_error(str(e))