from controllers import GameController
from validators import InvalidInputError, validate_retry_command
from views import InputView, OutputView

class Application:
    @staticmethod
    def run() -> None:
        OutputView.print_start_message()
        controller = GameController()

        while True:
            controller.play_round()

            while True:
                try:
                    retry_command = InputView.read_retry_command()
                    validate_retry_command(retry_command)
                    break
                except InvalidInputError as e:
                    OutputView.print_error(str(e))

            if retry_command == "2":
                break

# 시작 코드
if __name__ == "__main__":
    Application.run()