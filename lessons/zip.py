"""Combining two lists into a dictionary."""

from typing import List, Dict

__author__ = "730690615"


def zip(str_list: List[str], int_list: List[int]) -> Dict[str, int]:
    """Combine two lists into a dictionary."""
    # Check if the input lists have different lengths or if they are empty
    if len(str_list) != len(int_list) or not str_list or not int_list:
        return {}
    
    result = {}  # Initialize an empty dictionary

    for i in range(len(str_list)):
        result[str_list[i]] = int_list[i]  # Create key-value pairs in the dictionary
    
    return result