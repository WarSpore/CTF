# Define the Base64 Alphabet
base64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
padding = '='

def shift_base64_string(input_string, shift_amount=5):
    result = []
    
    # Iterate through the string
    for char in input_string:
        if char == padding:
            # If it's padding, add it without change
            result.append(char)
        else:
            # Find the index of the character in the Base64 alphabet
            index = base64_alphabet.index(char)
            # Shift the index by the specified amount (wrap around using modulus)
            new_index = (index - shift_amount) % len(base64_alphabet)
            # Append the character at the new index in the Base64 alphabet
            result.append(base64_alphabet[new_index])
    
    # Return the transformed string
    return ''.join(result)

# Input Base64 string
input_string = "Z4OMj4eqRrOoS4mmRId6TYioR4KpRLR+RIh3TIV7SIF3eIp1kV=="

# Shift the string
shifted_string = shift_base64_string(input_string, shift_amount=5)

print("Original String:", input_string)
print("Shifted String:", shifted_string)
