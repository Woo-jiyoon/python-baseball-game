class InvalidInputError(ValueError):
    pass

class EmptyInputError(InvalidInputError):
    def __init__(self) -> None:
        super().__init__("입력값이 없습니다.")

class NotDigitError(InvalidInputError):
    def __init__(self) -> None:
        super().__init__("숫자만 입력해야 합니다.")

class InvalidLengthError(InvalidInputError):
    def __init__(self) -> None:
        super().__init__("3자리의 숫자를 입력해야 합니다.")

class OutOfRangeError(InvalidInputError):
    def __init__(self) -> None:
        super().__init__("1부터 9까지의 숫자만 입력 가능합니다.")

class DuplicateNumberError(InvalidInputError):
    def __init__(self) -> None:
        super().__init__("중복되지 않는 숫자를 입력해야 합니다.")

class InvalidCommandError(InvalidInputError):
    def __init__(self) -> None:
        super().__init__("1(재시작) 또는 2(종료)만 입력 가능합니다.")

def validate_baseball_numbers(user_input: str) -> list[int]:
    if not user_input.strip():
        raise EmptyInputError()
    if not user_input.isdigit():
        raise NotDigitError()
    if len(user_input) != 3:
        raise InvalidLengthError()
    if "0" in user_input:
        raise OutOfRangeError()
    if len(set(user_input)) != 3:
        raise DuplicateNumberError()

    # 검증이 끝난 후 정제된 데이터를 반환
    return [int(char) for char in user_input]

def validate_retry_command(user_input: str) -> None:
    if user_input not in ("1", "2"):
        raise InvalidCommandError()