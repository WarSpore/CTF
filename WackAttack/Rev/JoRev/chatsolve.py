import numpy as np
import string
import itertools

def custom_function(x):
    return ((81 * x) % 1024) >> 2

def binary_sum(k):
    return k + binary_sum(k - 1) if k > 0 else 0

def check_flag(input_string):
    to_array = np.array
    l = to_array([ord(c) + 5 for c in input_string])

    # Ensure the sum of the array is less than 145 raised to the power of the length of the array
    if not sum(l) < 145 ** len(l):
        return False

    # Ensure the length of the array matches 20 (from the calculation)
    if len(l) != 20:
        return False

    # Seed the random number generator with the first element of the array `l`
    np.random.seed(l[0])

    # Generate an array of random integers between 0 and 183 with the length of `l`
    random_args = {"size": len(l)}
    k = np.random.randint(0, 183, **random_args)

    # Ensure that the first element (which satisfies the condition) equals 115 ('s' in ASCII)
    try:
        if l[3:][k[:-3] % 4 == 3][0] != 115:
            return False
    except IndexError:
        return False

    # Ensure that a specific section of the array (modulo 4) matches a specific sequence
    if not (l[3:][k[:-3] % 4 == 0] ^ -4 == to_array([-116, -114, -119, -126, -104, -106])).all():
        return False

    # Ensure that another section matches after applying the custom function
    if not (custom_function(l[3:][k[:-3] % 4 == 2]) == to_array([207, 105, binary_sum(19) + binary_sum(3) + binary_sum(2) - binary_sum(1), 72])).all():
        return False

    # Check another section by cubing the elements and subtracting 2
    if not (l[3:][k[:-3] % 4 == 1] ** 3 - 2 == to_array([int(a) for a in "20971503181584631574623195110399999831685157".split("3")])).all():
        return False

    return True

# Generate possible middle parts of the flag
middle_charset = string.ascii_letters + string.digits + "_?!"
middle_length = 14  # Length between 'wack{' and '}'
prefix = "wack{"
suffix = "}"

# Create combinations for the middle part
for middle in itertools.product(middle_charset, repeat=middle_length):
    flag = prefix + ''.join(middle) + suffix
    if check_flag(flag):
        print(f"Found a valid input: {flag}")
        break
