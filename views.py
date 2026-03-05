from models import GameResult

class InputView:
    @staticmethod
    def read_numbers() -> str:
        return input("숫자를 입력해주세요 : ")

    @staticmethod
    def read_retry_command() -> str:
        return input("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.\n")

class OutputView:
    @staticmethod
    def print_start_message() -> None:
        print("숫자 야구 게임을 시작합니다.")

    @staticmethod
    def print_result(result: GameResult) -> None:
        if result.strike == 0 and result.ball == 0:
            print("낫싱")
            return

        messages = []
        if result.ball > 0:
            messages.append(f"{result.ball}볼")
        if result.strike > 0:
            messages.append(f"{result.strike}스트라이크")

        print(" ".join(messages))

    @staticmethod
    def print_victory_message() -> None:
        print("3개의 숫자를 모두 맞히셨습니다! 게임 종료")

    @staticmethod
    def print_error(error_message: str) -> None:
        print(f"[ERROR] {error_message}")