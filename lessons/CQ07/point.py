"""CQ08 Modifying Point."""

__author__ = "730690615"


class Point:
    """Class to represent (x, y) coordinates."""

    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Initialize a Point with x and y attributes."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: float) -> None:
        """Scale the Point's coordinates in-place by a given factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: float) -> 'Point':
        """Create and return a new Point with scaled coordinates by a given factor."""
        scaled_x = self.x * factor
        scaled_y = self.y * factor
        return Point(scaled_x, scaled_y)

    def __str__(self) -> str:
        """Return a string representation of the Point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: 'int | float') -> 'Point':
        """Overload the multiplication * operator for Point object with a factor."""
        scaled_x = self.x * factor
        scaled_y = self.y * factor
        return Point(scaled_x, scaled_y)

    def __add__(self, factor: 'int | float') -> 'Point':
        """Overload the addition + operator for Point object with a factor."""
        new_x = self.x + factor
        new_y = self.y + factor
        return Point(new_x, new_y)