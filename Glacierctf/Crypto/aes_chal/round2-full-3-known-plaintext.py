from itertools import product
from Crypto.Util.strxor import strxor
import aes
from utils import *
from typing import List

rounds = 2

def expand_key(key: bytes, rounds: int) -> List[List[int]]:
    round_keys = [[key[i:i + 4] for i in range(0, len(key), 4)]]
    while len(round_keys) < rounds + 1:
        base_key = b"".join(round_keys[-1])
        round_keys += aes.expand_key(base_key, 10)[1:]
    round_keys = [b"".join(k) for k in round_keys]
    round_keys = [aes.bytes2matrix(k) for k in round_keys]
    return round_keys[:rounds + 1]



def decrypt_block(ct: bytes, key: bytes, rounds: int) -> bytes:
    if len(ct) != 16 or len(key) != 16:
        raise ValueError("Invalid input length")

    subkeys = expand_key(key, rounds)[::-1]
    assert len(subkeys) == rounds + 1

    block = aes.bytes2matrix(ct)

    for i in range(rounds):
        aes.add_round_key(block, subkeys[i])
        aes.inv_mix_columns(block)
        aes.inv_shift_rows(block)
        aes.inv_sub_bytes(block)

    aes.add_round_key(block, subkeys[-1])

    return aes.matrix2bytes(block)



# Inverse state from ciphertext to start of Round 2
def inv_last_round(s, k):
    state = bytes2matrix(s)
    round_key = bytes2matrix(k)
    inv_mix_columns(state)
    add_round_key(state, round_key)
    inv_shift_rows(state)
    inv_sub_bytes(state)
    return matrix2bytes(state)

# Perform MixColumns operation on a given round key
def mix_columns_key(round_key):
    state = bytes2matrix(round_key)
    mix_columns(state)
    return matrix2bytes(state)

# Generate S-box Differential Distribution Table
def generate_sbox_different_distribution_table():
    table = {}
    for i in range(256):
        for j in range(256):
            diff = i ^ j
            diff_sbox = sbox[i] ^ sbox[j]
            if diff in table:
                if diff_sbox not in table[diff]:
                    table[diff].append(diff_sbox)
            else:
                table[diff] = [diff_sbox]
    return table

# Generate impossible states for given plaintext XOR differences
def generate_impossible_state(differential):
    impossible = []
    for i in range(4):
        impossible.append([])
        for j in range(256):
            if j not in sbox_ddt[differential[i]]:
                impossible[i].append(j)

    impossible_state = []
    for i in range(4):
        for j in impossible[i]:
            state = bytes2matrix(b'\x00' * i + bytes([j]) + b'\x00' * (15 - i))
            shift_rows(state)
            mix_columns(state)
            impossible_state.append(matrix2bytes(state))

    return impossible_state

# Generate a list of all possible byte values
def generate_256_list():
    return list(range(256))


# Main attack function
def attack(p1, p2, c1, c2):
    # Calculate XOR differences
    plain_diff = strxor(p1, p2)
    enc_diff = strxor(c1, c2)

    # Generate impossible states based on plaintext XOR difference
    impossible_state = generate_impossible_state(plain_diff)
    impossible_key = [None] * 16

    # Define ShiftRows ordering for the first round
    shifted_round1 = [0, 5, 10, 15, 4, 9, 14, 3, 8, 13, 2, 7, 12, 1, 6, 11]

    # Brute-force last round key one byte at a time
    for i in range(16):
        if impossible_key[i] is None:
            impossible_key[i] = []

        shifted_index = shifted_round1[i]
        for j in range(256):
            if j in impossible_key[i]:
                continue

            # Inverse ciphertexts to start of Round 2
            guess_key = b'\x00' * i + bytes([j]) + b'\x00' * (15 - i)
            inv_a = inv_last_round(c1, guess_key)
            inv_b = inv_last_round(c2, guess_key)
            inv_diff = strxor(inv_a, inv_b)

            # Check if inv_diff is in impossible states
            for k in impossible_state:
                if inv_diff[shifted_index] == k[shifted_index]:
                    impossible_key[i].append(j)

    # Generate possible key candidates
    list_256 = generate_256_list()
    possible_key = [list(set(list_256) - set(imp_key)) for imp_key in impossible_key]
    all_possible_keys = product(*possible_key)

    # Verify each possible key
    for possible_round_key in all_possible_keys:
        mixed_key = mix_columns_key(possible_round_key)
        master_key = inv_key_expansion(list(mixed_key), 2)
        decrypt_check = decrypt_block(c1, master_key,rounds)
        if decrypt_check == p1:
            print('[+] Possible Master Key:', master_key.hex())

    print("[-] No valid master key found.")
    return None

# Main driver
if __name__ == "__main__":
    # Replace these with the actual inputs
    p1 = bytes.fromhex("00112233445566778899aabbccddeeff")
    p2 = bytes.fromhex("102030405060708090a0b0c0d0e0f001")
    c1 = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")
    c2 = bytes.fromhex("7b0c785e27e8ad3f8223207104725dd4")
    sbox_ddt = generate_sbox_different_distribution_table()
    print("[+] Starting Differential Cryptanalysis Attack...")
    master_key = attack(p1, p2, c1, c2)

    if master_key:
        print(f"[+] Found Master Key: {master_key.hex()}")
    else:
        print("[-] Attack failed to find the master key.")
