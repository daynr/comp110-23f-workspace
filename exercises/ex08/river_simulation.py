"""Simulating the River."""
from exercises.ex08.river import River

# Create a river with 10 Fish and 2 Bears
my_river = River(10, 2)

# View the initial state of the river
my_river.view_river()

# Simulate one day in the river
my_river.one_river_day()

# Simulate one week in the river
my_river.one_river_week()
