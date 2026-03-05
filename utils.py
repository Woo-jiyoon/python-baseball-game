import random

def generate_unique_random_numbers(length: int = 3) -> list[int]:
    return random.sample(range(1, 10), length)

def parse_string_to_integers(numbers_str: str) -> list[int]:
    return [int(char) for char in numbers_str]