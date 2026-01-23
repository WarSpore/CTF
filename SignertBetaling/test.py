from itertools import product

# Define the starting number and the possible subtractions
start = 100
subtractions = [5, 7, 8, 12]

# Use a set to store unique numbers reached
visited = set()

# Initialize a stack with the starting number
stack = [start]

# Perform DFS-like exploration
while stack:
    current = stack.pop()
    if current not in visited:
        visited.add(current)
        # Generate new numbers by subtracting each allowed value
        for sub in subtractions:
            new_value = current - sub
            if new_value >= 0:
                stack.append(new_value)

# Number of unique values encountered
num_unique_numbers = len(visited)

# Display the result
print(num_unique_numbers)
