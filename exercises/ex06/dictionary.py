"""Utilizing Dictionary Functions."""

__author__ = "730690615"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values in the input dictionary."""
    inverted_dict = {}
    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate key encountered: " + value)
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Finds and returns the most popular color from a dictionary of names and favorite colors."""
    names = []
    color_count = {}
    most_popular_color = None
    max_count = 0

    for name, color in color_dict.items():
        if name in names:
            raise KeyError("Duplicate name: " + name)
        
        names.append(color)

        if color not in color_count:
            color_count[color] = 1
        else:
            color_count[color] += 1

        if color_count[color] > max_count or (color_count[color] == max_count and color < most_popular_color):
            most_popular_color = color
            max_count = color_count[color]

    if most_popular_color is not None:
        return most_popular_color
    else:
        raise ValueError("No valid colors found in the input dictionary")

 
def count(input_list: list[str]) -> dict[str, int]:
    """Counts the occurrences of each value in a list and returns a dictionary with the counts."""
    count_dict: dict[str, int] = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Categorizes words into lists based on their starting letters."""
    alpha_dict: dict[str, list[str]] = {}
    for word in word_list:
        first_letter = word[0].lower()
        if first_letter in alpha_dict:
            alpha_dict[first_letter].append(word)
        else:
            alpha_dict[first_letter] = [word]
    return alpha_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates the attendance log with a new attendance record."""
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return attendance_dict


if __name__ == "__main__":
    # Example usage for count
    counts = count(["apple", "banana", "apple", "cherry", "banana"])
    print(counts)  # Output: {'apple': 2, 'banana': 2, 'cherry': 1}

    # Example usage for alphabetizer
    words = ["cat", "apple", "boy", "angry", "bad", "car"]
    alpha_dict = alphabetizer(words)
    print(alpha_dict)  # Output: {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}

    # Example usage for update_attendance
    attendance_log = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    update_attendance(attendance_log, "Wednesday", "Kaleb")
    print(attendance_log)