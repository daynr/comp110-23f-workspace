"""List Utility."""

__author__ = "730690615"


def all(int_list, target_int):
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


def max(int_list):
    if not int_list:
        raise ValueError("max() arg is an empty List")
    
    max_num = int_list[0]  # Initialize max_num with the first element of the list

    for num in int_list:
        if num > max_num:
            max_num = num

    return max_num


def is_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True