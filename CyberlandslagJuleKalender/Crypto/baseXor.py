import base64

def xor_decrypt(base64_message, key, encoding='utf-8'):
    message_bytes = base64.b64decode(base64_message)
    decrypted_bytes = bytearray()
    for i in range(len(message_bytes)):
        decrypted_bytes.append(message_bytes[i] ^ key[i % len(key)])
    try:
        decrypted_string = decrypted_bytes.decode(encoding)
        return decrypted_string
    except UnicodeDecodeError:
        #print("Warning: Decoding with specified encoding failed. Returning raw bytes.")
        return ""



def main():
    base64_message = "4Yiv4YmO4Yi74YiH4YiY4Yie4YmI4YmL4YmP4YmN4YmO4YiZ4Yif4YmF4Yif4Yia4YmN4Yid4YmN4YmI4YmO4YmF4YmF4YmI4Yia4YmL4YmK4YiY4YmE4YiY4YmM4YmP4YmP4YiZ4YmJ4YiY4YiB=="
    print("Base64 Encoded Message:", base64_message)

    for key_length in range(1, 6):  # Trying keys of length 1 to 5
        for key_num in range(2 ** (8 * key_length)):  # Trying all possible keys of current length
            key = format(key_num, f'0{key_length * 2}X')  # Format key as hexadecimal string
            key_bytes = bytes.fromhex(key)  # Convert key to bytes

            decrypted_message = xor_decrypt(base64_message, key_bytes)
            if decrypted_message.startswith("S2G{}"):
                print(f"Key: {key_bytes}, Decrypted: {decrypted_message}")

if __name__ == "__main__":
    main()
