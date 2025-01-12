import aes
import random
from collections import defaultdict
from victim import encrypt_block, NORMAL_ROUNDS, PREMIUM_ROUNDS


def generate_differential_pairs(plaintext, difference):
    """Generate a plaintext pair with a specific XOR difference."""
    pt1 = plaintext
    pt2 = bytes([b ^ difference[i % len(difference)] for i, b in enumerate(pt1)])
    return pt1, pt2

def analyze_sbox_differentials():
    """Create a differential distribution table for the AES S-Box."""
    sbox = aes.SBOX  # Assuming `aes.py` provides the AES S-Box
    diff_table = defaultdict(int)

    for x in range(256):
        for y in range(256):
            input_diff = x ^ y
            output_diff = sbox[x] ^ sbox[y]
            diff_table[(input_diff, output_diff)] += 1

    return diff_table

def apply_differential_attack(pt1, pt2, ct1, ct2, round_count, diff_table):
    """
    Differential cryptanalysis targeting the SubBytes operation.
    Focus on matching known plaintext/ciphertext pairs with potential keys.
    """
    key_guesses = defaultdict(int)

    # XOR ciphertexts
    ct_diff = bytes([a ^ b for a, b in zip(ct1, ct2)])

    # Brute-force key byte guesses
    for byte_position in range(16):
        for guess in range(256):
            p1_byte = pt1[byte_position]
            p2_byte = pt2[byte_position]

            s1 = aes.SBOX[p1_byte ^ guess]
            s2 = aes.SBOX[p2_byte ^ guess]

            if s1 ^ s2 == ct_diff[byte_position]:
                key_guesses[(byte_position, guess)] += 1

    return key_guesses

def main():
    # Setup
    plaintext = b"knownplaintext!!"  # 16 bytes
    difference = b"\x01" * 16  # Example difference for XOR
    key = bytes([random.randint(0, 255) for _ in range(16)])  # Random AES key

    # Generate plaintext pairs with a fixed difference
    pt1, pt2 = generate_differential_pairs(plaintext, difference)
    print(f"Plaintext Pair: {pt1.hex()}, {pt2.hex()}")

    # Encrypt under normal mode (can be adjusted to PREMIUM_ROUNDS)
    ct1 = encrypt_block(pt1, key, NORMAL_ROUNDS)
    ct2 = encrypt_block(pt2, key, NORMAL_ROUNDS)
    print(f"Ciphertext Pair: {ct1.hex()}, {ct2.hex()}")

    # Analyze S-Box differentials
    diff_table = analyze_sbox_differentials()

    # Apply differential cryptanalysis
    key_guesses = apply_differential_attack(pt1, pt2, ct1, ct2, NORMAL_ROUNDS, diff_table)

    # Display results
    print("Key Byte Guesses (Position, Guess):")
    for (pos, guess), count in sorted(key_guesses.items(), key=lambda x: -x[1]):
        print(f"Byte {pos}: Guess {guess} (Count: {count})")

if __name__ == "__main__":
    main()
