from baseball.controllers import GameController
from baseball.views import OutputView

class Application:
    @staticmethod
    def run() -> None:
        OutputView.print_start_message()
        controller = GameController()

        should_continue = True
        while should_continue:
            # Controller가 모든 세부사항을 알아서 처리하고 결과만 줌
            should_continue = controller.play_round()

if __name__ == "__main__":
    Application.run()