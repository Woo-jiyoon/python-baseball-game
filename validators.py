class InvalidInputError(ValueError):
    pass

def validate_baseball_numbers(user_input: str) -> None:
    if not user_input or not user_input.strip():
        raise InvalidInputError("입력값이 없습니다.")
    if not user_input.isdigit():
        raise InvalidInputError("숫자만 입력해야 합니다.")
    if len(user_input) != 3:
        raise InvalidInputError("3자리의 숫자를 입력해야 합니다.")
    if "0" in user_input:
        raise InvalidInputError("1부터 9까지의 숫자만 입력 가능합니다.")
    if len(set(user_input)) != 3:
        raise InvalidInputError("중복되지 않는 숫자를 입력해야 합니다.")

def validate_retry_command(user_input: str) -> None:
    if user_input not in ("1", "2"):
        raise InvalidInputError("1(재시작) 또는 2(종료)만 입력 가능합니다.")