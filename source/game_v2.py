"""Guess the Number Game
The computer itself chooses and guesses the number.
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Randomly guess the number.

    Args:
        number (int, optional): The hidden number. Defaults to 1.
        The number should be in the range [1, 101).

    Returns:
        int: The number of attempts.
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # The guessed number
        if number == predict_number:
            break  # Exit the loop if the number is guessed
    return count
