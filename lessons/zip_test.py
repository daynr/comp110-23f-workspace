"""Testing my zip function."""
__author__ = "730690615"

from lessons.zip import zip


# Test: Zip two empty lists should result in an empty list.
def test_zip_empty_lists():
    """Test the zip function with two empty lists."""
    list1 = {}
    list2 = {}
    result = zip(list1, list2)
    return result


# Test: Zip two lists of equal length and compare the result.
def test_zip_equal_length_lists():
    """Test the zip function with two lists of equal length."""
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    result = zip(list1, list2)
    return result


# Test: Zip two lists of unequal length and ensure the result contains elements up to the length of the shortest list.
def test_zip_unequal_length_lists():
    """Test the zip function with two lists of unequal length."""
    list1 = [1, 2, 3, 4, 5]
    list2 = ['a', 'b', 'c']
    result = zip(list1, list2)
    return result


# Run the tests
test_zip_empty_lists()
test_zip_equal_length_lists()
test_zip_unequal_length_lists()
