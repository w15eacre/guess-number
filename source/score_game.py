"""This module is used to test and evaluate the effectiveness of guessing algorithms,
    such as random guessing or binary search algorithms, by running them over
    a large number of trials and calculating their average performance.
"""

from numpy import mean as np_mean
from numpy import random as np_random
from typing import Callable


def score_game(random_predict: Callable[[int], int]) -> int:
    """How many attempts on average (over 1000 trials) 
    does the algorithm take to guess the number.

    Args:
        random_predict (Callable[[int], int]): the guessing function

    Returns:
        int: the average number of attempts
    """

    np_random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np_random.randint(
        1, 100, size=(1000))  # загадали список чисел

    count_ls = [random_predict(number) for number in random_array]

    score = int(np_mean(count_ls))

    print(f"Your algorithm guesses the number on average in: {score} attempts")
    return score
