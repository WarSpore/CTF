from Crypto.Util.number import getPrime, isPrime, getRandomInteger
from gmpy2 import mpz

# Generate a safe prime (we'll use a smaller one for demonstration purposes)
def gen_safe_prime(bits=512):
    while True:
        q = getPrime(bits)  # Generate a large prime q
        p = 2 * q + 1
        if isPrime(p):
            return p

# Function for modular exponentiation
def mod_exp(base, exp, modulus):
    return pow(base, exp, modulus)

# ElGamal Encryption
def elgamal_encrypt(plain_text, p, g, pub_key):
    # Random number k for encryption
    k = getRandomInteger(128)  # Random integer for security
    c1 = mod_exp(g, k, p)  # c1 = g^k mod p
    c2 = (plain_text * mod_exp(pub_key, k, p)) % p  # c2 = m * pub_key^k mod p
    return (c1, c2)

# ElGamal Decryption
def elgamal_decrypt(ciphertext, p, private_key):
    c1, c2 = ciphertext
    # Calculate the modular inverse of c1^private_key mod p
    s = mod_exp(c1, private_key, p)
    s_inv = pow(s, -1, p)  # Inverse of s mod p
    # m = c2 * s_inv mod p
    plain_text = (c2 * s_inv) % p
    return plain_text

# Example usage
if __name__ == "__main__":
    # Step 1: Generate a prime p and generator g
    p = gen_safe_prime()  # Generate a safe prime
    g = 2  # A common generator for ElGamal encryption

    # Step 2: Generate private and public keys
    private_key = getRandomInteger(128)  # Private key 'a'
    pub_key = mod_exp(g, private_key, p)  # Public key 'pub_key = g^a mod p'

    print(f"Private key: {private_key}")
    print(f"Public key: {pub_key}")

    # Step 3: Encrypt a message (plain_text)
    plain_text = 42  # The message to encrypt (example)
    print(f"Plain text: {plain_text}")

    # Encrypt the message
    ciphertext = elgamal_encrypt(plain_text, p, g, pub_key)
    print(f"Encrypted ciphertext: {ciphertext}")

    # Step 4: Decrypt the message
    decrypted_message = elgamal_decrypt(ciphertext, p, private_key)
    print(f"Decrypted message: {decrypted_message}")
