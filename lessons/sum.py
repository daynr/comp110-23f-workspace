"""Summing the elements of a list using different loops."""
__author__ = "730690615"


def w_sum(vals: list[float]) -> float:
    """Calculate the sum of all elements in vals using a while loop, vals (list[float]): List of floats to be summed."""
    total = 0.0
    i = 0
    while i < len(vals):
        total += vals[i]
        i += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Calculate the sum of all elements in vals using a for-in loop, vals (list[float]): List of floats to be summed."""
    total = 0.0
    for val in vals:
        total += val
    return total


def f_range_sum(vals: list[float]) -> float:
    """Calcuclate the sum of elements, vals (list[float]): List of floats to be summed."""
    total = 0.0
    for i in range(len(vals)):
        total += vals[i]
    return total


# Test cases
print(w_sum([1.1, 0.9, 1.0]))  # Should print 3.0
print(w_sum([]))  # Should print 0.0

print(f_sum([1.1, 0.9, 1.0]))  # Should print 3.0
print(f_sum([]))  # Should print 0.0

print(f_range_sum([1.1, 0.9, 1.0]))  # Should print 3.0
print(f_range_sum([]))  # Should print 0.0