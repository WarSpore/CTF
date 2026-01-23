import string

alphabet = 'abcdefghijklmnopqrstuvwxyzæøå'
def clean_input(text):
    text = text.lower()
    tmp = [c if c in (alphabet + string.whitespace) else '' for c in text]
    return ''.join(tmp)

def subtract(a, b):
    if a not in alphabet:
        return a
    return alphabet[(alphabet.index(a) - alphabet.index(b)) % len(alphabet)]

def vigenere_decrypt(key, text):
    plaintext = ""
    for i in range(len(text)):
        plaintext += subtract(text[i], key[i % len(key)])
    return plaintext

def main():
    with open(r"crypto_vigedict\encryption.txt", "rb") as f:
        text = f.read().decode("utf-8")
    text = clean_input(text)
    with open(r"crypto_vigedict\danish_dict.txt", "rb") as f:
        keys = [line.decode("utf-8").strip() for line in f.readlines()]

    for key in keys:
        if len(key) == 9:
            decrypted_text = vigenere_decrypt(key, text)
            if 'er' in decrypted_text:
                print("decrypt:", decrypted_text)

if __name__ == '__main__':
    main()
