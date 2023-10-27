"""Combining two lists into a dictionary."""
from typing import List, Dict

__author__ = "730690615"


def zip_lists(str_list: List[str], int_list: List[int]) -> Dict[str, int]:
    """Check if the input lists have the same length and must not be empty."""
    if len(str_list) != len(int_list) or len(str_list) == 0:
        return {}
    
    # Use a dictionary to create the resulting Dict[str,int]:
    result = {str_list[i]: int_list[i] for i in range(len(str_list))}

    return result
    