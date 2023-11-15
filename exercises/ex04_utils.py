"""List Utility."""

from typing import List

__author__ = "730690615"


def all(int_list: List[int], target_int: int) -> bool:
    """Check if the elements in the list are equal to the target integer.

    Args:
        int_list (list): A list of integers.
        target_int (int): The integer to compare elements with.

    Returns:
        bool: True if all elements match the target integer, False otherwise.
    """
    # Check if the list is empty, and return False in that case
    if not int_list:
        return False

    # Initialize a variable to keep track of whether all elements match the target int
    all_match = True

    # Iterate through the list and compare each element with the target int
    for num in int_list:
        if num != target_int:
            all_match = False
            break

    return all_match


def max(int_list: List[int]) -> int:
    """Find the maximum integer in a list.

    Args:
        int_list (list): A list of integers.

    Returns:
        int: The maximum integer in the list.

    Raises:
        ValueError: If the list is empty.
    """
    if not int_list:
        raise ValueError("max() arg is an empty List")

    max_num = int_list[0]  # Initialize max_num with the first element of the list

    for num in int_list:
        if num > max_num:
            max_num = num

    return max_num


def is_equal(list1: List[int], list2: List[int]) -> bool:
    """Check if two lists are equal in terms of their elements at each index.

    Args:
        list1 (list): The first list of integers.
        list2 (list): The second list of integers.

    Returns:
        bool: True if the lists are equal, False otherwise.
    """
    if len(list1) != len(list2):
        return False

    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False

    return True