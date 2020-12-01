from .cookie import TOKEN
import requests


def get_puzzle_input(day_number):
    """
    Get the advent of code input for the given day.
    Parameters
    ----------
    day_number: int
        The day to import the input for

    Returns
    -------

    """
    return requests.get(f"https://adventofcode.com/2020/day/{day_number}/input", cookies={"session": TOKEN}).text.strip()
