def find_leftmost_set_bit(x):
    return x.bit_length() - 1

def generate_crc(data: int, poly: int) -> int:
    poly_len = poly.bit_length()
    rem = data << (poly_len - 1)
    while rem.bit_length() >= poly_len:
        rem ^= (poly << (rem.bit_length() - poly_len))
    return rem

def correct_single_bit_error(data_with_crc: int, poly: int) -> int:
    poly_len = poly.bit_length()
    data_len = 12
    crc_len = poly_len - 1

    # Check current CRC
    received_data = data_with_crc >> crc_len
    received_crc = data_with_crc & ((1 << crc_len) - 1)
    calculated_crc = generate_crc(received_data, poly)
    
    # If no error
    if received_crc == calculated_crc:
        return data_with_crc

    # Try flipping each bit to see if it corrects the error
    for i in range(data_len + crc_len):
        test_data_with_crc = data_with_crc ^ (1 << i)
        test_data = test_data_with_crc >> crc_len
        test_crc = test_data_with_crc & ((1 << crc_len) - 1)
        if generate_crc(test_data, poly) == test_crc:
            return test_data_with_crc

    # If no single-bit correction possible, return the original with an error flag
    return -1  # Indicating error could not be corrected

def process_blocks(binary_string: str, poly: int):
    block_size = 8 + (poly.bit_length() - 1)
    corrected_string = ""
    for i in range(0, len(binary_string), block_size):
        block = binary_string[i:i + block_size]
        data_with_crc = int(block, 2)
        corrected_block = correct_single_bit_error(data_with_crc, poly)
        if corrected_block == -1:
            corrected_string += block  # Uncorrected block
        else:
            corrected_string += format(corrected_block, f"0{block_size}b")
    return corrected_string

# Example usage
poly = int("10011", 2)  # Polynomial for CRC
binary_string = "011000001011010000111000011000111110011000111100011101001100001001100111011111110110011110010100011100010111011011111001010011011011010100011010001010011110010110010000001110111010001000011100011100011100010011111101010101101011110000110010001101100011011010100011001001010010001011011111011110000010001101100110010000110011011101110101010010111000011100011001010100011001001000111000001101010001011000100111010011000001011100011111111101010111010001001000001101000000001101011100010101101010101011011110011010100010010010010011010101010101010000010000001011011100011000011010010000111110001110011111011100011101010110001010010100100111001110011100011010101000011000101010001000101001001100011101111101100010010011100000010101111010011101101000011100100101001001000001010001111111010001001101111110100101011111001100"  # Example 12-bit blocks with CRC

corrected_string = process_blocks(binary_string, poly)
for i in range(0,len(corrected_string),12):
    print(chr(int(corrected_string[i:i+8],2)),end="")
#print(f"Corrected Binary String: {corrected_string}")
