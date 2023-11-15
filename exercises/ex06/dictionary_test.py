"""Applying our cases from the Dictionary Assignment."""
__author__ = "730690615"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest


def test_invert_key_error():
    """Test that invert function raises a KeyError when duplicate keys are encountered in the input dictionary."""
    with pytest.raises(KeyError):
        input_dict = {"a": "apple", "b": "banana", "c": "cherry", "d": "banana"}
        invert(input_dict)


def test_invert():
    """Test the invert function by checking if it correctly inverts the keys and values in the input dictionary."""
    input_dict = {"a": "apple", "b": "banana", "c": "cherry", "d": "date"}
    inverted_dict = invert(input_dict)
    expected_result = {'apple': 'a', 'banana': 'b', 'cherry': 'c', 'date': 'd'}
    assert inverted_dict == expected_result


def test_invert_empty_dict():
    """Test the invert function with an empty dictionary."""
    input_dict = {}
    inverted_dict = invert(input_dict)
    assert inverted_dict == {}


def test_favorite_color_same():
    """Test that favorite_color function raises a KeyError when duplicate colors are encountered in the input dictionary."""
    color_dict = {"Greg": "red", "Bob": "green", "Charlie": "blue"}
    most_popular = favorite_color(color_dict)
    assert most_popular == "blue"


def test_favorite_color():
    """Test the favorite_color function by checking if it correctly finds and returns the most popular color."""
    color_dict = {"Alice": "red", "Bob": "green", "Charlie": "blue", "David": "red"}
    most_popular = favorite_color(color_dict)
    assert most_popular == "red"


def test_favorite_color_no_colors():
    """Test the favorite_color function with an empty dictionary. It should raise a ValueError."""
    with pytest.raises(ValueError):
        color_dict = {}
        favorite_color(color_dict)


def test_count():
    """Test the count function by checking if it correctly counts the occurrences of values in the input list."""
    input_list = ["apple", "banana", "apple", "cherry", "banana"]
    counts = count(input_list)
    expected_result = {'apple': 2, 'banana': 2, 'cherry': 1}
    assert counts == expected_result


def test_count_empty_list():
    """Test the count function with an empty list. It should return an empty dictionary."""
    input_list = []
    counts = count(input_list)
    assert counts == {}


def test_count_single_element():
    """Test the count function with a list containing a single element. It should return a dictionary with a count of 1 for that element."""
    input_list = ["apple"]
    counts = count(input_list)
    expected_result = {'apple': 1}
    assert counts == expected_result


def test_alphabetizer():
    """Test the alphabetizer function by checking if it correctly categorizes words into lists based on their starting letters."""
    word_list = ["cat", "apple", "boy", "angry", "bad", "car"]
    alpha_dict = alphabetizer(word_list)
    expected_result = {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}
    assert alpha_dict == expected_result


def test_alphabetizer_empty_list():
    """Test the alphabetizer function with an empty list. It should return an empty dictionary."""
    word_list = []
    alpha_dict = alphabetizer(word_list)
    assert alpha_dict == {}


def test_alphabetizer_single_element():
    """Test the alphabetizer function with a list containing a single word. It should return a dictionary with the word categorized under its starting letter."""
    word_list = ["apple"]
    alpha_dict = alphabetizer(word_list)
    expected_result = {'a': ['apple']}
    assert alpha_dict == expected_result


def test_update_attendance():
    """Test the update_attendance function by updating the attendance log with new attendance records."""
    attendance_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    update_attendance(attendance_log, "Wednesday", "Kaleb")
    
    expected_result = {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa", "Vrinda"],
        "Wednesday": ["Kaleb"]
    }
    assert attendance_log == expected_result


def test_update_attendance_new_day():
    """Test the update_attendance function by adding a new day to the attendance log."""
    attendance_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Thursday", "Alice")
    expected_result = {
        "Monday": ["Vrinda", "Kaleb"],
        "Tuesday": ["Alyssa"],
        "Thursday": ["Alice"]
    }
    assert attendance_log == expected_result


def test_update_attendance_empty_log():
    """Test the update_attendance function with an empty attendance log. It should add the attendance record for the specified day."""
    attendance_log = {}
    update_attendance(attendance_log, "Monday", "Alice")
    expected_result = {"Monday": ["Alice"]}
    assert attendance_log == expected_result