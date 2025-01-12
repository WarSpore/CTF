def reverse_hex_string(hex_string):
    # Remove the '0x' prefix if present
    hex_string = hex_string[2:]

    # Reverse the string in pairs (each byte)
    reversed_hex = ' '.join(reversed([hex_string[i:i+2] for i in range(0, len(hex_string), 2)]))

    # XOR each byte with 0x9
    xor_result = ' '.join([format(int(byte, 16) ^ 0x9, '02x') for byte in reversed_hex.split()])

    # Add the '0x' prefix again
    reversed_xor_hex = xor_result

    return reversed_xor_hex
# Example usage
hex_strings = ["0x3d7d3c726e68656f","0x70656a387d3c387d","0x7b6e56643d563856","0x287d3d3a","0x74"]
for hex_string in hex_strings:
    print(reverse_hex_string(hex_string),end="")
