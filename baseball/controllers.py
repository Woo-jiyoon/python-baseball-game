from baseball.models import Computer, Player, Referee
from baseball.validators import InvalidInputError, validate_baseball_numbers, validate_retry_command
from baseball.views import InputView, OutputView
from baseball import utils

class GameController:
    def play_round(self) -> bool:
        """한 라운드를 플레이하고, 재시작 여부를 반환합니다."""
        computer = Computer()

        # 게임 진행 루프
        while True:
            try:
                numbers_str = InputView.read_numbers()
                
                # 검증 및 정제 후 Player 생성
                validate_baseball_numbers(numbers_str)
                parsed_numbers = tuple(utils.parse_string_to_integers(numbers_str))
                player = Player(numbers=parsed_numbers)
                
                # 판정 및 결과 출력
                result = Referee.judge(computer, player)
                OutputView.print_result(result)

                if result.is_victory:
                    OutputView.print_victory_message()
                    break

            except InvalidInputError as e:
                OutputView.print_error(str(e))
        
        # 재시작 여부 확인 루프
        while True:
            try:
                retry_command = InputView.read_retry_command()
                validate_retry_command(retry_command)
                return retry_command == "1"  # 1이면 True 2면 False
            except InvalidInputError as e:
                OutputView.print_error(str(e))