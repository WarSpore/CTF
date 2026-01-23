
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes
from secrets import token_bytes, randbelow
from math import log2
import os

flag = os.environ.get("FLAG", "wack{flag_for_testing}")
p = getPrime(2048)
q = getPrime(2048)
n = p*q
e = 65537
phi = (p-1)*(q-1)
d = pow(e, -1, phi)

def pad(m, n):
    l = int(log2(n)) // 8
    pfx = token_bytes(l - len(m))
    while bytes_to_long(pfx + m) > n:
        pfx = token_bytes(l - len(m))
    return pfx.hex(), bytes_to_long(pfx + m)

def encrypt(m):
    p_hex, pm = pad(m, n)
    ct = pow(pm, e, n)
    return p_hex, ct

def decrypt(ct):
    return pow(ct, d, n)

def hexpad_to_int(p_hex: str) -> int:
    return int.from_bytes(bytes.fromhex(p_hex), 'big')

def B_for_message_len(mlen: int = 32) -> int:
    return 256**mlen

def ct_from_components(X: int, m_int: int, B: int, n: int, e: int) -> int:
    P = X * B + m_int
    return pow(P, e, n)

def main():
    secrets = [token_bytes(32) for _ in range(3)]
    numbers = [randbelow(3) for _ in range(100)]
    transcript = []
    for n_i in numbers:
        p_hex, ct = encrypt(secrets[n_i])
        X = hexpad_to_int(p_hex)
        transcript.append({"p_hex": p_hex, "X": X, "ct": ct})
    B = B_for_message_len(32)
    t0 = transcript[0]
    P0 = decrypt(t0["ct"])
    m_star_int = P0 - t0["X"] * B
    m_star_bytes = long_to_bytes(m_star_int, 32)
    try:
        m_star_idx = next(i for i, s in enumerate(secrets) if s == m_star_bytes)
    except StopIteration:
        raise RuntimeError("Recovered m* does not match any server secret (unexpected).")
    labels = [None] * len(transcript)
    for i, row in enumerate(transcript):
        if ct_from_components(row["X"], m_star_int, B, n, e) == row["ct"]:
            labels[i] = m_star_idx
    remaining_idxs = [j for j in range(3) if j != m_star_idx]
    m_ints = {j: bytes_to_long(secrets[j]) for j in remaining_idxs}

    for i, row in enumerate(transcript):
        if labels[i] is not None:
            continue
        X = row["X"]
        ct = row["ct"]
        match = None
        for j in remaining_idxs:
            if ct_from_components(X, m_ints[j], B, n, e) == ct:
                match = j
                break
        if match is None:
            raise RuntimeError(f"No matching secret found for row {i} (consistency error).")
        labels[i] = match
    print(f"Public parameters: n={n} e={e}")
    print("Can you distinguish between the following padded plaintexts")
    for row in transcript:
        print(f"p='{row['p_hex']}'\nct={row['ct']}")
    print("Before you answer I will give you a decryption querry")
    print("Input a ciphertext")
    print(f"> {t0['ct']}")
    print(f"Here is the result: {decrypt(t0['ct'])}")
    print("What are my numbers")
    recovered_numbers = ",".join(str(x) for x in labels)
    print(f"> {recovered_numbers}")
    if labels == numbers:
        print(f"Good job here is the flag: {flag}")
    else:
        print("Too bad, that is not correct")
        mism = [(i, labels[i], numbers[i]) for i in range(100) if labels[i] != numbers[i]]
        print("First mismatches (up to 10):", mism[:10])

if __name__ == "__main__":
    main()
