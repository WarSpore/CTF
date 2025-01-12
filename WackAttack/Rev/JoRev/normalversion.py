import numpy as np
import sys

# Make the print statement behave normally
length = len

# Define a lambda function that does some bitwise math
def custom_function(x):
    return ((81 * x) % 1024) >> 2

# Ensure that an argument is provided
# assert len(sys.argv) > 1

# Alias for numpy array creation
to_array = np.array

# Get the input string from the command line
input_string = "wack{numpy_15_wrerD}"
print(len(input_string))

# Convert input string to a numpy array, adding 5 to each character's ASCII value
l = to_array([ord(c) + 5 for c in input_string])

# Ensure that the sum of the array is less than 145 raised to the power of the length of the array
assert sum(l) < 145 ** len(l)

# Alias for numpy's random integer generator
random_int = np.random.randint

# Ensure the length of the array matches 20 (from the calculation)
assert len(l) == 3 * 5 + 2 ** 2 + int((1j ** 4).real)

# Define a recursive binary summation function
def binary_sum(k):
    return k + binary_sum(k - 1) if k > 0 else 0

# Seed the random number generator with the first element of the array `l`
np.random.seed(l[0])

# Define a dictionary to pass the length of the array to the random integer generator
random_args = {"size": length(l)}

# Generate an array of random integers between 0 and 183 with the length of `l`
k = random_int(0, 183, **random_args)

# Ensure that the first element (which satisfies the condition) equals 115 ('s' in ASCII)
assert l[3:][k[:-3] % 4 == 3][0] == 115

# Ensure that a specific section of the array (modulo 4) matches a specific sequence
assert (l[3:][k[:-3] % 4 == 0] ^ -4 == to_array([-116, -114, -119, -126, -104, -106])).all()

print(l)
print(l[3:][k[:-3] % 4 == 2])
print(custom_function(l[3:][k[:-3] % 4 == 2]))

# Ensure that another section matches after applying the custom function
assert (custom_function(l[3:][k[:-3] % 4 == 2]) == to_array([207, 105, binary_sum(19) + binary_sum(3) + binary_sum(2) - binary_sum(1), 72])).all()

# Check another section by cubing the elements and subtracting 2
assert (l[3:][k[:-3] % 4 == 1] ** 3 - 2 == to_array([int(a) for a in "20971503181584631574623195110399999831685157".split("3")])).all()

# Print that the input is correct
sys.stdout.write(f"{sys.argv[1]} is the correct flag\n")
