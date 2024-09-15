"""Guess the Number Game
The computer itself guesses and finds the number
"""

import numpy as np


def bin_search_predict(number: int = 1) -> int:
    """Guess the number using a binary search algorithm.

    Args:
        number (int, optional): The number to guess. Defaults to 1.
        The number should be within the range [1, 101).

    Returns:
        int: The number of attempts taken to guess the number.
    """
    left_bound = 1  # Lower bound of the search range
    right_bound = 101  # Upper bound of the search range (exclusive)

    if number < 1 or number >= 101:
        raise ValueError(
            f"Invalid input argument, expected value in range "
            f"[{left_bound}, {right_bound}], your value: {number}"
        )

    count = 0

    while left_bound < right_bound:
        mid = (right_bound + left_bound) // 2  # Find the midpoint of the range
        if mid == number:
            break  # Exit the loop if the correct number is found
        elif mid < number:
            left_bound = mid + 1  # Shift the lower bound up
        elif mid > number:
            right_bound = mid  # Shift the upper bound down
        count += 1  # Increment the attempt counter

    return count
