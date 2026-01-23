import string
import random

alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'

# Rotate each character by the index of the key character
def times(a, b):
    # Ignore spaces
    if a in string.whitespace:
        return a
    return alphabet[(alphabet.index(a) * alphabet.index(b)) % len(alphabet)]

def caesar_decrypt(key, text):
    plaintext = ""
    for i in range(len(text)):
        plaintext += times(text[i], key)
    return plaintext

key = 'a'
while (key == 'a'):
	key = random.choice(alphabet)
print(key)

def main():
    # Danish text, flag is in text
    with open('crypto-longlive\encryption.txt', 'rb') as f:
        text = f.read().decode("utf-8").strip()
    for key in alphabet:
        if key == 'a':
            continue
        plaintext = caesar_decrypt(key, text)
        print(plaintext)

    # Once you have decrypted the ciphertext, remember to add flag formatting
    # For example:
    # ddc example flag
    # to
    # ddc{example_flag}


if __name__ == '__main__':
    main()
