from baseball import utils

def test_generate_unique_random_numbers():
    numbers = utils.generate_unique_random_numbers()
    assert len(numbers) == 3
    assert len(set(numbers)) == 3
    assert all(1 <= n <= 9 for n in numbers)