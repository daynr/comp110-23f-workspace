"""Returning the input of a list for a list that is odd and even."""

__author__ = "730690615"


def odd_and_even(input: list[int]) -> list[int]:
    """Returning the input as a list that are odd and even."""
    result = []
    i: int = 0

    while i < len(input):
        if input[i] % 2 == 1 and i % 2 == 0: 
            result.append(input[i])
            i += 1 
            
    return result
