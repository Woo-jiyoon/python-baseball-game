import pytest
from baseball.validators import InvalidInputError, validate_retry_command, validate_baseball_numbers

def test_player_input_validation():
    # Validator를 직접 테스트하도록 분리
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("12")
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("abc")
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("112")
    with pytest.raises(InvalidInputError):
        validate_baseball_numbers("012")

def test_retry_command_validation():
    validate_retry_command("1")
    validate_retry_command("2")
    
    with pytest.raises(InvalidInputError):
        validate_retry_command("3")
    with pytest.raises(InvalidInputError):
        validate_retry_command("a")