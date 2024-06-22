from typing import List, Tuple

# List of connections between cities, each represented as a tuple of (origin, destination, flight_time)
connections: List[Tuple[str, str, int]] = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

# Initialize counter and sum variables
counter: int = 0
sum: float = 0.0

# Iterate over each connection to find those leading to 'Rome'
for city in connections:
    if city[1] == 'Rome':  # Check if the destination city is 'Rome'
        counter += 1  # Increment the counter for connections to 'Rome'
        sum += city[2]  # Add the flight time to the total sum

# Print the results
print(counter, 'connections lead to Rome with an average flight time of', sum / counter, 'minutes')
