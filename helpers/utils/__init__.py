from ..cookie import RORY_TOKEN, VIV_TOKEN
import requests


def get_puzzle_input(day_number, is_viv=False):
    """
    Get the advent of code input for the given day.
    Parameters
    ----------
    day_number: int
        The day to import the input for
    is_viv: bool
        Is this puzzle input for my smexy girlfriend
    Returns
    -------

    """
    TOKEN = VIV_TOKEN if is_viv else RORY_TOKEN
    return requests.get(f"https://adventofcode.com/2020/day/{day_number}/input", cookies={"session": TOKEN}).text.strip()
