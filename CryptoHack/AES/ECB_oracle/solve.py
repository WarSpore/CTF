import requests
from urllib.parse import quote
from Crypto.Util.Padding import pad, unpad

def split_into_blocks(ciphertext_hex, block_size=16):
    # Convert the hex string to bytes
    ciphertext_bytes = bytes.fromhex(ciphertext_hex)
    
    # Split the byte array into blocks of the specified size
    blocks = [(ciphertext_bytes[i:i + block_size]).hex() for i in range(0, len(ciphertext_bytes), block_size)]
    return blocks
    

# Function to send the plaintext to the ECB encryption endpoint and extract the ciphertext
def send_to_encryption(plaintext,attempt):
    # Prepare the URL
    base_url = "https://aes.cryptohack.org/ecb_oracle/encrypt/"
    
    # URL encode the plaintext to handle special characters
    encoded_plaintext = quote(plaintext)
    # Full URL with the encoded plaintext
    full_url = base_url + encoded_plaintext + "/"
    
    # Send a GET request to the endpoint
    response = requests.get(full_url)
    
    # Check for successful response
    if response.status_code == 200:
        # Parse the JSON response to extract ciphertext
        response_json = response.json()  # Parse JSON response
        ciphertext = response_json.get("ciphertext", "")
        return ciphertext

# Example usage:
if __name__ == "__main__":
    # You can replace this with any string
    known = b"6u1n5_h473_3cb}"
    result = b""
    for b in range(15,32):
        if len(known) >=16:
            result = known + result
            known = known[:-1]

        print(b)
        for i in range(30,130):
            p = hex(i)[2:]
            attempt = (bytes.fromhex(p)+known).hex()
            plaintext_input = attempt+"ff"*(8+b)
            ciphertext = send_to_encryption(plaintext_input,attempt)
            blockc = split_into_blocks(ciphertext)
            if blockc[0] == blockc[-2]:
                print(bytes.fromhex(p),end="")
                known = bytes.fromhex(p) + known
